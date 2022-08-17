    
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)  



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good Evening")

    speak("I am Jarvais sir. Please tell me how may i help you")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        

        print("say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    while 1:
      query =  takeCommand().lower()

      if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
      
      elif ' youtube' in query:
        webbrowser.open("youtube.com")
      elif ' google' in query:
        webbrowser.open("google.com")
      elif ' instagram' in query:
        webbrowser.open("instagram.com")
      elif ' google classroom' in query:
        webbrowser.open("google classroom.com")
      elif ' time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strtime}")
      elif 'spotify' in query:
        webbrowser.open("spotify.com")
      elif 'the temperature' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strtime}")



