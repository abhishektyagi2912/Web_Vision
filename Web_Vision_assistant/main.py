from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import speech_recognition as sr
import time
import pyttsx3
import random
from pyautogui import keyDown, keyUp, press

chrome_options = ChromeOptions()
chrome_options.add_extension('Web_Vision.crx')
s = Service('C:\\Users\\anees\\PycharmProjects\\Browser\\chromedriver.exe')
driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options, service=s)
# driver = webdriver.Chrome('C:\\Users\\anees\\PycharmProjects\\Browser\\chromedriver.exe')
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()


def speak(query):
    engine.say(query)
    engine.runAndWait()


def recognize_speech():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.05)
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response


time.sleep(1.5)
speak("Hey.  I   am   online!")
while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open google' or 'search google' or 'google' in voice:
        speak('Opening google..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        # driver.switch_to_window(window_list[-1])
        driver.switch_to.window(driver.window_handles[-1])
        driver.get('https://google.com')
        while True:
            speak('what to search')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'sleep' in voice:
        time.sleep(30)


    elif 'open url' in voice:
        while True:
            speak('which url')
            query = recognize_speech()
            if query != 'Error':
                break
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(driver.window_handles[-1])
        driver.get('https://' + query)
    elif 'open youtube' in voice:
        speak('Opening youtube..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(driver.window_handles[-1])
        driver.get('https://youtube.com')
    elif 'open news' in voice:
        speak('Opening news..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to.window(driver.window_handles[-1])
        list1 = [
            'https://www.ndtv.com/india-news/11-dead-in-massive-fire-in-timber-godown-in-telanganas-secunderabad-2837704',
            'https://www.hindustantimes.com/quick-read']
        driver.get(random.choice(list1))
    elif 'search youtube' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('search_query')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'tab switch' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver.switch_to.window(driver.window_handles[cur_tab])
    elif 'close tab' in voice:
        speak('Closing Tab..')
        driver.close()
    elif 'go back' in voice:
        driver.back()
    elif 'go forward' in voice:
        driver.forward()
    elif 'exit' in voice:
        speak('Goodbye!')
        driver.quit()
        break
    elif 'start reading' in voice:
        keyDown('Ctrl')
        keyDown('Shift')
        press('X')
        keyUp('Ctrl')
        keyUp('Shift')
        time.sleep(20)
    # elif 'stop reading' in voice:
    #     keyDown('Alt')
    #     press('S')
    #     keyUp('Alt')
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(1.5)
