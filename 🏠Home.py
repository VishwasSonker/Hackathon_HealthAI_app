import streamlit as st
from streamlit_lottie import st_lottie
import json

with st.sidebar:
    st.markdown("## 🛠️ HealthAI Toolkit")
    st.markdown("_Built by Team AIvengers❤️_")

st.set_page_config(page_title="Homepage", layout="wide")
st.title("🧠 HealthAI: AI-powered Assistant")
st.markdown("_Predict, Chat, Visualize — All in One._")

def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# ✅ Correct relative path to JSON file
lottie_ai = load_lottie_file("assets/robot_greeting.json")


# Create two columns: left (content) and right (animation)
col1, col2 = st.columns([3, 1])  # 3:1 ratio, so animation is narrower

with col1:
    st.markdown("### ❌ The Problem")
    st.write("""
    In today’s fast-paced lifestyle, individuals often experience:

    - **Mood swings** and *emotional instability* without clear warning  
    - *Neglect of daily habits* like **sleep**, **exercise**, and **socialization**  
    - **Lack of self-awareness** about how lifestyle affects mental well-being  

    These issues contribute to:

    - 😓 **Mental fatigue**  
    - 📉 **Reduced productivity**  
    - ⚠️ **Decline in overall quality of life**
    """)

    # --- Solution Section ---
    st.markdown("### ✅ Our Solution")
    st.write(
        """
    **HealthAI** is a lightweight, AI-powered mental wellness tool designed to enhance **emotional well-being** through intelligent insights and real-time support:

    🔹 **Mood Score Predictor:** A custom-built ML model that predicts your *mood score* based on lifestyle habits like **sleep**, **screen time**, and **exercise**, helping users take proactive steps toward better mental health.

    🔹 **AI Mental Health Chatbot:** A 24/7 empathetic chatbot trained to simulate supportive conversations, provide *mental wellness tips*, and reduce the burden on real-world support systems.

    🔹 **Data Visualization & Insights:** Interactive visual dashboards that show how daily habits impact mood over time, encouraging healthier behavioral patterns.

    Together, these features form a **personal mental health companion** that empowers individuals to track, understand, and improve their emotional well-being.
    """)


    st.info("👈 Use the sidebar to explore: Mood Detector, AI Health Chatbot and Data Analytics.")



with col2:
    # Display the animation
    st_lottie(lottie_ai, height=300, width=350,speed=1, loop=True, quality="high", key="right_side_lottie")



