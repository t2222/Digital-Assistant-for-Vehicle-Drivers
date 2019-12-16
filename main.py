# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:43:08 2019

@author: Tousif
"""
import os
import time
import speech_recognition as sr
import threading, signal
from datetime import timedelta
import requests
from firebase import firebase
import pyttsx3 as t2s
import face_recognition
import cv2 
import numpy as np
import webbrowser

import lib.runner
import lib.demo_project.web_crawl
import lib.sender_firebase



#thread methods
WAIT_TIME_SECONDS = 50

class ProgramKilled(Exception):
    pass



def signal_handler(signum, frame):
    raise ProgramKilled
    
class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs
        
    def stop(self):
                self.stopped.set()
                self.join()
    def run(self):
            while not self.stopped.wait(self.interval.total_seconds()):
                self.execute(*self.args, **self.kwargs)
#end of thread methods
                



eng=t2s.init()

def speak(text):
    try:
        eng.setProperty('rate',120);eng.setProperty('volume',.9)
        eng.say(text)
        eng.runAndWait()
    except:
        pass


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio,language="en-US")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

#may work, here goes porosh's new method
num = 1
    
    
def search(input):
    #driver=webdriver.Firefox(executable_path ="D:\programmes\geckodriver")
    #driver.implicitly_wait(1)
    #driver.maximize_window() 
    input=input.lower()
    if "go to" in input:
        l1=len("go to")
        query = input[l1 + 1:]
        query=query.lower()
        query=query.replace(" ", "")
        webbrowser.open("https://"+query)
        return    
    else:
        query = input.split()
        webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + '+'.join(query)) 
        return
    
    
def captureFromWebcam():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            print("Press S to capture your face and Q to quit")
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

def faceRecognitionMethod(name):
    known_image = face_recognition.load_image_file(name + ".jpg")
    unknown_image = face_recognition.load_image_file("saved_img.jpg")
        
    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        
    result = face_recognition.compare_faces([known_encoding], unknown_encoding)   
    return result

def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 
        
def recognizeDriverFace():
    drivers = ["tousif","porosh"]

    A = np.array([4])
    comp = (A == 4) #True class 'numpy.ndarray'
    
    captureFromWebcam()
    
    for name in drivers:
        print("status of " + name)
        res = faceRecognitionMethod(name)
        tempComp = (comp==res)
        print(tempComp)
        if tempComp == comp:
            print("Driver recognized, welcome " + name)
            return name
    
    return "none"

def detectFaceCount(): 
    captureFromWebcam()
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("saved_img.jpg")
    
    # Find all the faces in the image using the default HOG-based model.
    face_locations = face_recognition.face_locations(image)
    print(face_locations)
    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    
    for face_location in face_locations:
    
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))  
    
    


while True:
    print("Listening")
    speak("Listening")
    text = get_audio()
    
    if "hello" in text:
        speak("hello, how are you?")
        
    elif "what is your name" in text:
        speak("My name is Nino")
        
    elif "driving mode" in text:
        status = recognizeDriverFace()
        if (status == "none"):
            speak("failed to recognize driver's face, exiting")
            break
        else:
            speak("Welcome " + status + ". Driver confirmed")
            
            speak("Initiating driving mode. Please do not get drowsy.")
            #thread initiate
            signal.signal(signal.SIGTERM, signal_handler)
            signal.signal(signal.SIGINT, signal_handler)
            job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=lib.sender_firebase.foo())
            job.start()
            lib.runner.drowsiness_detection()
    
    elif "status log" in text:
        detectFaceCount()
        
    elif "news" in text:
        lib.demo_project.web_crawl.web_crawling()
        
    elif "find" in text:
        while(1):
            speak("What can i search for you?")
            voice=get_audio()
            if voice==0:
                continue
            if "exit" in voice:
                speak("Ok, Bye")
                break
            search(voice)
                
        
    elif "goodbye" in text:
        speak("Good bye, Nino is terminating!")
        print ("Location thread killed: running cleanup code")
        job.stop()
        break
    
    else:
        speak("I did not understand")