import pickle
from config import MODEL_PATH, VECTORIZER_PATH
from preprocess import clean_text

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

def predict_fraud(transaction_text):
    cleaned_text = clean_text(transaction_text) 
    vectorized_text = vectorizer.transform([cleaned_text])  #only transform
    prediction = model.predict(vectorized_text) 
    return "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"

example_text = "Large cash withdrawal of $10,000 detected."
print(predict_fraud(example_text))