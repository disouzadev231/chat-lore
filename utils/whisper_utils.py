import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def transcribe_audio(audio_url):
    # Aqui, você pode baixar o áudio e enviar para Whisper
    audio_file = open(audio_url, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']
