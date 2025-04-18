import os
from TTS.api import TTS
os.environ["TTS_PHONEMIZER_ESPEAK_PATH"] = "/usr/bin/espeak-ng"
FILE_PATH="/Users/ashwiniyadav/Downloads/EduGen/EduGen/DjangoFiles/Model/generated_audio/output.wav"
def generate_audio(script):
    tts = TTS(model_name="tts_models/en/ljspeech/vits").to("cuda")
    tts.tts_to_file(script, file_path=FILE_PATH)
    print("Audio Generated Successfully")