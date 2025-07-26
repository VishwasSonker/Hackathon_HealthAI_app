import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Load your dataset ---
df = pd.read_csv(r"assets/mood_data.csv")  # Replace with your actual file name

# --- Columns for dropdowns ---
columns_with_mood = df.columns.tolist()                 # includes Mood_Score
columns_without_mood = [col for col in df.columns if col != 'Mood_Score']

# --- Streamlit page config ---
st.set_page_config(page_title="Data Insights", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 🛠️ HealthAI Toolkit")
    st.markdown("_Built by Team AIvengers ❤️_")

# --- Title ---
st.markdown("<h1 style='text-align: center;'>📊 Data Insights</h1>", unsafe_allow_html=True)

# --- Two-column layout ---
col1, col2 = st.columns(2)

# --- Column 1: Histogram + summary ---
with col1:
    st.markdown("### 📌 Your Activity of Last 1 Month")
    feature1 = st.selectbox("Select a feature:", columns_with_mood, key="activity")

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.histplot(df[feature1], kde=True, color="mediumpurple", ax=ax1)
    ax1.set_xlabel(feature1)
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    # Summary for the left graph
    st.markdown("""
    **🔍 Summary:**  
    This graph shows the distribution of your selected feature over the last month.  
    Peaks in the histogram indicate the most frequent values, helping you recognize patterns, consistency, or irregularities in your tracked data.
    """)

# --- Column 2: Lineplot with Mood Score + summary ---
with col2:
    st.markdown("### 📈 Your Mood According To Your Activity")
    feature2 = st.selectbox("Select a feature (X-axis):", columns_without_mood, key="mood")

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.lineplot(x=df[feature2], y=df['Mood_Score'], marker="o", ax=ax2)
    ax2.set_xlabel(feature2)
    ax2.set_ylabel("Mood Score")
    st.pyplot(fig2)

    # Summary for the right graph
    st.markdown("""
    **🧠 Insight:**  
    This plot shows how your mood score varies with the selected activity.  
    You can analyze trends to identify which habits are positively or negatively impacting your mood.
    """)

# --- Area plot: Mood_Score vs 1 to 30 ---

st.markdown("---")  # separator line

st.markdown("### 📈 Mood Score Trend (Days 1–30)")

st.markdown("#### 🗓️ Your Mood Score For The Last 30 Days --->")

# Prepare data
count = np.arange(1, 31)
mood_subset = df["Mood_Score"].head(30)

# Create smaller area plot
fig, ax = plt.subplots(figsize=(8, 3))  # reduced size from (10, 4) to (8, 3)
ax.fill_between(count, mood_subset, color="skyblue", alpha=0.5)
ax.plot(count, mood_subset, color="steelblue", linewidth=2)
ax.set_xlabel("Days")
ax.set_ylabel("Mood Score")


st.pyplot(fig)
st.markdown(
    """
    <p style='text-align: center; font-size: 20px; color: black;'>
    This area plot illustrates how the mood score fluctuates over a period of 30 days. 
    Each point on the graph represents the user's recorded mood score for a given day. 
    The shaded region helps visualize the overall trend and intensity of mood variations. 
    This can be useful for identifying emotional patterns, detecting stress periods, 
    or evaluating the impact of lifestyle changes over time.
    </p>
    """,
    unsafe_allow_html=True
)
