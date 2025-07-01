# 🛡️ AI Security Chatbot using NLP and LLM API

This project is an **AI-powered cybersecurity assistant chatbot** that intelligently answers security-related questions using **Natural Language Processing (NLP)** and a **Large Language Model (LLM)** via the [Together AI](https://www.together.xyz/) API.

It also features **basic NLP classification**, a dynamic **Streamlit web interface**, and interactive conversations stored in real-time.

## 🚀 Features

* 🔐 Ask cybersecurity questions (e.g., phishing, malware, password safety, firewalls).
* 🤖 Responses are generated using LLM (Mixtral-8x7B from Together AI).
* 🧠 Basic NLP preprocessing (stopword removal, intent classification).
* 🎨 Beautiful responsive UI with linear gradient background.
* 💬 Maintains chat history during session.


## 🧰 Tech Stack

* [Python 3.11+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [NLTK](https://www.nltk.org/)
* [Together AI API](https://api.together.xyz/)
* \[HTML/CSS]\(for UI design styling)

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Bollyb/ai-security-chatbot.git
cd ai-security-chatbot
```

2. **Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set your Together AI API Key:**

Create a `.env` file in the root folder and paste your API key:

```
TOGETHER_API_KEY=your_api_key_here
```

> 🔑 You can get your API key from [Together AI Dashboard](https://platform.together.xyz/).

5. **Run the Streamlit App:**

```bash
streamlit run app.py
```

## 📁 File Structure

```
├── app.py               # Main Streamlit app
├── .env                 # Contains your API key
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🧠 NLP & Intent Classification

This chatbot uses basic NLP (with NLTK) to:

* Clean and preprocess text
* Classify questions into cybersecurity domains like:

  * `phishing`
  * `malware`
  * `password security`
  * `network security`

These intents help customize the system prompt sent to the LLM.

## 🌈 UI Design

* Linear gradient background: **Blue → Purple → Wine**
* Color-coded chat bubbles
* Responsive layout with custom HTML & CSS

## 🙋‍♂️ Example Questions You Can Ask

* *How can I protect myself from phishing?*
* *What is a strong password policy?*
* *Explain ransomware.*
* *Is public Wi-Fi safe to use?*

## 🤝 Contribution

Feel free to fork this repo, open issues or submit PRs to improve functionality or design.

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.
