#text to speach 
#pip install gtts
from gtts import gTTS
def text_to_speach(text,lang="en"):
    speach=gTTS(text=text,lang=lang,slow=False)
    speach.save("Output.mp3")

from deep_translator import GoogleTranslator
def eng_to_tel(text):
    telugu_text = GoogleTranslator(
        source='en',
        target='te'
    ).translate(text)
    print("Telugu Text:", telugu_text)
    speech = gTTS(
        text=telugu_text,
        lang='te',
        slow=False
    )
    speech.save("telugu.mp3")

text = input("Enter text: ")
text_to_speach(text)
eng_to_tel(text)
