from essential_function import tokenize, list_to_str
import webbrowser
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
import time
import pyperclip

keyboard = Controller()

def open_links(query, web_num):
    query = tokenize(query)
    query = str('+'.join(query))
    search = "http://www.google.com/search?q="+query+"&num="+str(web_num+2)
    webbrowser.open(search)
    time.sleep(3)
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('u')
        keyboard.release('u')
    time.sleep(1)
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('a')
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('c')
    keyboard.release('a')
    time.sleep(1)
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('w')
        keyboard.release('w')
    time.sleep(1)
    data = pyperclip.paste()
    time.sleep(2)
    f = open('H:\python projects\Rafiq A.I\database\data\data.txt','w', encoding="UTF-8")
    f.write(data)
    f.close()
    time.sleep(2)
    r = open('H:\python projects\Rafiq A.I\database\data\data.txt','r',encoding="UTF-8")
    data = r.read()
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find_all('div', class_="yuRUbf")
    for h in soup[:int(web_num)]:
        web_link = h.a.get('href')
        webbrowser.open(web_link)