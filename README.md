# 💳 PaySecure – Real-Time Credit Card Fraud Detection \& Analytics Platform

**PaySecure** is a comprehensive, production-ready fraud detection system that combines **real-time machine learning**, **interactive dashboards**, and **business intelligence analytics**. Built with **FastAPI**, **Streamlit**, and **advanced ML models**, it delivers enterprise-grade fraud detection with 99.97% AUC performance.

## 🚀 Key Features \& Performance

- 🧠 **Advanced ML Pipeline** - Random Forest model achieving **99.97% AUC score**
- 📡 **Real-Time Detection** - Live transaction simulation with millisecond response times
- 📊 **Interactive Dashboards** - Streamlit-powered monitoring and risk visualization
- 🔄 **Complete MLOps Workflow** - From data analysis to model deployment
- 📈 **Business Intelligence** - Comprehensive fraud analytics and reporting
- 🐳 **Docker Support** - Containerized deployment for scalability
- 🎯 **Risk Categorization** - 4-tier risk scoring system (Low/Medium/High/Critical)


## 🛠 Tech Stack

| **Layer** | **Technologies** |
| :-- | :-- |
| **API Backend** | FastAPI, Uvicorn, Pydantic |
| **Frontend Dashboard** | Streamlit, Plotly, Matplotlib |
| **Machine Learning** | Scikit-learn, Random Forest, SMOTE |
| **Data Processing** | Pandas, NumPy, RobustScaler |
| **Deployment** | Docker, Joblib |
| **Analytics** | Jupyter Notebooks, LaTeX Reports |
| **Visualization** | Tableau Dashboard, Seaborn |

## 📂 Project Structure

```
PaySecure/
├── 🔧 api/                          # FastAPI Backend
│   ├── main.py                      # Main API server
│   ├── schema.py                    # Pydantic data models
│   ├── feature_order.json           # ML feature ordering
│   └── models/                      # Trained ML models
│       ├── Random_Forest_Model.pkl  # Primary model (99.97% AUC)
│       ├── Logistic_Regression_model.pkl
│       └── Robust_Scaler.pkl        # Feature scaler
├── 📊 dashboard/                    # Streamlit Dashboard
│   └── app.py                       # Real-time monitoring interface
├── 🎮 simulator/                    # Transaction Simulator
│   └── simulator.py                 # Synthetic data generator
├── 📁 data/                         # Data Storage
│   ├── transactions_log.jsonl      # Real-time transaction logs
│   └── risk_analysis_df/           # Risk analysis datasets
├── 📓 Notebook/                     # Analysis & Development
│   ├── Fraud_Analysis_Notebook.ipynb # Complete ML pipeline
│   ├── feature_order.json          # Feature configuration
│   └── .ipynb_checkpoints/         # Notebook backups
├── 📋 reports/                      # Business Intelligence
│   ├── CreditCardFraudAnalysisReport.pdf
│   ├── Latex/                      # LaTeX analysis reports
│   │   ├── Fraud_Analysis_Notebook.tex
│   │   └── *.png                   # Analysis visualizations
│   └── Tableau Dashboard/
│       └── Credit Card Fraud Analysis Dashboard.twb
├── 🐳 Dockerfile                   # Container configuration
├── ⚙️ run_all.py                   # One-click startup script
├── 📋 requirements.txt             # Python dependencies
└── 📖 README.md                    # Project documentation
```


## ⚡ Quick Start Guide

### Prerequisites

- **Python 3.9+**
- **Docker** (optional, for containerized deployment)


### 1. Clone \& Setup

```bash
git clone https://github.com/Rohit-Singh-0/PaySecure.git
cd PaySecure
pip install -r requirements.txt
```


### 2. One-Click Launch 🚀

```bash
python run_all.py
```

**This automatically starts:**

- ✅ **FastAPI Backend**: `http://localhost:8000`
- ✅ **Streamlit Dashboard**: `http://localhost:8501`
- ✅ **Live Simulator**: Generates transactions every second


### 3. Docker Deployment (Alternative)

```bash
docker build -t paysecure .
docker run -p 8000:8000 -p 8501:8501 paysecure
```


