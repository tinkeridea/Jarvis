import pyttsx3
import speech_recognition as sr
import datetime
import os
from cv2 import cv2
import random
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
from requests import get
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
import sys
import time
import pyjokes
import pyautogui
import articles
import PyQt5    
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, Qt, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=32c463405cc1459289c069ab49b73788'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")
        

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#def sendEmail(to,content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
#    server.starttls()
#    server.login('ykushwaha873@gmail.com', 'Yogesh@123')
#    server.sendmail('ykushwaha873@gmail.com', to, content)
#    server.close()


#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning!")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon!")
    else:
        speak(f"Good evening!")
    speak("I am jarvis sir, please tell me how may i help you!")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution


    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #audio = r.listen(source, timeout=5, phrase_time_limit=8)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception:
            #speak("Say that again please...")
            return "none"
        query = query.lower()
        return query

    def TaskExecution(self):
        wish()
        while True:
        #if 1:
            self.query = self.takecommand().lower()
            #logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Users\\HOME\\Documents\\Notepad"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Reader XI.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "D:\\Songs\\Songs"
                songs = os.listdir(music_dir)
                #rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))


            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP Address is {ip}")

            elif "wikipedia" in self.query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                speak(results)
                print(results)

            elif "open facebook" in self.query:
                    webbrowser.open("www.facebook.com")

            elif "open instagram" in self.query:
                    webbrowser.open("www.instagram.com")

            elif "open amazon" in self.query:
                    webbrowser.open("www.amazon.com")

            elif "open stack overflow" in self.query:
                    webbrowser.open("www.stackoverflow.com")

            elif "open map" in self.query:
                    webbrowser.open("maps.google.com")

            elif "open youtube" in self.query:
                    webbrowser.open("www.youtube.com")

            elif "open google" in self.query:
                    speak("Sir, what should i search on Google")
                    cm = self.takecommand().lower()
                    webbrowser.open(f"{cm}")
                    speak(cm)

            elif "send message" in self.query:
                    kit.sendwhatmsg("+919454958133", "this is testing protocol",2,25)
                    time.sleep(120)
                    speak("message has been sent")

            elif "play music on Youtube" in self.query:
                    kit.playonyt("see you again")

            #elif "email to yogesh" in query:
            #        try:
            #            speak("what should i say?")
            #            content = self.blockSignalstakecommand().lower()
            #            to = "ukushwaha414@gmail.com"
            #            sendEmail(to,content)
            #            speak("Email has been succesfully sent ")
            #
            #        except Exception as e:
            #            print(e)
            #            speak("soory sir!, i am not able to sent mail to yogesh.")

            elif "you can sleep" in self.query:
                    speak("thanks for using me sir!, have a good day.")
                    sys.exit()

            #to close a any application
            elif "close notepad" in self.query:
                    speak("okay sir!, closing notepad")
                    os.system("C:\\Users\\HOME\\Documents\\Notepad")

            #to set an alarm
            elif "set alarm" in self.query:
                    nn = int(datetime.datetime.now().hour)
                    if nn==22:
                        music_dir = 'D:\\Songs\\Songs'
                        songs = os.listdir(music_dir)
                        os.startfile(os.path.join(music_dir, songs[0]))

            #to find a joke
            elif "tell me joke" in self.query:
                    joke = pyjokes.get_jokes()
                    speak(joke)

            elif "shut the system" in self.query:
                    os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                    os.system("shutdown /r /t 5")

            #elif "sleep the system" in query:
            #        os.system("rund1132.exe powrprof.d11,SetSuspendState 0,1,0")

            elif 'switch the window' in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                    speak("Please wait sir!, feteching the latest news")
                    news()

            elif "nothing" in self.query:
                    speak("thanks for using me sir!, have a good day.")
                    sys.exit()

            elif "email to yogesh" in self.query:

                    speak("sir what should i say")
                    self.query = self.takecommand().lower()
                    if"send a file" in self.query:
                        email = 'ykushwaha873@gmail.com'
                        password = 'Yogesh@123'
                        send_to_email = 'ukushwaha414@gmail.com'
                        speak("okay sir!, what is the subject for this email")
                        self.query = self.takecommand().lower()
                        subject = query  # the subject in the email
                        speak("and sir!, what is the message for this email?")
                        self.query2 = self.takecommand().lower()
                        message = self.query2
                        speak("sir please enter the correct path for the file into the shell")
                        file_location = input("please enter the path here!: ")  # the file attachment in the file

                        speak("please wait!, i am sending email now.")

                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = send_to_email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(message, 'plain'))

                        # Setup the attachment
                        filename = os.path.basename(file_location)
                        attachment = open(file_location, "rb")
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                        #Attach the attachment to the MIMEMulticular object
                        msg.attach(part)

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        text = msg.as_string()
                        server.sendmail(email, send_to_email, text)
                        server.quit()
                        speak("email has sent to yogesh!")

                    else:
                        email = 'ykushwaha873@gmail.com'
                        password = 'Yogesh@123'
                        send_to_email = 'ukushwaha414@gmail.com'
                        message = self.query

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        server.sendmail(email, send_to_email, message)
                        server.quit()
                        speak("email has been sent to yogesh")

        #speak("sir!, do you have any other work.")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Pictures/Saved Pictures/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/Saved Pictures/iron-man-jarvis-gif-5.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/Saved Pictures/AgileFixedBichonfrise-size_restricted.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/Saved Pictures/J.A.R.V.I.S-Live-Wallpaper-GIF.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/Saved Pictures/8ee7d93c9b015c00938a4091c3ef443e951d1518_hq.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../Pictures/Saved Pictures/wm59k.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTimer.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label_6.setText(label_date)
        self.ui.label_7.setText(label_time)


app= QtWidgets.QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())   