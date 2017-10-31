from gtts import gTTS

def main():
    intro = "Welcome to Vocal Focals."
    audio_output = gTTS(text=intro, lang='en', slow=False)
    audio_output_file = 'vocal_focals_intro.mp3'
    audio_output.save(audio_output_file)
    print(intro)
    os.system("mpg321 " + audio_output_file)

if __name__ == '__main__':

    main()
