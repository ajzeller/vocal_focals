from gtts import gTTS

audio = "Scene captured... please wait."
audio_output = gTTS(text=audio, lang='en', slow=False)
audio_output_file = 'vocal_focals_capturing_scene.mp3'
audio_output.save(audio_output_file)
print(audio)
os.system("mpg321 " + audio_output_file)
