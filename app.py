import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download("punkt")
nltk.download("punkt_tab")

st.set_page_config(page_title="Email Spam Detector", page_icon="📩", layout="centered")

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if w.isalnum()]
    tokens = [w for w in tokens if w not in stop_words]
    tokens = [ps.stem(w) for w in tokens]
    return " ".join(tokens)

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ff5f6d 0%, #ffc371 100%);
}
.main-card {
    background: rgba(255, 255, 255, 0.22);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 26px;
    padding: 28px;
    box-shadow: 0px 10px 35px rgba(0,0,0,0.18);
    border: 1px solid rgba(255,255,255,0.35);
    margin-top: 25px;
}
h1 {
    text-align: center;
    color: white;
    font-weight: 800;
    letter-spacing: 0.5px;
}
.subtitle {
    text-align: center;
    color: rgba(255,255,255,0.92);
    font-size: 16px;
    margin-top: -10px;
    margin-bottom: 25px;
}
.stTextArea textarea {
    background: rgba(255,255,255,0.90) !important;
    border-radius: 18px !important;
    font-size: 16px !important;
    padding: 16px !important;
    border: 1px solid rgba(255,255,255,0.55) !important;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.12) !important;
}
.stButton > button {
    background: #ffe600 !important;
    color: #111 !important;
    border: none !important;
    border-radius: 999px !important;
    padding: 12px 22px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    box-shadow: 0px 8px 18px rgba(0,0,0,0.20) !important;
    transition: 0.2s ease-in-out;
}
.stButton > button:hover {
    background: #ffffff !important;
    transform: translateY(-1px);
}
.helper {
    text-align: center;
    color: rgba(255,255,255,0.90);
    font-size: 13px;
    margin-top: -6px;
}
.result-box {
    margin-top: 22px;
    padding: 18px 18px;
    border-radius: 22px;
    text-align: center;
    font-size: 22px;
    font-weight: 800;
    background: rgba(255,255,255,0.96);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.14);
    border: 1px solid rgba(255,255,255,0.5);
}
.pill {
    display: inline-block;
    margin-top: 10px;
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
    background: rgba(0,0,0,0.08);
}
.footer {
    text-align: center;
    margin-top: 26px;
    color: rgba(255,255,255,0.95);
    font-size: 14px;
}
.footer a {
    color: #fff;
    font-weight: 800;
    text-decoration: none;
}
.footer a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Email Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Paste your email/SMS content below to check if it is spam 🚫</div>", unsafe_allow_html=True)

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

user_input = st.text_area("", height=200, placeholder="Type or paste message here...")

char_count = len(user_input)
st.markdown(f"<div class='helper'>{char_count}/4000 characters</div>", unsafe_allow_html=True)

run = st.button("Run Spam Test")

if run:
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    elif len(user_input) > 4000:
        st.warning("Text too long. Please keep it under 4000 characters.")
    else:
        with st.spinner("Analyzing message..."):
            pred = model.predict([user_input])[0]
            try:
                proba = model.predict_proba([user_input])[0]
                spam_prob = float(proba[1])
                ham_prob = float(proba[0])
                confidence_text = f"Spam Probability: {spam_prob*100:.2f}% | Ham Probability: {ham_prob*100:.2f}%"
            except:
                confidence_text = "Confidence not available for this model."

        if pred == 1:
            label = "🚫 SPAM"
            color = "#ff3b3b"
        else:
            label = "✅ NOT SPAM"
            color = "#23b26d"

        st.markdown(
            f"<div class='result-box' style='color:{color};'>{label}<div class='pill'>{confidence_text}</div></div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
    <a href="https://github.com/wigjatin/spam-detector-large-scale" target="_blank">View this project on GitHub</a>
</div>
""", unsafe_allow_html=True)
