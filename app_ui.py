import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Multilingual Voice Cloning", layout="wide")
st.title("🌍 Multilingual Voice Cloning + TTS")

mode = st.radio("Choose mode:", ["Text to Speech", "Voice Cloning"])

if mode == "Text to Speech":
    text = st.text_area("Enter text in any language:")
    lang = st.selectbox("Select language:", ["auto", "en", "fr-fr", "pt-br"])

    if st.button("Generate Speech"):
        with st.spinner("Generating..."):
            response = requests.post(f"{API_URL}/tts/", data={"text": text, "language": lang})
            if response.status_code == 200:
                st.audio(response.content, format="audio/wav")
            else:
                st.error("Error generating speech.")

else:
    text = st.text_area("Enter text:")
    uploaded_file = st.file_uploader("Upload a voice sample (.wav)", type=["wav"])
    lang = st.selectbox("Select language:", ["auto", "en", "fr-fr", "pt-br"])

    if uploaded_file and st.button("Clone Voice"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        data = {"text": text, "language": lang}
        with st.spinner("Cloning voice..."):
            response = requests.post(f"{API_URL}/clone/", data=data, files=files)
            if response.status_code == 200:
                st.audio(response.content, format="audio/wav")
            else:
                st.error("Error cloning voice.")
