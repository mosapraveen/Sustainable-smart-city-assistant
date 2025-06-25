import streamlit as st
import requests
import forecast  

st.set_page_config(page_title="Smart City Assistant", layout="centered")

st.title("🌆 Smart City Assistant")

st.header("🧠 Ask the Assistant")

question = st.text_input("Ask your question about city sustainability:")
if st.button("Ask"):
    try:
        response = requests.post("http://localhost:5000/query", json={"question": question})
        if response.status_code == 200:
            data = response.json()
            st.markdown(f"**Answer:** {data['answer']}")
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"❌ Failed to connect to Flask server: {e}")


st.header("📈 Forecasting Energy Usage")

if st.button("Run Forecast"):
    try:
        result_df = forecast.forecast_and_detect("data/sample_city_data.csv")
        st.write("📊 Predicted Usage for 2025–2027:")
        st.dataframe(result_df)
        st.image("forecast_plot.png", caption="Energy Usage Forecast")
    except Exception as e:
        st.error(f"⚠️ Forecasting failed: {e}")
