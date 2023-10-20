from gtts import gTTS
import os
from playsound import playsound
import json
from text_json import TextJson
from utils import create_directory, generate_audio

PROJECT_NAME = 'project_name'
TEXTS = 'texts'

filepath = "./texts/c-pointers.json"
json_text_manager = TextJson(filepath)
json_data = json_text_manager.read_json()

new_audio_dir = f"./audios/{json_data[PROJECT_NAME]}"
texts = json_data[TEXTS]
create_directory(new_audio_dir)
for i in range (len(texts)):
    text = texts[i]
    if text != "":
        generate_audio(texts[i], str(i+1), json_data[PROJECT_NAME])

# # The text that you want to convert to audio
# mytext = 'Hello everyone, welcome to my channel. In this video, we are going to talk about multi dimensional arrays in c language.'

# # Language in which you want to convert
# language = 'en'

# audio_filename = "welcome.mp3"

# myobj = gTTS(text=mytext, lang=language, slow=False)
# myobj.save(audio_filename)
# playsound(audio_filename)