## 🔬 How It Works

### **Real-Time Fraud Detection Pipeline**

1. **Transaction Generation**
    - `simulator.py` creates realistic credit card transactions
    - Features mirror the European Credit Card Dataset structure
    - Generates ~1.65 transactions/second (86,400 daily volume)
2. **ML-Powered Risk Assessment**
    - **Random Forest Model** (100 estimators, depth=10)
    - **99.97% AUC performance** on balanced dataset
    - **Feature Engineering**: Amount logging, hourly patterns
    - **SMOTE Balancing**: 284,315 legitimate + 284,315 synthetic fraud samples
3. **Risk Categorization**

```python
Low Risk     (0-10%)   → Normal processing
Medium Risk  (10-30%)  → Enhanced monitoring  
High Risk    (30-70%)  → Additional verification
Critical Risk (70-100%) → Immediate review/block
```

4. **Real-Time Dashboard**
    - Updates every 2 seconds
    - **Last 10 Transactions** with risk scores
    - **Fraud Metrics**: Total transactions, fraud count, detection rate
    - **Risk Distribution**: Visual breakdown by category
    - **Temporal Analysis**: Fraud patterns over time

## 📊 Business Impact \& Performance

### **Model Performance Metrics**

| Metric | Random Forest | Logistic Regression |
| :-- | :-- | :-- |
| **AUC Score** | **99.97%** | 99.75% |
| **Precision** | 99%/100% (Normal/Fraud) | 97%/99% |
| **Recall** | 100%/99% (Normal/Fraud) | 99%/97% |
| **Accuracy** | **99%** | 98% |

### **Financial Impact Analysis**
The following figures are modeled projections based on the dataset, pipeline performance, and business assumptions used in the accompanying Jupyter Notebook. They are intended for scenario planning and should not be interpreted as realized savings without production validation.
- **Annual Fraud Prevented**: \$3,075,307,500
- **Investigation Costs**: \$593,125
- **Net Annual Savings**: \$3,074,477,125
- **ROI**: **518,352%**

### Assumptions Used:
- Volume and base rates
    - Daily transaction volume: ~86,400 transactions/day (≈1.65 tx/s), extrapolated to a 365-day year (~31.5M transactions/year).
    - Fraud base rate: 0.173% (492 frauds out of 284,807 transactions from the benchmark European credit card dataset).
    - Annual transactions used in projections: ~31,536,000 (86,400×365).
- Model training and evaluation setup
    - Class imbalance handled with SMOTE during training to create a balanced training set.
    - Reported AUC (≈99.97%) is from balanced evaluation; production precision/recall will differ under true class imbalance.
    - A single operating threshold maps predicted probabilities to actions and risk tiers.
- Risk tiers to business actions (operational policy)
    - Low risk: auto-approve.
    - Medium risk: step-up verification; only a defined fraction routed to manual review.
    - High/Critical risk: block/hold (counted as prevented fraud if truly fraudulent) and routed to manual review.
    - Prevented fraud dollars are counted only for truly fraudulent transactions blocked/held at/above the threshold.
- Financial parameters (fixed scalars in the notebook)
    - Average loss per fraudulent transaction: fixed value defined in the notebook (used to convert prevented fraud counts to dollars).
    - Investigation unit cost: fixed per-case cost applied to all manually reviewed transactions.
    - Customer churn cost: fixed penalty per impacted legitimate transaction (false positive/challenged), multiplied by annual FP impact count.
- False positive and review workload assumptions
    - Annual manual reviews are derived from the number of flagged transactions by tier and the assumed review rates.
    - Customer churn cost is computed from the subset of legitimate transactions affected by controls and the per-event penalty.
- Latency, reliability, and scope
    - Assumes real-time decisioning meets SLA (no penalties modeled for delays/queues/fallbacks).
    - Recovery/chargebacks are not modeled; prevented fraud assumes timely block/hold.
    - Dataset-to-production generalization: the benchmark dataset’s fraud rate/patterns are used as a proxy; seasonal shifts, merchant mix differences, and adversarial drift are not modeled.
