import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Created by Ajay")
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")

        if x.lower() == 'q':
            print("Goodbye!")
            break

        engine.say(x)
        engine.runAndWait()

