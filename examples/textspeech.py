import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    # to get the info. about various voices in our PC
    print("Voice:")
    print("ID: %s" % voice.id)
    #print("Name: %s" % voice.name)
    #print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    #print("Languages Known: %s" % voice.languages)

voice_id ='malayalam'
#engine.setProperty('voice', voice_id)
engine.setProperty('rate',150)
#engine.say("Once, three Crows and two Sparrows lived in a forest. They all were good friends. They would meet every day and fly around together from one place to another. The Crows would constantly look for food and the Sparrows for a place to make their nests.One day, the Crows said, “Let’s explore this part of the forest.  Someone told us there is lots of food here.The new part of the forest was beautiful and there was, indeed, plenty of food. However, there was only one large tree. The Sparrows and the Crows wanted to live there.The Sparrows told their aunts, uncles, cousins, grandparents and friends about the new place. Everyone wanted to live there. The Crows also did the same.Soon, a big fight broke out among the birds. The Crows said, ‘We found the place first, so we will live on the tree.”The Sparrows said, “So what? We will live there. We found the tree first.”After this, the two Sparrows and three Crows also could not be friends.They constantly fought with each, “You Crows are bad.”“You Sparrows are fools!”Thus, they went back to their own kind.")

engine.say("Text to speech convertor")
engine.runAndWait()