- Aggregation formulas (annual results)
    - Annual_fraud_prevented = (annual count of truly fraudulent transactions detected and blocked/held) × (average loss per fraud).
    - Annual_investigation_costs = (annual manual review count) × (investigation unit cost).
    - Customer_churn_cost = (annual impacted legitimate transaction count) × (per-event churn penalty).
    - Net_annual_savings = Annual_fraud_prevented − Annual_investigation_costs − Customer_churn_cost.
    - ROI% = (Net_annual_savings ÷ annual program/operational cost baseline) × 100.
- Notes on interpretation
    - All dollar impacts are modeled projections based on the above parameters and operating policy; they are not realized savings without production validation.
    - Results are sensitive to average loss per fraud, operating threshold (precision/recall trade-off), review rates, and daily volume; moderate changes in these inputs can materially alter prevention, costs, and ROI.

## 🔍 Advanced Analytics \& Reports

### **Jupyter Notebook Analysis**

- **Complete ML Pipeline**: Data exploration → Feature engineering → Model training → Evaluation
- **Business Intelligence**: Risk pattern analysis, temporal fraud detection
- **Visualization**: Correlation heatmaps, feature importance, risk distribution


### **Business Reports**

- **📄 PDF Report**: Comprehensive fraud analysis findings
- **📊 Tableau Dashboard**: Interactive business intelligence
- **📝 LaTeX Documentation**: Academic-quality analysis documentation


### **Key Findings**

- **Dataset**: 284,807 transactions over 2 days
- **Fraud Rate**: 0.173% (492 fraudulent out of 284,807)
- **Critical Features**: V14, V4, V11, V12, V10 (top fraud indicators)
- **Temporal Patterns**: Peak fraud activity during off-hours


## 🔐 Security \& Production Considerations

**Current Implementation** (Demo/Development):

- File-based transaction logging
- Basic API endpoints without authentication
- Local model storage

**Production Recommendations**:

- 🔐 **Authentication**: JWT tokens, API keys
- 🗄️ **Database Integration**: PostgreSQL, MongoDB for transaction storage
- 🌐 **Security**: HTTPS, input validation, rate limiting
- 📊 **Monitoring**: Logging, metrics, alerting systems
- ⚖️ **Compliance**: PCI DSS, data privacy regulations


## 🚀 Deployment Options

### **Development**

```bash
python run_all.py
```


### **Docker Production**

```bash
docker-compose up -d  # (if docker-compose.yml available)
# OR
docker run -p 8000:8000 -p 8501:8501 paysecure
```


### **Cloud Deployment**

- **AWS**: ECS, Lambda, API Gateway
- **GCP**: Cloud Run, App Engine
- **Azure**: Container Instances, App Service
- **Heroku/Render**: Direct deployment support


## 📈 Future Enhancements

### **Planned Features**

- 🔐 **User Authentication** with role-based access control
- 🗃️ **Database Integration** (PostgreSQL/MongoDB)
- 🧠 **Advanced ML Models** (XGBoost, Neural Networks, Ensemble methods)
- 📱 **Mobile App** for fraud alerts and monitoring
- 🔔 **Real-time Alerts** via email/SMS/webhooks
- 📊 **Advanced Analytics** with time-series forecasting
- 🌐 **Multi-language Support**
- 🔄 **Model Retraining Pipeline** with MLOps automation


### **Technical Improvements**

- **Microservices Architecture** with API Gateway
- **Message Queues** (Redis/RabbitMQ) for high-volume processing
- **Caching Layer** for improved response times
- **A/B Testing** framework for model comparison
- **Explainable AI** integration for regulatory compliance


## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request


## ✍️ Author

**Rohit Kumar Singh**

- 🐙 **GitHub**: [@Rohit-Singh-0](https://github.com/Rohit-Singh-0)
- 💼 **LinkedIn**: [Connect with Rohit](https://www.linkedin.com/in/rohit-singh-336859247/)
- 📧 **Email**: [Contact](mailto:rohitsingh3640@gmail.com)

***

***

**⭐ Star this repository if you found it helpful!**

**🔍 For detailed technical documentation, see the [Jupyter Notebook](Notebook/Fraud_Analysis_Notebook.ipynb) and [Reports](reports/) section.**
