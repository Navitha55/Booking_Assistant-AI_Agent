import streamlit as st
import requests

st.set_page_config(page_title="AI Booking Assistant")

st.title("📅 Book Your Appointment with AI Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.chat_input("Say something like 'Schedule a call tomorrow at 3 PM'")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    try:
        response = requests.post("http://localhost:8000/chat", json={"message": user_input})
        bot_reply = response.json().get("response", "Something went wrong.")
    except Exception as e:
        bot_reply = f"⚠️ Backend error: {e}"

    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
