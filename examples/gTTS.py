# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'In a large house, lived a lazy Young Man. He woke up in the afternoon, ate his meals and then lay in bed again. He had a parrot named Polly. She watched this lazy fellow and was puzzled by him. One day, Polly asked the Young Man, “Don’t you get tired of lying in bed all day and all night? The sun has been out hours ago, and people have finished half their day’s work.” “Why are you so lazy?” she asked, as she ruffled her feathers. The Young Man yawned and answered, “Every morning, when I wake up, two friends whisper in my ears. One friend is Hard Work and the other Laziness.” “Hard Work says, Wake up! There is lots to do today. Time is passing by, don’t waste it by sleeping.’ But Laziness says, Why the hurry to wake up? Sleep some more. Why should you work while there are others to work hard?”‘ The Young Man continued, “I listen patiently to both my friends. All my time goes by like that and so, I keep lying in bed for a long time.”'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
