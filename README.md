
![WhatsApp Image 2022-03-24 at 03 14 41](https://user-images.githubusercontent.com/81071871/159801043-ef878b3a-378a-4483-a118-bac39f760e17.jpeg)

# WebVision

Webvision is planned to be a complete solution for the visually impaired. The World Wide Web is the center for information and knowledge sharing. The internet connects the world and we think that no one should be left behind.

It centers around the needs of the visually impaired, and will combine multiple features such as voice commands, text to speech content to simplify accessing visual information by persons with visual disability. Thus, it will improve accessibility and provide them a user friendly environment.


### Requirements:
Python version 3.7

Chrome web driver in accordance to the installed version of chrome (Current version in the project is 99.0.4844.51)

### Installation:
Download/Clone the repository 

Run the following command in current directory terminal
```
pip install -r requirements.txt
```

### Usage:


> Run main.py, and give the desired command.

Available Voice commands:
```
-Open google
-Search google
-Open YouTube
-Open News
-Open URL
-sleep
-scroll tab
-close tab
-go back
-go forward
-start reading
-exit
```

Keyboard commands:
```
Ctrl+Shift+X : Trigger/start the extension
Alt+S : Stop
Alt+W : Play/Pause
Alt+A : Rewind
```

### Functionality:
This project will use Javascript, HTML and CSS for the chrome extension and Python for web automation and voice commands.

#### Chrome Extension:
* The chrome will convert the textual content of the page into audio format.
* The extension is capable of translating the text into 40+ different languages.
* It will also magnify and highlight text for people with low vision.
* The user can modulate the pitch, speed and volume of the output speech 

It uses : 
* Google Translate API - Used to translate the text from the source language to the desired language.
* Web Speech API- Used for speech synthesis in the chrome extension to convert the written text to audio.
![image](https://user-images.githubusercontent.com/81071871/159798979-f5535251-34ca-4d7f-8f8d-91cbc9fcc5bd.png)
#### Voice Assistant:
The user will be able to use voice commands to open a web page, read page, search and playback control commands to navigate and access the content on the web.

It uses : 
* Selenium - every automated command in the browser is executed with the help of selenium
* PyAudio - Any voice output by the assistant is made by the help of PyAudio
* Speech Recognition - Any voice input given to the assistant is made with the help of speech recognition module.
* Pyttsx3 - Responsible for text-to-speech conversion
* PyAutoGUI - It is used to convert voice commands into hotkey instructions (keyboard shortcuts) required to invoke the extension to enable a hands-free experience.
  
### Flow Chart:


![WhatsApp Image 2022-03-24 at 5 37 33 AM](https://user-images.githubusercontent.com/85986613/159821095-cf3a3ffc-8697-4a86-b90b-0a136a5891ee.jpeg)


### Future plans:

* Enable OCR support to enable the user to access image text
* Develop an additional AI for greater automated control on devices.
* Filter the webpage content to reduce irrelevant information, thus improving the user experience.
* Add support for more languages in speech recognition for the voice assistant.
* Complete access of the web only through voice commands for the visually impaired.


# Project Video Link :

https://www.youtube.com/watch?v=6-foe5rDckU
