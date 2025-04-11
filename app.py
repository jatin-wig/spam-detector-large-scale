import streamlit as st
import joblib
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Fix: Only download if not already available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #FF6F61, #D65D5D);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
}
.stApp {
    background: linear-gradient(135deg, #FF6F61, #D65D5D);
}
h2.title {
    color: #FFFFFF;
    text-align: center;
    font-size: 3rem;
    font-weight: 600;
    margin-top: 30px;
}
.subtitle {
    text-align: center;
    color: #fefefe;
    font-size: 1.2rem;
    margin-top: 5px;
    margin-bottom: 40px;
}

.stTextArea textarea {
    background-color: #ffffff !important;
    color: #333;
    font-size: 16px;
    border-radius: 20px !important;
    padding: 18px;
    width: 100%;
    border: 1px solid #ccc;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
}

.stButton > button {
    background-color: yellow;
    color: black;
    border: none;
    border-radius: 50px;
    font-size: 18px;
    font-weight: 600;
    padding: 12px 24px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    cursor: pointer;
}
.stButton > button:hover {
    background-color: white;
}

.result-box {
    margin-top: 40px;
    padding: 30px;
    border-radius: 30px;
    display: inline-block;
    text-align: center;
    font-size: 1.5rem;
    font-weight: bold;
    background-color: #ffffff;
    width: 50%;
    max-width: 500px;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: white;
    font-size: 1rem;
}
.footer a {
    color: #ffcc00;
    text-decoration: none;
    font-weight: 600;
}
.footer a:hover {
    text-decoration: underline;
}

.char-counter {
    text-align: center;
    color: #ffffff;
    font-size: 14px;
    margin-top: -10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='title'>📧 Email Spam Detector</h2>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Paste your email content below to check if it's spam!</p>", unsafe_allow_html=True)

user_input = st.text_area("", height=250, placeholder="Paste your email text here...")

char_count = len(user_input)
st.markdown(f"<div class='char-counter'>{char_count}/4000 characters</div>", unsafe_allow_html=True)

if st.button("Run Spam Test"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        cleaned = preprocess_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        result_text = "Spam" if prediction == 1 else "Not Spam"
        color = "#FF4D4D" if prediction == 1 else "#28A745"

        st.markdown(
            f"<div class='result-box' style='color:{color};'>{result_text}</div>",
            unsafe_allow_html=True
        )

st.markdown("""
<div class='footer'>
    <a href="https://github.com/wigjatin/spam-detector-large-scale" target="_blank">🔗 View this project on GitHub</a>
</div>
""", unsafe_allow_html=True)
