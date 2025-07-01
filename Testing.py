import streamlit as st
import requests
import nltk
import re
import os
from dotenv import load_dotenv
from nltk.corpus import stopwords

# Load environment variables
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# --- Streamlit Page Config ---
st.set_page_config(page_title="🛡️ AI Security Chatbot", layout="centered")

# --- Gradient Background and Chat Styling ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(to bottom right, #4A90E2, #8E44AD, #7B1E3D);

    }
    .main {
        background: linear-gradient(to bottom, #f0f4ff, #fbeeff);
        padding: 2rem;
        border-radius: 12px;
        max-width: 800px;
        margin: auto;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    .chat-bubble-user {
        background-color: #d0ebff;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: #003366;
    }
    .chat-bubble-bot {
        background-color: #d4edda;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: #155724;
    }
    .title {
        text-align: center;
        color: #004085;
    }
    </style>
""", unsafe_allow_html=True)

# --- Main Title and Header ---
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🛡️ AI Security Chatbot")
st.write("Ask anything about **cybersecurity**, and I’ll respond with expert NLP-powered guidance.")

# --- Session History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- NLP Text Cleaning ---
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text

# --- Intent Classification ---
def classify_intent(text):
    keywords = {
        "phishing": ["phish", "scam", "fake email", "fraud"],
        "password": ["password", "login", "credentials", "passphrase"],
        "malware": ["virus", "malware", "ransomware", "trojan", "worm"],
        "network": ["network", "firewall", "wifi", "router", "ddos"],
    }
    for intent, kw_list in keywords.items():
        if any(kw in text for kw in kw_list):
            return intent
    return "general"

# --- System Prompt by Intent ---
def get_system_prompt(intent):
    prompts = {
        "phishing": "You are a cybersecurity expert specialized in phishing attacks.",
        "password": "You are a cybersecurity assistant skilled at password security and authentication.",
        "malware": "You are a malware analyst helping users understand and prevent virus threats.",
        "network": "You are a network security expert helping with firewall and Wi-Fi safety.",
        "general": "You are a general cybersecurity assistant.",
    }
    return prompts.get(intent, prompts["general"])

# --- Together API Call ---
def get_response_from_together(user_message):
    cleaned = clean_text(user_message)
    intent = classify_intent(cleaned)
    system_prompt = get_system_prompt(intent)

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 300,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        response = requests.post("https://api.together.xyz/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- User Input Section ---
user_input = st.text_input("You:", key="input", placeholder="e.g., How can I detect a phishing email?")

# --- Process User Input ---
if user_input:
    with st.spinner("Analyzing..."):
        bot_response = get_response_from_together(user_input)

    st.session_state.chat_history.append(("🧑", user_input))
    st.session_state.chat_history.append(("🤖", bot_response))

# --- Display Chat History with Bubbles ---
for sender, msg in st.session_state.chat_history:
    if sender == "🧑":
        st.markdown(f'<div class="chat-bubble-user"><strong>{sender}:</strong> {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-bot"><strong>{sender}:</strong> {msg}</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 12px;'>
    Made with ❤️ using Python, NLP & Streamlit UI
    </p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

