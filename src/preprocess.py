import config
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

PUNCTUATION_REGEX = re.compile(r"[^\w\s]") 
NUMBERS_REGEX = re.compile(r"\d+")

def download_nltk_resources():
    """Download required NLTK resources"""
    try:
        # First try to find the resources
        nltk.data.find('tokenizers/punkt_tab')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK resources...")
        try:
            # Download the correct resources
            nltk.download('punkt_tab', quiet=True)
            nltk.download('stopwords', quiet=True)
            print("NLTK resources downloaded successfully")
        except Exception as e:
            print(f"Error downloading NLTK resources: {e}")
            print("Please try running these commands manually in Python:")
            print(">>> import nltk")
            print(">>> nltk.download('punkt')")
            print(">>> nltk.download('stopwords')")
            raise

# Download required NLTK resources
download_nltk_resources()

STOPWORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """Cleans text by removing special characters and stopwords."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    text = text.lower()
    text = PUNCTUATION_REGEX.sub("", text)
    text = NUMBERS_REGEX.sub("", text)
    words = word_tokenize(text)
    words = [word for word in words if word not in STOPWORDS]  # Use the global STOPWORDS set
    return " ".join(words)

# Test the function
print(clean_text("Cleans text by removing special characters 5 and stopwords."))