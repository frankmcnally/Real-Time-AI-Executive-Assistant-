import requests
import os
from ..config import ELEVEN_API_KEY, ELEVEN_VOICE_ID

def speak(text):
    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_VOICE_ID}",
        headers={"xi-api-key": ELEVEN_API_KEY},
        json={"text": text, "voice_settings": {"stability": 0.4, "similarity_boost": 0.8}}
    )
    with open("temp.mp3", "wb") as f:
        f.write(response.content)
    os.system("afplay temp.mp3")  # Use `mpg123` or `vlc` on Windows/Linux
