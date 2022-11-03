from ast import Break
import pyautogui
import os
from selenium import webdriver
import time
import webbrowser


os.system('cls')
print('''\n
\t /$$      /$$  /$$$$$$        /$$$$$$$              /$$    
\t| $$  /$ | $$ /$$__  $$      | $$__  $$            | $$    
\t| $$ /$$$| $$| $$  \ $$      | $$  \ $$  /$$$$$$  /$$$$$$  
\t| $$/$$ $$ $$| $$$$$$$$      | $$$$$$$  /$$__  $$|_  $$_/  
\t| $$$$_  $$$$| $$__  $$      | $$__  $$| $$  \ $$  | $$    
\t| $$$/ \  $$$| $$  | $$      | $$  \ $$| $$  | $$  | $$ /$$
\t| $$/   \  $$| $$  | $$      | $$$$$$$/|  $$$$$$/  |  $$$$/
\t|__/     \__/|__/  |__/      |_______/  \______/    \___/ .Credits Lovelak 
''')

print('\n\n\t[1] Whatsapp web by selenium\t[2] Whatsapp Desktop\t[3] Whatsapp web default')
type = str(input('\n\tSelect Your Whatsapp Version : '))
user_name = str(input('\n\tEnter Victom Name : '))
message = str(input('\n\tEnter Your Message : '))
message_amount = int(input('\n\tEnter Amount Of Messages : '))
print('''


''')

chrome_path ='C:\\Users\\Lovelak\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'



# >>>>>>>>> Whatsapp Web By selemium Code <<<<<<<<<
if type == '1':
    os.environ["PATH"] = r'C:\seleniumwebdriver'
    driver = webdriver.Chrome()
    os.system('cls')
    driver.get('https://web.whatsapp.com')
    os.system('cls')
    driver.implicitly_wait(60)
    # login = driver.find_element_by_class_name('')
    # driver.implicitly_wait(20)
    # login.click()

# >>>>>>>>> Whatsapp Desktop Code <<<<<<<<<
elif type == '2':
    time.sleep(1)
    pyautogui.hotkey('win','d')
    time.sleep(0.5)
    pyautogui.press('win')
    time.sleep(0.3)
    pyautogui.typewrite('whatsapp')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite(user_name)
    time.sleep(0.4)
    pyautogui.press('enter')
    for i in range(message_amount):
        pyautogui.typewrite(message)
        print('\n\tDone...!')
        time.sleep(0.2)
        pyautogui.press('enter')


elif type == '3':
    time.sleep(1)
    pyautogui.hotkey('win','d')
    webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open('web.whatsapp.com')
    time.sleep(15)
    pyautogui.hotkey('ctrl','alt','/')


else:
    print('\tSomething Went Wrong...!')
    time.sleep(10)
    Break










