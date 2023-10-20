from gtts import gTTS
import json
import os

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    else:
        print(f"Directory '{directory_path}' already exists.")

def generate_audio(input_text, audio_filename, project_name):
    language = 'en'
    myobj = gTTS(text=input_text, lang=language, slow=False)
    myobj.save(f"./audios/{project_name}/{audio_filename}.mp3")
