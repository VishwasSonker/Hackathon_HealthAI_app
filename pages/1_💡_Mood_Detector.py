import streamlit as st
from streamlit_lottie import st_lottie
import json
import pickle
import numpy as np

with st.sidebar:
    st.markdown("## 🛠️ HealthAI Toolkit")
    st.markdown("_Built by Team AIvengers❤️_")


st.set_page_config(page_title="ML Predictor",layout="wide")

def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# ✅ Correct relative path to JSON file
lottie_ai = load_lottie_file("assets/ml_gif.json")


model = pickle.load(open(r'C:\VScode\hackathon\prototype_app\assets\mood_scorer.pkl', 'rb'))

st.title("🧠 Mood Score Predictor")

# Create two columns: left (content) and right (animation)
col1, col2 = st.columns([5, 2])  # 3:1 ratio, so animation is narrower

with col1:

    # st.write("Input your daily routine and get your mood😄.")   
    # st.write("Adjust the sliders below as per your daily routine and get your predicted mood score😄")
    st.markdown("Predict your mood score (0 to 10) based on your lifestyle habits.")

    sleep = st.slider("**😴 Sleep Hours**", 3.0, 10.0, 7.0, 0.5)
    screen = st.slider("**📱 Screen Time (hours)**", 2.0, 12.0, 6.0, 0.5)
    exercise = st.slider("**🏃 Exercise Minutes**", 0, 60, 20, 5)
    social = st.slider("**🗣️ Social Interaction Hours**", 0.0, 5.0, 2.0, 0.5)
    food = st.slider("**🍎 Food Quality (1 = Poor, 5 = Excellent)**", 1, 5, 3, 1)

    # --- Original Means and Stds from StandardScaler ---
    means = np.array([6.8967, 6.1033, 22.3333, 1.9483, 3.0667])
    stds = np.array([1.4827, 1.8142, 14.7079, 1.1504, 1.4817])

    # --- Raw input ---
    input_data = np.array([sleep, screen, exercise, social, food])

    # --- Standardize using training stats ---
    scaled_input = (input_data - means) / stds
    scaled_input = scaled_input.reshape(1, -1)

    # --- Prediction ---
    if st.button("🔮 Predict Mood Score"):
        prediction = model.predict(scaled_input)[0]
        st.success(f"🎯 Predicted Mood Score: **{round(prediction, 2)} / 10**")

        # Optional user feedback
        if prediction < 4:
            st.warning("😞 Low mood. Consider relaxing, exercising, or connecting with others.")
        elif prediction < 7:
            st.info("🙂 Moderate mood. Doing fine, keep balanced.")
        else:
            st.balloons()
            st.success("😄 Great mood! Keep up the good habits!")

with col2:
    # Display the animation
    st_lottie(lottie_ai, height=300, width=350,speed=1, loop=True, quality="high", key="right_side_lottie")
