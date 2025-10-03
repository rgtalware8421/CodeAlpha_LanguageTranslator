import streamlit as st
from googletrans import Translator

st.title("🌍 Language Translator Tool - CodeAlpha")

translator = Translator()

text = st.text_area("Enter text to translate:")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source = st.selectbox("Select source language:", list(languages.keys()))
target = st.selectbox("Select target language:", list(languages.keys()))

if st.button("Translate"):
    if text:
        result = translator.translate(text, src=languages[source], dest=languages[target])
        st.success(result.text)
    else:
        st.warning("⚠️ Please enter text.")

