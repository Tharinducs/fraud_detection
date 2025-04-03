import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from config import MODEL_PATH, TEST_DATA, VECTORIZER_PATH
from preprocess import clean_text

df_test = pd.read_csv(TEST_DATA)

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

df_test["Transaction_Description"] = df_test["Transaction_Description"].apply(clean_text)
X_test = vectorizer.transform(df_test["Transaction_Description"])
y_test = df_test["Fraudulent"]

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
