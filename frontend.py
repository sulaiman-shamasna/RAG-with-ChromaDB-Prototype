import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Ollama RAG Chatbot", page_icon="💬")

st.title("💬 Ollama RAG Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def send_message():
    user_input = st.session_state["user_input"].strip()
    if user_input:
        st.session_state['messages'].append({"role": "user", "content": user_input})

        try:
            response = requests.post(API_URL, json={"query": user_input})
            if response.status_code == 200:
                bot_response = response.json().get("response", "No response from bot.")
            else:
                bot_response = f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            bot_response = f"Error: {e}"

        st.session_state['messages'].append({"role": "bot", "content": bot_response})

        st.session_state["user_input"] = ""

for msg in st.session_state['messages']:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Chatbot:** {msg['content']}")

st.text_input("You:", key="user_input", on_change=send_message)
