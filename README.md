# 💳 PaySecure – Real-Time Credit Card Fraud Monitoring

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

PaySecure is a real-time fraud detection and risk monitoring system built using **FastAPI**, **Streamlit**, and **machine learning**. It simulates a live stream of credit card transactions, scores them for fraud, and displays the results on a responsive dashboard.

---

## 🚀 Features

- 🧠 **ML-powered Fraud Detection** using a trained Random Forest model
- 📡 **Live Transaction Simulator** generating synthetic data every second
- 📊 **Interactive Dashboard** with Streamlit to monitor frauds and risk distribution
- ⚙️ **FastAPI-based API** for prediction via `/predict/` endpoint
- 📁 **Real-time logging** of transactions in `.jsonl` format

---

## 🧠 Tech Stack

| Layer        | Technology |
|--------------|------------|
| API Server   | FastAPI, Uvicorn |
| Frontend UI  | Streamlit |
| ML Model     | Scikit-learn (Random Forest) |
| Data Handling| Pandas, NumPy |
| Dev Tools    | Joblib, JSON, Subprocess |

---

📦 PaySecure/
├── api/
│   ├── main.py
│   ├── schema.py
│   ├── feature_order.json
│   └── models/
│       ├── Random_Forest_Model.pkl
│       └── Robust_Scaler.pkl
├── dashboard/
│   └── app.py
├── simulator/
│   └── simulator.py
├── data/
│   └── transactions_log.jsonl
├── run_all.py
├── requirements.txt
└── README.md



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/paysecure.git
cd paysecure
```

## 2. Install Dependencies
### Make sure you have Python 3.9+ installed.
```bash
pip install -r requirements.txt
```

## 3. Run the Project
### Use the one-click starter script:
```bash
python run_all.py
```

This will automatically:

- ✅ Start the FastAPI backend: [http://localhost:8000](http://localhost:8000)
- ✅ Launch the Streamlit dashboard: [http://localhost:8501](http://localhost:8501)
- ✅ Run the simulator (generating fake transactions every second)

---

## 🔬 How It Works

1. The `simulator.py` script generates synthetic credit card transactions using random features similar to the [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
2. Each transaction is sent as a JSON payload to the FastAPI backend (`/predict/`).
3. The API uses a trained **Random Forest model** and **Robust Scaler** to:
   - Predict whether the transaction is fraudulent
   - Classify it into a risk level: **Low**, **Medium**, **High**, or **Critical**
4. The full transaction and prediction result are logged to `transactions_log.jsonl`.
5. The Streamlit dashboard reads this log every 2 seconds and updates:
   - 📄 **Last 10 Transactions**
   - 🔢 **Fraud Count and Metrics**
   - 📊 **Risk Category Distribution**
   - 📈 **Frauds Over Time**

---

## 📊 Screenshots

> Add screenshots or a demo GIF here  
> You can use [Loom](https://www.loom.com) or [Peek](https://github.com/phw/peek) to record a screen demo.

---

## 🔒 Security Notes

This is a demo prototype intended for learning and showcasing backend+dashboard integration.  
For real-world usage:

- 🔐 Use authentication for your API endpoints
- 🗄️ Use a production-grade logging system (e.g., PostgreSQL or S3)
- 🧼 Sanitize and validate all incoming data
- 🌐 Consider HTTPS, API rate limits, and secure deployment (e.g., Docker + Nginx)

---

## 📈 Future Improvements

- 🔐 Add user authentication and token-based access
- 🗃️ Store logs in a database instead of a flat file
- 🐳 Dockerize the entire stack (API + dashboard + simulator)
- ☁️ Deploy on Render, Heroku, or AWS
- 🧠 Add visual anomaly detection on the dashboard

---

## ✍️ Author

**Rohit Kumar Singh**  
[GitHub](https://github.com/rohit-singh-0) • [LinkedIn](https://www.linkedin.com/in/rohit-singh-0)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

