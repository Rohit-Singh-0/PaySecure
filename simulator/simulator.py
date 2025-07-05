import requests
import json
import random
import time
import os

API_URL = "http://localhost:8000/predict/"
LOG_FILE = "../data/transactions_log.jsonl"  # Adjust path if needed

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Generate a realistic fake transaction
def generate_transaction():
    transaction = {
        "Time": random.randint(0, 172800),  # seconds since first txn (2 days)
        "Amount": round(random.uniform(0.1, 10000), 2)
    }
    # Add V1 to V28 features
    for i in range(1, 29):
        transaction[f"V{i}"] = round(random.gauss(0, 1), 6)
    return transaction

# Run loop to simulate transactions
print("🚀 Starting real-time transaction simulation...\n")
while True:
    transaction = generate_transaction()

    try:
        # Send to FastAPI
        response = requests.post(API_URL, json=transaction)
        result = response.json()

        # Merge original + prediction
        full_record = {**transaction, **result}

        # Write to log
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(full_record) + "\n")

        print(f"✅ Logged transaction | Fraud: {result['fraud_prediction']} | Risk: {result['risk_category']}")
    except Exception as e:
        print(f"❌ Error sending transaction: {e}")

    time.sleep(1)  # simulate 1 transaction per second
