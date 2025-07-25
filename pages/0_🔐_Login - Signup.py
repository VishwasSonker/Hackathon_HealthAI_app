import streamlit as st

with st.sidebar:
    st.markdown("## 🛠️ HealthAI Toolkit")
    st.markdown("_Built by Team AIvengers❤️_")


st.set_page_config(page_title="Login Signup",layout="centered")
st.title("🔐 Login / Signup")

tab1, tab2 = st.tabs(["🔑 Login", "🆕 Signup"])

with tab1:
    st.subheader("Welcome Back!")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Login"):
        if username and password:
            st.success("✅ You have successfully logged in!")
            st.markdown("---")
            st.info("⚠️ This is a demo login system for UI purposes only. No actual authentication is performed.")
        else:
            st.error("❌ Invalid credentials. Please enter both username and password.")

with tab2:
    st.subheader("Create New Account")
    new_username = st.text_input("New Username", key="signup_user")
    new_password = st.text_input("New Password", type="password", key="signup_pass")
    
    if st.button("Sign Up"):
        if new_username and new_password:
            st.success("✅ Your account has been successfully created!")
            st.markdown("---")
            st.info("⚠️ This is a demo login system for UI purposes only. No actual authentication is performed.")           
        else:
            st.error("❌ Please fill out both fields to create an account.")




