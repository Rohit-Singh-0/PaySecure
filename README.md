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

## 📁 Project Structure

