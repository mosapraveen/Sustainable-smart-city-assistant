
# Sustainable Smart City Assistant 🌆💡

An AI-powered platform designed to support urban sustainability, improve governance, and enhance citizen engagement using large language models and modern data analytics.

---

## 🔍 Project Overview

The Sustainable Smart City Assistant is an intelligent platform that integrates advanced AI (including IBM Granite LLM), data forecasting, and semantic search to solve key urban challenges. The platform enables policymakers, citizens, and administrators to interact with data and documents effectively through a unified dashboard and modular backend.

---

## 🚀 Key Features

- 💬 Chat Assistant powered by IBM Granite LLM  
- 📊 KPI Forecasting using machine learning (ARIMA model)  
- ⚠️ Anomaly Detection in city metrics  
- 📁 Document Summarization and Semantic Search  
- 🌿 Eco Tips Generator  
- 📝 Citizen Feedback Form  
- 📈 Energy Consumption Visualization  

---

## 🧠 Technologies Used

| Component         | Technology                        |
|------------------|-----------------------------------|
| AI Model         | IBM Watsonx Granite LLM           |
| Frontend         | Streamlit                         |
| Backend API      | FastAPI                           |
| Vector DB        | Pinecone                          |
| Forecasting      | statsmodels, pandas, matplotlib   |
| NLP & Processing | OpenAI API, dotenv, requests      |
| File Support     | JSON, CSV, PDF, TXT               |

---

## 💼 Use Case Scenarios

🧾 Policy Summarization  
Upload city policy PDFs → Summarized into citizen-friendly formats via LLM.

🗣️ Citizen Feedback  
Residents submit issues (e.g., potholes, water leaks) → Categorized and stored.

📉 KPI Forecasting  
Upload metrics (e.g., energy usage) → Forecasted for 2025–2027.

🌱 Eco Tips  
Generate sustainable living suggestions using AI-powered tips.

⚡ Anomaly Detection  
Highlight unusual trends in urban data for quick administrative response.

💬 Chat Assistant  
Ask questions like “How can my city reduce emissions?” and get instant AI-driven advice.

---

## 📂 Project Structure

.
├── app.py                # Flask backend for chat assistant  
├── ai_engine.py          # LLM interaction module  
├── forecast.py           # Forecasting and plotting logic  
├── ui.py                 # Streamlit frontend  
├── data/                 # Sample CSVs and forecast data  
└── README.md             # You're here!  

---

## 📦 Setup Instructions

1. Clone this repo:  
   git clone https://github.com/mosapraveen/Sustainable-smart-city-assistant

2. Install required packages:  
   pip install -r requirements.txt

3. Add your API key to a .env file:  
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx

4. Run the Flask backend:  
   python app.py

5. In a new terminal, run the Streamlit UI:  
   streamlit run ui.py

---

## 📊 Example Dataset (for Forecasting)

| Year | Usage |
|------|-------|
| 2015 | 95    |
| 2016 | 105   |
| 2017 | 115   |
| 2018 | 130   |
| ...  | ...   |

Stored in: data/sample_city_data.csv

---

## 👨‍💻 Author

MOSA PRAVEEN  
CSE Student | Seshadri Rao Gudlavalleru Engineering College  
📧 Email: praveenmosa903@gmail.com  
🔗 LinkedIn: [mosa-praveen-83a444307](https://www.linkedin.com/in/mosa-praveen-83a444307)  
🐙 GitHub: [mosapraveen](https://github.com/mosapraveen)
