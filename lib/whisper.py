import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe_audio_small(audio_file, model="whisper-1"):
    """Transcribe an audio file to text."""
    response = openai.Audio.transcribe(model, audio_file)
    return response["text"]
