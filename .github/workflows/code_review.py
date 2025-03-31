import os
import requests
import subprocess
import google.generativeai as genai
from github import Github

# Load environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")

GITHUB_REF = os.getenv("GITHUB_REF", "")
if "pull" in GITHUB_REF:
    PR_NUMBER = GITHUB_REF.split("/")[2]  # Extract PR number
else:
    PR_NUMBER = None

if not PR_NUMBER:
    raise ValueError("Pull Request number could not be determined.")

# Authenticate with Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Authenticate with GitHub
github_client = Github(GITHUB_TOKEN)
repo = github_client.get_repo(REPO_NAME)
pr = repo.get_pull(int(PR_NUMBER))

def get_changed_files():
    """Get list of changed files in the PR"""
    try:
        # Get the base and head commits
        base_sha = pr.base.sha
        head_sha = pr.head.sha
        
        # Get the comparison
        comparison = repo.compare(base_sha, head_sha)
        
        # Extract changed files
        changed_files = [file.filename for file in comparison.files]
        return changed_files
    except Exception as e:
        print(f"Error getting changed files: {e}")
        return []

def get_file_content(file_path):
    """Get file content from GitHub repository"""
    try:
        content = repo.get_contents(file_path, ref=pr.head.ref)
        if content.encoding == 'base64':
            import base64
            return base64.b64decode(content.content).decode('utf-8')
        return content.decoded_content.decode('utf-8')
    except Exception as e:
        print(f"Error getting content for {file_path}: {e}")
        return None

def main():
    changed_files = get_changed_files()
    
    for file in changed_files:
        if not file.endswith(('.py', '.js', '.ts', '.jsx', '.tsx')):  # Limit to code files
            continue

        try:
            code_content = get_file_content(file)
            if not code_content:
                continue

            prompt = f"""
            Perform a code review for the following file: {file}.
            Provide concise, actionable feedback for improvements.
            Focus on:
            1. Code quality and best practices
            2. Potential bugs or issues
            3. Performance considerations
            4. Security concerns
            5. Suggestions for improvement
            
            ```{code_content}```
            """

            response = model.generate_content(prompt)

            if response and response.text:
                review_comment = f"**Code Review Suggestion for `{file}`:**\n\n{response.text}"
                pr.create_issue_comment(review_comment)
                print(f"Added review comment for {file}")

        except Exception as e:
            print(f"Error analyzing {file}: {e}")

if __name__ == "__main__":
    main()
