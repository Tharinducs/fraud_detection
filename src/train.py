import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle
from config import MODEL_PATH, TRAIN_DATA, VECTORIZER_PATH
from preprocess import clean_text 

df = pd.read_csv(TRAIN_DATA)

df["Transaction_Description"] = df["Transaction_Description"].apply(clean_text)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Transaction_Description"]) #learns and transform
y = df["Fraudulent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

with open(MODEL_PATH, "wb") as model_file:
    pickle.dump(model, model_file)

with open(VECTORIZER_PATH, "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model trained and saved successfully!")