import streamlit as st
import pandas as pd

with st.sidebar:
    st.markdown("## 🛠️ HealthAI Toolkit")
    st.markdown("_Built by Team AIvengers❤️_")


st.set_page_config(page_title="About", layout="centered")

st.title("✨ Behind the Scenes")
st.markdown("*Meet the minds 🧠 and tools 🛠️ powering our hackathon project.*")

# 🔹 Hackathon Name
st.subheader("🏁 Hackathon")
st.markdown("**Hackathon Name:** *VIBE CODING🔥*")  # <-- Change name if needed

col1, col2 = st.columns([2, 2])

with col1:
    # 🔹 Team Info Table
    st.subheader("👥 Team AIvengers")

    team_df = pd.DataFrame({
        "**Name**": ["Tarun Asati", "Vishwas Sonker"],
        "**Branch**": ["AI & DS", "AI & DS"],
        "**Year**": ["3rd Year", "3rd Year"]
        })
    team_df.index = team_df.index + 1
    st.table(team_df)
    


with col2:
# 🔹 Tech Stack Table
    st.subheader("🕸️ Tech Stack Used")

    tech_stack = pd.DataFrame({
        "**Component**": ["Framework", "Language", "ML Library", "Data Handling", "Visualization", "Animation", "LLM model"],
        "**Technology**": ["Streamlit", "Python", "Scikit-learn", "Pandas, NumPy", "Matplotlib, Seaborn", "LottieFiles", "Llama3-70b-8192"]
    })
    tech_stack.index=tech_stack.index+1
    st.table(tech_stack)

# 🔹 Resources / Links
st.subheader("🔗 Project Resources")

st.markdown("""
- [🔢 Dataset](https://drive.google.com/file/d/1vbNlRGGN8SHTm17DmdMmpA-QjJvEh9jH/view?usp=sharing)  
- [📁 GitHub Repository](https://github.com/Tarun-asati21/Vibecode_hackathon_app)  
""")
