import streamlit as st
import pandas as pd
import time
import json
import os

# === Setup ===
st.set_page_config(page_title="Live Fraud Monitor", layout="wide")
st.title("📡 Live Credit Card Fraud Monitoring")

fraud_log = "../data/transactions_log.jsonl"

# === Placeholders ===
table_placeholder = st.empty()
risk_chart_placeholder = st.empty()
line_chart_placeholder = st.empty()

# Setup metric placeholders just once
st.subheader("🔢 Fraud Count")
col1, col2 = st.columns(2)
total_txn_metric = col1.empty()
fraud_txn_metric = col2.empty()

# === Load function ===
@st.cache_data(ttl=1)
def load_data():
    try:
        with open(fraud_log, "r") as f:
            data = [json.loads(line) for line in f.readlines()]
        return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame()

# === Live update loop ===
while True:
    df = load_data()

    if not df.empty:
        # === Last 10 Transactions ===
        latest_10 = df.tail(10).sort_index(ascending=False)
        table_placeholder.subheader("Last 10 Transactions")
        table_placeholder.dataframe(
            latest_10[["Time", "Amount", "fraud_prediction", "risk_category"]],
            use_container_width=True,
            hide_index=True,
            height=320
        )

        # === Update Metrics ===
        total_txn_metric.metric("Total Transactions", len(df))
        fraud_txn_metric.metric("Frauds Detected", int(df["fraud_prediction"].sum()))

        # === Risk Distribution Chart ===
        with risk_chart_placeholder:
            st.subheader("📊 Risk Category Distribution")
            st.bar_chart(df["risk_category"].value_counts())

        # === Fraud Over Time ===
        with line_chart_placeholder:
            st.subheader("📈 Fraud Over Time")
            frauds = df[df["fraud_prediction"] == 1]
            if not frauds.empty:
                frauds["Time (rounded)"] = frauds["Time"].astype(int) // 100
                st.line_chart(frauds["Time (rounded)"].value_counts().sort_index())

    time.sleep(2)
