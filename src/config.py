import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #get abosulte path of the current script
DATA_DIR = os.path.join(BASE_DIR, "../data")
MODEL_PATH = os.path.join(BASE_DIR, "../models/text_classifier.pkl")

print("BASE DIR",BASE_DIR)
print("BASE DIR",DATA_DIR)
print("BASE DIR",MODEL_PATH)

TRAIN_DATA = os.path.join(DATA_DIR, "train.csv")
TEST_DATA = os.path.join(DATA_DIR, "test.csv")