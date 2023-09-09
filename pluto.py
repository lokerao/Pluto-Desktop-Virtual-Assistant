import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from ecapture import ecapture as ec
import json
import requests
import subprocess
import pywhatkit
import pyjokes
import psutil

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!!')
    else:
        speak('Good Evening!!')

    speak("I am pluto! How Can I Help You?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {command}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
         
    return command
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('21r21a6286@mlrinstitutions.ac.in', 'Lokesh@9848')
    server.sendmail('21r21a6286@mlrinstitutions.ac.in', to, content)
    server.close()


if __name__=="__main__" : 
 while True:  
   word=takeCommand().lower()  
   if 'pluto' in word :
     wishMe()
     while True:
         command = takeCommand().lower()
         if 'wikipedia'  in command:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
         elif 'open youtube' in command:
               webbrowser.open("youtube.com")
         elif 'open wikipedia' in command:
               webbrowser.open("wikipedia.com")     

         elif 'open google' in command:
               webbrowser.open("google.com")     
        
         elif 'send email' in command:
            
                speak("What should I say")
                print("what should i say?")
                content = takeCommand()
                to = '21r21a6296@mlrinstitutions.ac.in'    
                sendEmail(to, content)
                speak("Email has been sent!")
          
         elif 'time' in command:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
             speak(f"Sir, the time is {strTime}")
             print(strTime)

         elif 'open code' in command:
            codePath = "C:\\Users\\Lokesh\\AppData\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        
         elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)

         elif "camera" in command or "take a photo" in command:
              ec.capture(0,"robo camera","img.jpg")
         elif 'play' in command:
              song = command.replace("play","")
              speak('playing '+song)
              pywhatkit.playonyt(song)   
         elif 'battery' in command:
             print(psutil.sensors_battery())
             speak(psutil.sensors_battery())
             
         elif 'cpu frequency' in command:
             print(psutil.cpu_freq())
             speak(psutil.cpu_freq())
         elif 'memory' in command:
             print(psutil.virtual_memory())
             speak(psutil.virtual_memory()) 
         elif 'boot time' in command:
             print(psutil.boot_time())
             speak(psutil.boot_time())
         elif 'system users' in command:
             print(psutil.users())
             speak(psutil.users())  
         elif 'address' in command:
             print(psutil.net_if_addrs())
             speak(psutil.net_if_addrs())         
         elif "weather" in command:
            api_key="2df4f564db2c62adf3dabf36eae3c1e1"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

   else:
     speak(f"who is {word}? im pluto")   
  

         

        






    

 

 
 