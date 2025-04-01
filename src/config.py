import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../data")
BASE_MODEL_PATH = os.path.join(BASE_DIR,"../models")
MODEL_PATH = os.path.join(BASE_MODEL_PATH, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_MODEL_PATH,"vectorizer.pkl")

TRAIN_DATA = os.path.join(DATA_DIR, "train.csv")
TEST_DATA = os.path.join(DATA_DIR, "test.csv")

DOWNLOAD_NLTK_RESOURCES = True