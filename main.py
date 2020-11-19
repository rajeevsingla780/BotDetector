from gtts import gTTS 
from playsound import playsound
import os
def fun(t):
    mytext = str(t)
  
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False) 

    myobj.save("welcome.mp3") 

    playsound("welcome.mp3")
    os.remove('welcome.mp3')
 
