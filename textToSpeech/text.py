
from gtts import gTTS
import os

text = "Hey, I am Google Text to speech"

# gtts return back a audio

output = gTTS(text=text, lang='en', slow=False)

output.save('output.mp3')

#  starting mp3 file
#  for windos - start
# for mac - afplay
os.system('start output.mp3')
