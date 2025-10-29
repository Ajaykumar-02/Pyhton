import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="7ced2ce6e4a44d31aee53e420f8684f2"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommannd(c):
    if "open google"in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook"in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link) 

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    speak("Here are the latest headlines:")
                    for article in articles[:5]:  # Read top 5 headlines
                        speak(article['title'])
                else:
                    speak("No news articles found.")
            else:
                speak(f"Failed to fetch news. Status code: {r.status_code}")
        except Exception as e:
            speak("Sorry, I couldn't fetch the news.")
            print("News API Error:", e)
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()        


    else:
        speak("I didn't understand the command.")

      

   

if __name__ == "__main__":
    speak(" Initializing Jarivis....")
    while True:
       
        r=sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone()as source:
                print("listening...")
                audio=r.listen(source ,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)  
            if(word.lower() == "jarvis"):
                speak("Yes") 
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio=r.listen(source)
                    command = r.recognize_google(audio) 

                    processCommannd(command)
               



        except Exception as e:
            print("Error ;{0}".format(e))  
               
