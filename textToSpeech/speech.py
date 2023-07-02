from gtts import gTTS

import os

text = open('speech.txt').read()

language = 'en'

output = gTTS(text=text, lang=language, slow=False)

output.save('speech.mp3')

os.system('start speech.mp3')
