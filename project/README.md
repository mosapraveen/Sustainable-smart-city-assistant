
# 🌆 Sustainable Smart City Assistant

An AI-powered platform built to enhance urban sustainability, support smart governance, and improve citizen engagement using intelligent tools like chatbots, KPI forecasting, document summarization, and anomaly detection.

🚀 Live Demo: Coming Soon  
📦 Source Code: GitHub Repository (add link here)

---

## 🧠 Key Features

- 💬 AI Chat Assistant — Ask questions on sustainability & get intelligent responses using LLM.
- 📈 Energy Forecasting — Predict energy usage trends for upcoming years using ML (ARIMA).
- 📊 KPI Monitoring — Upload city performance data for forecasting and visual analysis.
- 🗃️ Citizen Feedback Form — Collect and categorize issues from residents (e.g., "Water Leak", "Waste").
- 📄 Document Summarizer — Upload city policies or reports and get concise summaries.
- 🌱 Eco Tips Generator — Generate sustainable living suggestions based on keywords.
- 🚨 Anomaly Detector — Automatically detect abnormal values in city KPI data.

---

## ⚙️ Tech Stack

| Tool            | Purpose                                      |
|------------------|----------------------------------------------|
| 🐍 Python        | Core programming language                    |
| 🌐 Streamlit     | Frontend UI framework for dashboards         |
| 🚀 FastAPI       | Backend API framework                        |
| 📦 OpenAI API    | LLM for chat assistant & summarization       |
| 📊 ARIMA (Statsmodels) | Forecasting time-series KPI data       |
| 🧪 Pydantic       | Data validation for API                     |
| 📂 dotenv         | Secure environment variables management     |
| 📌 Pinecone (optional) | Vector DB for semantic search           |

---

## 🖥️ Project Architecture

Frontend (Streamlit) → REST API (FastAPI) → ML/LLM Modules (Forecast, Chat, Summary)  
↪ Upload files (CSV/TXT/JSON), interact with AI, generate insights in real time.

---

## 🧪 Setup & Installation

1. Clone this repo:
   ```
   git clone https://github.com/yourusername/smart-city-assistant.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up .env file with your API key:
   ```
   OPENAI_API_KEY=sk-xxxxxxx...
   ```

4. Run the backend server:
   ```
   python app.py
   ```

5. Run the frontend interface:
   ```
   streamlit run ui.py
   ```

---

## 📂 Sample Dataset (for Forecasting)

| Year | Usage |
|------|-------|
| 2015 | 95    |
| 2016 | 105   |
| ...  | ...   |
| 2024 | 260   |

Save as: data/sample_city_data.csv

---

## 🧠 Sample Questions You Can Ask

- How can smart cities improve energy efficiency?
- What are the top 5 strategies for sustainable urban planning?
- How can my city reduce carbon emissions?
- What is a smart grid and how does it help?

---

## 🌟 Contributors

- MOSA PRAVEEN — Developer, Researcher  
- [Your Team Member Names]

---

## 📃 License

This project is licensed under the MIT License. See LICENSE for more details.
