from config import MODEL_PATH, VECTORIZER_PATH
from fastapi import FastAPI
import pickle
from pydantic import BaseModel

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

app = FastAPI()

class TransactionRequest(BaseModel):
    transaction_description: str

@app.post("/predict")
def predict_fraud(transaction: TransactionRequest):
    text = [transaction.transaction_description]
    transformed_text = vectorizer.transform(text)
    prediction = model.predict(transformed_text)[0]
    return {"fraudulent": bool(prediction)}
