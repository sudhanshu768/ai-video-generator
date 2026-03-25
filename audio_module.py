from gtts import gTTS


def generate_audio(text, filename="audio.mp3"):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(filename)
    return filename