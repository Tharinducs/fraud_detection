import config
import re
import nltk
from nltk.corpus import stopwords

PUNCTUATION_REGEX = re.compile(r"[^\w\s]")  # Compile regex for performance

try:
    STOPWORDS = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    STOPWORDS = set(stopwords.words("english"))


def clean_text(text: str) -> str:
    """Cleans text by removing special characters and stopwords."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    text = text.lower()
    text = PUNCTUATION_REGEX.sub("", text)  # Remove punctuation
    text = " ".join(word for word in text.split() if word not in STOPWORDS)  # Remove stopwords
    return text

# Test the function
print(clean_text("Cleans text by removing special characters and stopwords."))