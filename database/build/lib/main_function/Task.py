import datetime
import wikipedia
from main_function import Say, Say_in_arabic
from essential_function import tokenize, dirlocation
from features_function import search_on_google
import subprocess
import os
from keyboard import press_and_release
from features_function import website



# function

# 2 Type

# 1 - Non input
# eg: Time, Date, Speedtest

def Time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    Say("It's " + time)

def Date():
    date = datetime.date.today()
    day = datetime.datetime.now().strftime("%A")
    Say(f"{date} and this is {day}")

def Salam():
    Say_in_arabic("ٱلسَّلَامُ عَلَيْكُم وَرَحْمَةُ ٱللَّٰه", 250)
    Say("I'm a virtual assistant, how can I help you")

def health():
    Say_in_arabic("الحمد لله", 250)
    



def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "rafiq" in query:
        Salam()
    elif "health" in query:
        health()

#2 - Input
#eg - google search, wikipedia, youtube search

def InputExecution(tag,query):

    # more update needed
    if "wikipedia" in tag:
        try:
            name = str(query).replace("who is","").replace("talk about", "").replace("wikipedia", "").replace("what is", "")
            result = wikipedia.summary(name, 1)
            Say(result)
        except:
            pass
    elif "google" in tag:
        # search_on_google(query)
        Say("not for today, see you later")
    elif "open" in tag:
        if "notepad" in query:
            subprocess.Popen("C:\\Windows\\system32\\notepad.exe")
            Say("notepad is opened")
        elif "calculator" in query:
            subprocess.Popen("C:\\Windows\\system32\\calc.exe")
            Say("calculator is opened")
        elif "cmd" in query:
            subprocess.Popen("C:\\Windows\\system32\\cmd.exe")
            Say("command prompt is opened")
        elif "firefox" in query:
            subprocess.Popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        elif "code" in query:
            subprocess.Popen("C:\\Users\\saifu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "turbo" in query:
            subprocess.Popen("C:\\Program Files (x86)\\TurboTop\\TurboTop.exe")
        elif "file explorer" in query:
            press_and_release("windows + e")
        else:
            Say("I can't open this")
    elif "close" in tag:
        if "file explorer" in query:
            try:
                os.system("taskkill /f /im explorer.exe")
            except:
                Say("File explorer is not open")
        if "notepad" in query:
            try:
                os.system("taskkill /f /im notepad.exe")
            except:
                Say("Notepad is not open")
        elif "calculator" in query:
            try:
                os.system("taskkill /f /im calculator.exe")
            except:
                Say("calculator is not open")
        elif "cmd" in query:
            try:
                os.system("taskkill /f /im cmd.exe")
            except:
                Say("cmd is not open")
        elif "firefox" in query:
            try:
                os.system("taskkill /f /im firefox.exe")
            except:
                Say("firefox is not open")
        elif "code" in query:
            try:
                os.system("taskkill /f /im Code.exe")
            except:
                Say("vs code is not open")
        elif "turbo" in query:
            try:
                os.system("taskkill /f /im TurboTop.exe")
            except:
                Say("turotop is not open")
        else:
            Say("I can't close this")
    elif "ctrweb" in tag:
        if "name" in query:
            nameindex = query.index("name")
            name = query[nameindex+2]
        else:
            Say("Sir please provide a name of this project")