import os
import requests
import google.generativeai as genai
from github import Github

# Load environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")
PR_NUMBER = os.getenv("GITHUB_REF").split("/")[-1]

# Authenticate with Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Authenticate with GitHub
github_client = Github(GITHUB_TOKEN)
repo = github_client.get_repo(REPO_NAME)
pr = repo.get_pull(int(PR_NUMBER))

# Get changed files
changed_files = os.popen("git diff --name-only HEAD^1 HEAD").read().strip().split("\n")

for file in changed_files:
    if not file.endswith(('.py', '.js', '.ts', '.jsx', '.tsx')):  # Limit to code files
        continue

    try:
        with open(file, "r", encoding="utf-8") as f:
            code_content = f.read()

        prompt = f"""
        Perform a code review for the following file: {file}.
        Provide concise, actionable feedback for improvements.
        
        ```{code_content}```
        """

        response = model.generate_content(prompt)

        if response and response.text:
            review_comment = f"**Code Review Suggestion for `{file}`:**\n\n{response.text}"
            pr.create_issue_comment(review_comment)

    except Exception as e:
        print(f"Error analyzing {file}: {e}")
