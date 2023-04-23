import streamlit as st

from lib.openai_text import get_completion
from lib.whisper import transcribe_audio_small
from dotenv import load_dotenv

load_dotenv()

st.session_state.transcribed_text = ""
st.session_state.ai_response = ""


@st.cache_data
def get_transcription(audio) -> str:
    return transcribe_audio_small(audio)


st.title("Transcribler")

"""
Welcome to Transcribler, a tool to transcribe audio files to text and then query that text with AI.
"""

st.subheader("Step 1. Upload an audio file")
source_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

st.subheader("Step 2. Transcribe the audio file")

if source_audio is not None:

    if source_audio.size < 25_000_000:  # 25MB
        st.success("Audio file uploaded successfully")
        st.audio(source_audio)
        transcribe_button = st.button("Transcribe")

        if transcribe_button:
            st.session_state.transcribed_text = get_transcription(source_audio)
            st.success("Audio file transcribed successfully")
    else:
        st.error("File size too large. Please upload a file less than 10MB.")

if st.session_state.transcribed_text:
    with st.expander("Transcribed text"):
        st.write(st.session_state.transcribed_text)

st.subheader("Step 3. Query the text")


def get_ai_response():
    st.session_state.ai_response = get_completion(st.session_state.query, st.session_state.transcribed_text)
    print(st.session_state.ai_response)
    st.success(st.session_state.ai_response)


st.text_input("Enter a query", on_change=get_ai_response, key="query")
