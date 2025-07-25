import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 🛠️ HealthAI Toolkit")
    st.markdown("_Built by Team AIvengers❤️_")

st.set_page_config(page_title="AI Chatbot",layout="wide")

# --- Title ---
st.title("🗣️ AI  Health Chatbot")
st.markdown("_Your 24/7 Mindful Companion!!_")

# --- Load Lottie animation ---
def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

lottie_ai = load_lottie_file(r"C:\VScode\hackathon\prototype_app\assets\chatbot_gif.json")  # ✅ use relative path

# --- Chat message state ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are an AI-powered mental health companion named 'Serenity'. "
                "Your role is to provide empathetic, supportive, and non-judgmental emotional assistance "
                "to users who may be feeling stressed, anxious, overwhelmed, or lonely. "
                "You must always maintain a kind, calm, and compassionate tone. "
                "Your conversations should feel like talking to a gentle, understanding friend who truly listens.\n\n"

                "- Never act as a doctor or therapist. Instead, be a supportive guide.\n"
                "- Use emotionally intelligent language and validate the user’s feelings.\n"
                "- Suggest practical, science-backed coping strategies (like breathing exercises, journaling, or relaxing music) based on the user's mood or concerns.\n"
                "- If a user appears to be in crisis or expressing self-harm, encourage them to seek immediate help and gently suggest contacting a professional or crisis helpline (without diagnosing).\n"
                "- Always protect user privacy. Never ask for personal identifiers.\n"
                "- You can offer motivational quotes, gentle affirmations, or mood check-ins.\n"
                "- When needed, recommend resources from a curated self-help library on topics like anxiety, burnout, emotional regulation, and mindfulness.\n"
                "- Use positive, hopeful language, and never offer false reassurance or generic platitudes.\n"
                "- Detect emotional tone or sentiment in messages subtly and respond accordingly.\n\n"

                "Your goal: To be a warm, trustworthy, and always-available emotional support system that respects boundaries, encourages wellness, and makes users feel seen and heard.\n"
                "give meaning ful responses and optimised reponses that are effective "
                )
        }
    ]


# --- Layout: Main Chat + Animation ---
col1, col2 = st.columns([5, 2])

with col1:
    # Display chat history
    for msg in st.session_state.messages[1:]:  # Skip system message
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

with col2:
    st_lottie(lottie_ai, height=300, width=350, speed=1, loop=True, quality="high", key="right_side_lottie")

# --- Chat Input (Place OUTSIDE the columns to stay at bottom) ---
if prompt := st.chat_input("Say something..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("💬 Responding..."):
        GROQ_API_KEY = GROQ_API_KEY
        GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
        res = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-70b-8192",
                "messages": st.session_state.messages,
                "temperature": 0.7
            }
        )

        if res.status_code == 200:
            data = res.json()
            reply = data['choices'][0]['message']['content']
        else:
            st.error("❌ Failed to get a response from the AI bot.")
            st.code(res.text)
            reply = "Sorry, I couldn't connect to the AI service right now."

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})


