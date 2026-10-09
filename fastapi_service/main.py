from fastapi import FastAPI
from pydantic import BaseModel
import random
import requests

app = FastAPI(

#title of webpage
    title="Credit Card Payment Service",
    description="FastAPI service for simulated credit card payments",
    version="1.0.0"
)


class PaymentRequest(BaseModel):
    card_id: int
    amount: float


class PaymentResponse(BaseModel):
    transaction_id: int
    card_id: int
    amount: float
    initial_status: str
    final_status: str


@app.get("/")
def home():
    return {
        "message": "FastAPI Payment Service Running"
    }


@app.post(
    "/payments/process",
    response_model=PaymentResponse,
    summary="Process Payment"
)
def process_payment(payment: PaymentRequest):

    initial_status = "PENDING"

    final_status = random.choice(
        ["SUCCESS", "FAILED"]
    )

    transaction_id = random.randint(
        1000,
        9999
    )

    try:
        response = requests.post(
            "http://127.0.0.1:8000/api/transactions/add/",
            json={
                "user": 3,
                "card": payment.card_id,
                "amount": payment.amount,
                "status": final_status
            }
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except Exception as e:
        print("Error:", e)

    return {
        "transaction_id": transaction_id,
        "card_id": payment.card_id,
        "amount": payment.amount,
        "initial_status": initial_status,
        "final_status": final_status
    }