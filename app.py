import streamlit as st
from googletrans import Translator
import asyncio

# Function to translate text into a target language
async def translate_text(text, src_language, dest_language):
    """
    Translates the given text from source language to destination language.

    Parameters:
        text (str): The text to translate.
        src_language (str): The source language code.
        dest_language (str): The destination language code.

    Returns:
        str: Translated text.
    """
    translator = Translator()
    try:
        translated = await translator.translate(text, src=src_language, dest=dest_language)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

# Function to detect language
async def detect_language(text):
    """
    Detects the language of the given text.

    Parameters:
        text (str): The text to detect language for.

    Returns:
        str: Detected language code.
    """
    translator = Translator()
    try:
        detected = await translator.detect(text)
        return detected.lang
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
st.title("Language Translator")

# Language options
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Korean": "ko",
    "Japanese": "ja",
    "Chinese": "zh-cn",
    "Arabic": "ar",
   'afrikaans': 'af',
    "Hindi": "hi",
    'igbo': 'ig'
}

# Input fields
text_to_translate = st.text_area("Enter text to translate:", "Hello, how are you?")

# Language detection option
detect_language_checkbox = st.checkbox("Detect source language")

if detect_language_checkbox and text_to_translate.strip():
    detected_language_code = asyncio.run(detect_language(text_to_translate))
    detected_language_name = next((name for name, code in languages.items() if code == detected_language_code), detected_language_code)
    st.write(f"Detected Source Language: {detected_language_name}")
    src_language = detected_language_name
else:
    src_language = st.selectbox("Select source language:", options=list(languages.keys()), index=0, key="src")

dest_language = st.selectbox("Select destination language:", options=list(languages.keys()), index=1, key="dest")

# Translation
if st.button("Translate"):
    src_code = languages.get(src_language, src_language)  
    dest_code = languages[dest_language]

    translated_text = asyncio.run(translate_text(text_to_translate, src_code, dest_code))
    st.session_state.translated_text = translated_text
    st.session_state.src_code = src_code
    st.session_state.dest_code = dest_code
    
    st.write(f"**Translated Text:** {translated_text}")

# Reverse Translation
if st.button("Reverse Translate"):
    if 'translated_text' in st.session_state and 'src_code' in st.session_state and 'dest_code' in st.session_state:
        translated_text = st.session_state.translated_text
        src_code = st.session_state.src_code
        dest_code = st.session_state.dest_code
        reversed_text = asyncio.run(translate_text(translated_text, dest_code, src_code))
        st.write(f"**Reversed Translation:** {reversed_text}")
    else:
        st.write("Please translate the text first.")
