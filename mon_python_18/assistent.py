import pyttsx3

tts = pyttsx3.init()

def sayBots(text):
    tts.say(text)
    print(text)
    tts.runAndWait()

while True:
    text = input('Введите текст: ')

    if text.lower() == 'привет':
        sayBots('привет')
    
    elif text.lower() == 'как дела?':
        sayBots('норм')
    
        
    else:
        sayBots('Я тебя не понимаю')
