from dotenv import load_dotenv
# load the Key in .env. When you want to use ChatGPT to test chat modul, you can set your OpenAI_Key in .env
success = load_dotenv()
if not success:
    print("Failed to load .env file")

from .core.load_scene import load_scene
from .core.activate_livelink import activate_livelink
from .core.chat import chat
from .core.fetch_tts import fetch_tts
from .core.audio_to_array import audio_to_array
from .core.send_audio import send_audio
from .core.speechtotext import speechToText 
from .core.user_selection import *

# load A2F Instance
load_scene()
# Activate the live link of Audio2Face with Metahuman character in Unreal Engine
activate_livelink()

# User selection for doctor voice and the language
voice = doctor_selection()
lang = language_selection()

while(True):
    # Audio from Microfon as User Input will be converted to Text
    user = speechToText()
    #user = input("Enter text: ")
    if user:
        #assistant = chat(user)
        response_data = fetch_tts(user, VOICE=voice)
        wavarr, sample_rate = audio_to_array(response_data)
        send_audio(wavarr, sample_rate)
    continue