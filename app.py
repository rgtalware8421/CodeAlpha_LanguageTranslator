import streamlit as st
from deep_translator import GoogleTranslator

# Title
st.title("🌍 Language Translator Tool - CodeAlpha")

# Text input
text = st.text_area("Enter text to translate:")

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# Dropdowns for source and target
source = st.selectbox("Select source language:", list(languages.keys()))
target = st.selectbox("Select target language:", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text:
        # Use deep_translator instead of googletrans
        result = GoogleTranslator(source=languages[source], target=languages[target]).translate(text)
        st.success(f"**Translated Text:** {result}")
    else:
        # Correct syntax for warning message (Fix for SyntaxError)
        st.warning("⚠️ Please enter some text to translate.")
