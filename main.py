import speech_recognition as sr
import keyboardd
import os
from changeWindow import top_wind, getWindow
import sys
sys.path.insert(0,"C:\\VScode\\voice_helper\\env\\Lib\\site-packages\\sound")
from sound import Sound
from test import code
import pyaudio
import string
import datetime
import pyttsx3

name = "ника"
anglMonth = {
        "January":"январь",
        "February" : "февраль",	
        "March": "март",
        "April" :"апрель", 
        "May" :"май",
        "June" :"июнь", 
        "July" :"июль", 
        "August": "август", 
        "September": "сентябрь", 
        "October" :"октябрь",
        "November" :"ноябрь", 
        "December" :"декабрь" 
    }
# rasp = sr.Recognizer()# объект распознования речи
# mic = sr.Microphone()#объект работы с микрофоном
engine = pyttsx3.init()
son = False
key = ""
volum = 50
block = False
def dataChanger(date:str):
    date = date.replace(date.split(" ")[0],anglMonth[date.split(" ")[0]])
    return date
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def obr(message:str):
    global son, volum
    global engine
    global key, block
    # Распознаем речь
    # text = rasp.recognize_google(audio, language="ru")  # Используем Google Speech Recognition API для распознавания речи на русском языке
    
    if "доступ" in message.casefold():
        if str(key) in message.casefold():
            block = False
            engine.say("добро пожаловать")
            engine.runAndWait()
            return
    elif block == True:
        engine.say("код доступа")
        engine.runAndWait()
        return
    
    elif "вставай" in message.casefold() or name in message.casefold():
        engine.say("слушаю")
        engine.runAndWait()
        son = False
        return
    elif "спи" in message.casefold():
        print(son)
        son = True
        return
    elif son == False and block == False:
        # print("Распознанный текст:", message)
        if "выключи" in message.casefold():
            engine.say("до связи")
            engine.runAndWait()
            raise SystemExit
        elif "блок" in message.casefold():
            print(block)
            key = code()
            block = True
            print(block)
            return
        elif "без звука" in message.casefold():
            Sound.volume_set(0)
            return
        elif "звук" in message.casefold():
            Sound.volume_set(volum)
            return
        elif "тише" in message.casefold():
            volum -= 10
            Sound.volume_set(volum)
            return
        elif "громче" in message.casefold():
            volum +=10
            Sound.volume_set(volum)
            return
        elif "динамик" in message.casefold():
            os.system("C:\\Users\\kymsk\\nircmd\\nircmd.exe setdefaultsounddevice \"1 - C27JG5x\"")
            engine.say("переключила")
            engine.runAndWait()
            return
        elif "пауза" in message.casefold(): 
            print(message)
            if "брауз" in message.casefold():
                code = getWindow("Google")
                print(1)
                if len(str(code)) > 12:
                    print(2)
                    engine.say(code)
                    engine.runAndWait()   
                    return
                else:
                    print(3)
                    t = top_wind(int(code))
                    if t == 1:
                        print(4) 
                        keyboardd.press('space')
                        return
            elif len(message.casefold()) <6:
                keyboardd.press('space')
                return
            return
        elif "наушник" in message.casefold():
            os.system("C:\\Users\\kymsk\\nircmd\\nircmd.exe setdefaultsounddevice \"Динамики\"")
            engine.say("переключила")
            engine.runAndWait()
            return
        elif "врем" in message.casefold():
            now = datetime.datetime.now().strftime("%H:%M")
            engine.say(f"Текущее время, {now}")
            engine.runAndWait()
            return
        elif "дата" in message.casefold() or "число" in message.casefold():
            data = datetime.date.today().strftime("%B %d, %Y")
            engine.say(dataChanger(data))
            engine.runAndWait()
            return
        return
# def recognize_speech_and_add_to_word():
#     with mic as source:
#         print("Скажите что-нибудь:")
#         audio = rasp.listen(source)  # Слушаем аудио с микрофона

    # try:
        
    #         elif "сколько будет" in text.casefold():
    #             line:str  = text.split(" ")
    #             for lit in line:
    #                 if is_number(lit):
    #                     i = line.index(lit)
    #                     try:
    #                         rez = eval(line[i]+ line[i+1].replace('х','*')+line[i+2])
    #                     except Exception:
    #                         rez = "не удалось преобразовать"
    #                     print(rez)
    #                     engine.say(str(rez))
    #                     engine.runAndWait()
    #                     break
    # except sr.UnknownValueError:
    #     print("Не удалось распознать речь.")
    # except sr.RequestError as e:
    #     print("Ошибка при обращении к сервису распознавания речи; {0}".format(e))
    
    # recognize_speech_and_add_to_word()
    
# Запускаем распознавание речи

# recognize_speech_and_add_to_word()