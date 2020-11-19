from gtts import gTTS 
import os
def fun(t):
    mytext = str(t)
  
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False) 
    
    myobj.save(os.path.join("welcome.mp3")) 

    os.system(os.path.join("welcome.mp3"))
    os.remove(os.path.join("welcome.mp3"))
 
