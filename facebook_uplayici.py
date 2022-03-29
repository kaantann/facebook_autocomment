'''
ALGORİTMA
---------

1. Linkler alınacak
2. Mevcut tarayıcı açılıp linke gidilecek
3. Post'un altına 'Up!' yazılacak
4. Adres çubuğuna yeni link gelecek
5. Bütün linkler için bu senaryo gerçekleştirilecek (3 ve 4)
6. Tarayıcı Kapatılacak

'''
import time
import webbrowser
import pyautogui
import os

#changing directory to the file location
os.chdir(os.path.dirname(__file__))

#open the file
linkler_burda = open("linkler.txt",mode='r')

#read the links one by one
linkler = linkler_burda.readlines()

#close the file
linkler_burda.close()

#opening the client
def open_new_window():
    webbrowser.open_new(linkler[0])
    time.sleep(11)

#opening a new tab
def open_new_tab():
    webbrowser.open_new_tab(linkler[link])
    time.sleep(8)

#commenting 'Up!'
def typing_up():
    pyautogui.moveTo(308,707)
    pyautogui.click(button='left', clicks=1)
    pyautogui.press("end")
    pyautogui.moveTo(700,930)
    pyautogui.click(button='left', clicks=1)
    pyautogui.typewrite("Up!", interval=0.05)
    pyautogui.press("enter")
    time.sleep(5)

#executing
link_sayisi = len(linkler)
for link in range(link_sayisi):
    if link == 0:
        open_new_window()
        typing_up()
    else:
        open_new_tab()
        typing_up()
        pyautogui.hotkey('ctrl','w')
    
pyautogui.alert(text='Tüm postlara başarılı biçimde Up! yazıldı', title='ODTÜ-HAYDOST OTOMASYON LTD. ŞTİ.', button="Tamam knk tşk")

pyautogui.hotkey('ctrl','w')

