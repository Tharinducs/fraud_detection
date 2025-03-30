import config
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    """Cleans text by removing special characters and stopwords."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = " ".join(word for word in text.split() if word not in STOPWORDS)  # Remove stopwords
    return text

# Test the function
print(clean_text("Cleans text by removing special characters and stopwords is."))