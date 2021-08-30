import speech_recognition as sr
import pyttsx3
import webbrowser

ig_username = 'oksfdrv'


class PersonalBot:
  def Listen(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print('Listening for orders..')
      r.pause_threshold = 0.7
      audio = r.listen(source)

      try:
        print("Recognizing orders..")
        Query = r.recognize_google(audio,language='in-en')
      
      except Exception as e:
        print(e)
        print("Can you please say your orders again?")
        return "None"

    return Query

  def Speak(self, audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
  jarvis = PersonalBot()
  
  jarvis.Speak('Hello Oksa')
  jarvis.Speak('this is your bithday ?')
  jarvis.Speak('this is my wish for you, i hope you still healthy, still safe, obey parents, mature physically and spiritually')
  jarvis.Speak('I know Im annoying sometimes, but its me')
  jarvis.Speak('if you wanna play birthday song, say lagu')
  jarvis.Speak('if you wanna open instagram, say instagram')
  jarvis.Speak('if you wanna information, say informasi')
  jarvis.Speak('if you wanna stop this, say thank you')
  while True:
    result = jarvis.Listen()
    print("Your order is", result)
      
    if 'informasi' in result.lower():
      webbrowser.open("https://www.facebook.com/photo.php?fbid=106775179775720&set=pb.100013297145563.-2207520000..&type=3")
      jarvis.Speak('Name : Maria Oksana fedorova')
      jarvis.Speak('Age : 19')
      jarvis.Speak('Gender : Female')
      jarvis.Speak('birthday : Today')
    
    if 'lagu' in result.lower():
      jarvis.Speak('opening birthday song')
      webbrowser.open("https://www.youtube.com/watch?v=se5S1r2lpWY")
  
    if 'thank you' in result.lower(): 
      jarvis.Speak('no problem')
      break

    if 'instagram' in result.lower():
     jarvis.Speak('Opening your instagram')
     insta_link = "http://instagram.com/{}".format(ig_username)
     webbrowser.open(insta_link,new=1)

    if 'cake' in result.lower():
     jarvis.Speak('Happy Birtday')
     from main import *
