# 🚀 FX Intelligence Dashboard

### Real-Time Currency Analysis with Web Intelligence

An intelligent financial analytics platform that combines **live currency exchange rates** with **real-time web insights (Tavily API)** to provide actionable trading signals and market context.

---

## 📌 Overview

The **FX Intelligence Dashboard** is a cloud-deployable application designed for traders, analysts, and researchers. It integrates financial data with external intelligence sources to deliver:

* 📈 Live currency exchange rates
* 🧠 Insight generation based on market context
* 📰 Real-time news aggregation
* 🎯 Simple trading signals (Buy/Sell/Hold)
* 📊 Interactive dashboard for visualization

---

## 🧠 Key Features

* **Real-Time FX Data**
  Fetches live exchange rates using external APIs

* **Web Intelligence via Tavily**
  Retrieves relevant news and contextual insights

* **Automated Analysis Engine**
  Generates:

  * Market trend
  * Trading signal
  * Human-readable insights

* **Interactive Dashboard (Streamlit)**

  * Live-updating charts
  * Visual indicators
  * User-friendly interface

* **Cloud Deployment Ready**
  Fully containerized and deployable on Google Cloud Run

---

## 🏗️ Architecture

```
Frontend (Streamlit Dashboard)
        ↓
Backend API (FastAPI - Cloud Run)
        ↓
FX API + Tavily API
        ↓
Analysis Engine → Insights + Signals
```

---

## 📁 Project Structure

```
fx-intelligence/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── services/
│   │   ├── fx_service.py    # Currency data fetching
│   │   ├── tavily_service.py# Tavily API integration
│   │   └── analysis.py      # Insight + signal logic
│   └── models/
│       └── schema.py        # Request schema
│
├── dashboard.py             # Streamlit frontend
├── requirements.txt         # Dependencies
├── Dockerfile               # Container setup
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fx-intelligence.git
cd fx-intelligence
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set Environment Variables

```bash
export TAVILY_API_KEY=your_api_key_here
```

---

## ▶️ Running Locally

### Start Backend

```bash
uvicorn app.main:app --reload
```

Access API docs:

```
http://localhost:8000/docs
```

---

### Start Dashboard

```bash
streamlit run dashboard.py
```

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t fx-intelligence .
```

### Run Container

```bash
docker run -p 8080:8080 -e TAVILY_API_KEY=your_key fx-intelligence
```

---

## ☁️ Deploy to Google Cloud Run

```bash
gcloud run deploy fx-intelligence \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars TAVILY_API_KEY=your_key_here
```

---

## 📊 Example API Request

```json
POST /analyze
{
  "base": "USD",
  "target": "INR"
}
```

### Response

```json
{
  "pair": "USD/INR",
  "rate": 83.2,
  "trend": "uptrend",
  "signal": "buy",
  "news": ["Headline 1", "Headline 2"],
  "insight": "Recent news suggests..."
}
```

---

## 🔐 Security Practices

* API keys stored via environment variables
* No sensitive data hardcoded
* Input validation using Pydantic

---

## ⚡ Performance & Scalability

* Lightweight FastAPI backend
* Stateless design for Cloud Run scaling
* Efficient API calls and minimal memory usage

---

## 🧪 Testing & Maintainability

* Modular architecture (services, models, routes)
* Easily extendable for:

  * New data sources
  * Advanced analytics
  * AI integrations

---

## 🚀 Future Enhancements

* 🤖 Integration with Google Vertex AI (Gemini)
* 📊 Advanced technical indicators (RSI, MACD)
* 🌍 Multi-currency portfolio tracking
* 🔔 Alerts & notifications
* 📉 Historical trend analysis

---

## 🧠 Use Cases

* Traders seeking quick market signals
* Financial analysts monitoring trends
* Students learning FX markets
* AI-powered market intelligence systems

---

## 👨‍💻 Author

**Joshua Premkumar**
AI & Data Enthusiast | Six Sigma Professional

---

## ⭐ Acknowledgements

* Tavily API (Web Intelligence)
* Exchange Rate API
* FastAPI & Streamlit
* Google Cloud Run

---

## 📜 License

This project is open-source and available under the MIT License.