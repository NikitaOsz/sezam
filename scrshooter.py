import pyautogui
from pynput.keyboard import Key, Listener
import datetime


i = 1
valid = False
choice = 'None'
srcfolder = ''
name = str(datetime.date.today())
def on_press(key):
    global valid
    if key == Key.print_screen:
        valid = True


def on_release(key):
    global valid, i, choice, srcfolder
    if valid:
        if choice == 'Tak':
            source = r'C:/Users/nosze/Desktop/Nikita/Szkola' + '/' + srcfolder + '/' + name + '__' + str(i) + ".jpg"
            photo = pyautogui.screenshot()
            try:
                photo.save(source)
                i += 1
            except:
                pyautogui.alert("Nie ma takiego folderu!")
                pass
            valid = False

        else:
            srcfolder = pyautogui.prompt("W jakim folderze zapisać zdjęcie?")
            if choice != 'Nie':
                choice = pyautogui.confirm("Zapisać folder w bierzącej sesji?", buttons = ['Tak', 'Nie'])
            source = r'C:/Users/nosze/Desktop/Nikita/Szkola' + '/' + srcfolder + '/' + name + '__' + str(i) + ".jpg"
            photo = pyautogui.screenshot()
            try:
                photo.save(source)
                i += 1
            except:
                pyautogui.alert("Nie ma takiego folderu!")
                choice = 'None'
            valid = False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
