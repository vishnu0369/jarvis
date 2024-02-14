import time
import datetime
import pyttsx3
import speech_recognition as sr

master="vishnu"
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("dot")
        print("listening")
        r.pause_threshold=0.6
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio,language="en-in")

    except Exception as e:
        print(" can you repeat it again")
        query=None

    return query



query=takecommand()
query=query.lower()
print(query)

if "class" and "next" in query:
    day=int(datetime.datetime.today().strftime("%w"))
    timenow=datetime.datetime.now().strftime("%H:%M")
    hournow=int(datetime.datetime.now().strftime("%H"))
    minnow=int(datetime.datetime.now().strftime("%M"))

    #Monday
    class11="BEE"
    time11="9:30 AM"
    hour11=int(9)
    min11=int(30)
    mine11=int(50)

    class12="chemistry"
    time12="11 PM"
    hour12=int(11)
    min12=int(0)
    mine12=0

    class13="English"
    time13="12:15 PM"
    hour13=int(12)
    min13=int(15)
    mine13=int(15)


    class14="M1"
    time14="2:15 PM"
    hour14=int(14)
    min14=int(15)
    mine14=int(45)



    #day 2 i.e tuesday
       
    class21="Chemistry"
    time21="9:30 AM"
    hour21=int(9)
    min21=int(30)
    mine21=int(50)

    class22="Python"
    time22="11 PM"
    hour22=int(11)
    min22=int(0)
    mine22=int(0)

    class23="M1 lab"
    time23="2:15 PM"
    hour23=int(14)
    min23=int(15)
    mine23=int(45)
    
    
    #day 3 i.e wednesday
       
    class31="Chemistry"
    time31="9:30 AM"
    hour31=int(9)
    min31=int(30)
    mine31=int(50)

    class32="M1"
    time32="11 PM"
    hour32=int(11)
    min32=int(0)
    mine32=0

    class33="BEE"
    time33="12:15 PM"
    hour33=int(12)
    min33=int(15)
    mine33=int(15)


    class34="Chemistry"
    time34="2:15 PM"
    hour34=int(14)
    min34=int(15)
    mine34=int(45)



    # day 4 i.e thursday
    class41="M1"
    time41="9:30 AM"
    hour41=int(9)
    min41=int(30)
    mine41=int(50)

    class42="Python"
    time42="11 PM"
    hour42=int(11)
    min42=int(0)
    mine42=int(0)

    class43="chemistry"
    time43="2:15 PM"
    hour43=int(14)
    min43=int(15)
    mine43=int(45)
    
    
    #friday i.e day 5
        
       
    class51="BEE"
    time51="9:30 AM"
    hour51=int(9)
    min51=int(30)
    mine51=int(50)

    class52="M1"
    time52="11 PM"
    hour52=int(11)
    min52=int(0)
    mine52=0

    class53="PCE"
    time53="12:15 PM"
    hour53=int(12)
    min53=int(15)
    mine53=int(15)


    class54="Mentor"
    time54="2:15 PM"
    hour54=int(14)
    min54=int(15)
    mine54=int(45)

    #saturday i.e day 6

    class61="PCE"
    time61="9:30 AM"
    hour61=int(9)
    min61=int(30)
    mine61=int(50)

    class62="Python"
    time62="11 PM"
    hour62=int(11)
    min62=int(0)
    mine62=int(0)

    class63="BEE"
    time63="2:15 PM"
    hour63=int(14)
    min63=int(15)
    mine63=int(45)
    

     #sunday
    if day==0:
        speak("Rock the day {0} you are not having any class, its sunday".format(master))

    #Monday
    if day==1: 
        if hournow<(hour11+1) : #class at 9:30
            if hournow==hour11:  # if time greater than 9
                if minnow<min11:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class11,int(((hour11-hournow)*60)+(min11-minnow)),time11))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class11,int(((hournow-hour11)*60)+(minnow-min11)),time11))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class11,int(((hour11-hournow)*60)+(min11-minnow)),time11))
        elif hournow==(hour11+1):
            if minnow<mine11:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class41,int(((hournow-hour41)*60)+(minnow-min41)),time41))
            else:
               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))

        elif hournow<(hour12+1) :
            if hournow==hour12:  
                if minnow<min12: 
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class12,int(((hour12-hournow)*60)+(min12-minnow)),time12))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class12,int(((hournow-hour12)*60)+(minnow-min12)),time12))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class12,int(((hour12-hournow)*60)+(min12-minnow)),time12))
        elif hournow==hour12+1:
            if minnow<mine12:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class12,int(((hournow-hour12)*60)+(minnow-min12)),time12))
            else:
                 speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class13,int(((hour13-hournow)*60)+(min13-minnow)),time13))
        
        elif hournow<(hour13+1) : #class at 9:30
            if hournow==hour13:  # if time greater than 9
                if minnow<min13:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class13,int(((hour13-hournow)*60)+(min13-minnow)),time13))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class13,int(((hournow-hour13)*60)+(minnow-min13)),time13))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class13,int(((hour13-hournow)*60)+(min13-minnow)),time13))
        elif hournow==(hour13+1) :
            if minnow<mine13:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class13,int(((hournow-hour13)*60)+(minnow-min13)),time13))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class14,int(((hour14-hournow)*60)+(min14-minnow)),time14))
        elif hournow<(hour14+1) : #class at 9:30
            if hournow==hour14:  # if time greater than 9
                if minnow<min14:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class14,int(((hour14-hournow)*60)+(min14-minnow)),time14))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class14,int(((hournow-hour14)*60)+(minnow-min14)),time14))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class14,int(((hour14-hournow)*60)+(min14-minnow)),time14))
        elif hournow==(hour14+1) :
            if minnow<mine14:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class14,int(((hournow-hour14)*60)+(minnow-min14)),time14))
            else:
                speak("No more classes today , You have succesfully completed your classes. ")
        else:
             speak("No more classes today , You have succesfully completed your classes. ")


     #Tuesday
     
    if day==2: 
        if hournow<(hour21+1) : #class at 9:30
            if hournow==hour21:  # if time greater than 9
                if minnow<min21:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class21,int(((hour21-hournow)*60)+(min21-minnow)),time21))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class21,int(((hournow-hour21)*60)+(minnow-min21)),time21))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class21,int(((hour21-hournow)*60)+(min21-minnow)),time21))
        elif hournow==(hour21+1):
            if minnow<mine21:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class21,int(((hournow-hour21)*60)+(minnow-min21)),time21))
            else:
               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class22,int(((hour22-hournow)*60)+(min22-minnow)),time22))

        elif hournow<(hour22+1) :
            if hournow==hour22:  
                if minnow<min22: 
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class22,int(((hour22-hournow)*60)+(min22-minnow)),time22))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class22,int(((hournow-hour22)*60)+(minnow-min22)),time22))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class22,int(((hour22-hournow)*60)+(min22-minnow)),time22))
        elif hournow==hour22+1:
               speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class22,int(((hournow-hour22)*60)+(minnow-min22)),time22))
        elif hournow==(hour22+2):
            if minnow<mine22:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class22,int(((hournow-hour22)*60)+(minnow-min22)),time22))
            else:
                 speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class23,int(((hour23-hournow)*60)+(min23-minnow)),time23))
        
        elif hournow<(hour23+1) : #class at 9:30
            if hournow==hour23:  # if time greater than 9
                if minnow<min23:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class23,int(((hour23-hournow)*60)+(min23-minnow)),time23))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class23,int(((hournow-hour23)*60)+(minnow-min23)),time23))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class23,int(((hour23-hournow)*60)+(min23-minnow)),time23))
        elif hournow==(hour23+1) :
            if minnow<mine23:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class23,int(((hournow-hour23)*60)+(minnow-min23)),time23))
            else:
                speak("No more classes today , You have succesfully completed your classes. ")
        else:
             speak("No more classes today , You have succesfully completed your classes. ")
    #wednesday
    if day==3: 
        if hournow<(hour31+1) : #class at 9:30
            if hournow==hour31:  # if time greater than 9
                if minnow<min31:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class31,int(((hour31-hournow)*60)+(min31-minnow)),time31))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class31,int(((hournow-hour31)*60)+(minnow-min31)),time31))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class31,int(((hour31-hournow)*60)+(min31-minnow)),time31))
        elif hournow==(hour31+1):
            if minnow<mine31:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class31,int(((hournow-hour31)*60)+(minnow-min31)),time31))
            else:
               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class32,int(((hour32-hournow)*60)+(min32-minnow)),time32))

        elif hournow<(hour32+1) :
            if hournow==hour32:  
                if minnow<min32: 
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class32,int(((hour32-hournow)*60)+(min32-minnow)),time32))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class32,int(((hournow-hour32)*60)+(minnow-min32)),time32))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class32,int(((hour32-hournow)*60)+(min32-minnow)),time32))
        elif hournow==hour32+1:
            if minnow<mine32:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class32,int(((hournow-hour32)*60)+(minnow-min32)),time32))
            else:
                 speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class33,int(((hour33-hournow)*60)+(min33-minnow)),time33))
        
        elif hournow<(hour33+1) : #class at 9:30
            if hournow==hour33:  # if time greater than 9
                if minnow<min33:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class33,int(((hour33-hournow)*60)+(min33-minnow)),time33))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class33,int(((hournow-hour33)*60)+(minnow-min33)),time33))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class33,int(((hour33-hournow)*60)+(min33-minnow)),time33))
        elif hournow==(hour33+1) :
            if minnow<mine33:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class33,int(((hournow-hour33)*60)+(minnow-min33)),time33))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class34,int(((hour34-hournow)*60)+(min34-minnow)),time34))
        elif hournow<(hour34+1) : #class at 9:30
            if hournow==hour34:  # if time greater than 9
                if minnow<min34:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class34,int(((hour34-hournow)*60)+(min34-minnow)),time34))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class34,int(((hournow-hour34)*60)+(minnow-min34)),time34))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class34,int(((hour34-hournow)*60)+(min34-minnow)),time34))
        elif hournow==(hour34+1) :
            if minnow<mine34:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class34,int(((hournow-hour34)*60)+(minnow-min34)),time34))
            else:
                speak("No more classes today , You have succesfully completed your classes. ")
        else:
             speak("No more classes today , You have succesfully completed your classes. ")


    #thursday
    if day==4: 
        if hournow<(hour41+1) : #class at 9:30
            if hournow==hour41:  # if time greater than 9
                if minnow<min41:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class41,int(((hour41-hournow)*60)+(min41-minnow)),time41))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class41,int(((hournow-hour41)*60)+(minnow-min41)),time41))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class41,int(((hour41-hournow)*60)+(min41-minnow)),time41))
        elif hournow==(hour41+1):
            if minnow<mine41:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class41,int(((hournow-hour41)*60)+(minnow-min41)),time41))
            else:
               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))

        elif hournow<(hour42+1) :
            if hournow==hour42:  
                if minnow<min42: 
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class42,int(((hournow-hour42)*60)+(minnow-min42)),time42))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class42,int(((hour42-hournow)*60)+(min42-minnow)),time42))
        elif hournow==hour42+1:
               speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class42,int(((hournow-hour42)*60)+(minnow-min42)),time42))
        elif hournow==(hour42+2):
            if minnow<mine42:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class42,int(((hournow-hour42)*60)+(minnow-min42)),time42))
            else:
                 speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class43,int(((hour43-hournow)*60)+(min43-minnow)),time43))
        
        elif hournow<(hour43+1) : #class at 9:30
            if hournow==hour43:  # if time greater than 9
                if minnow<min43:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class43,int(((hour43-hournow)*60)+(min43-minnow)),time43))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class43,int(((hournow-hour43)*60)+(minnow-min43)),time43))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class43,int(((hour43-hournow)*60)+(min43-minnow)),time43))
        elif hournow==(hour43+1) :
            if minnow<mine43:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class43,int(((hournow-hour43)*60)+(minnow-min43)),time43))
            else:
                speak("No more classes today , You have succesfully completed your classes. ")
        else:
             speak("No more classes today , You have succesfully completed your classes. ")

     #Friday day 5
    if day==3: 
        if hournow<(hour51+1) : #class at 9:30
            if hournow==hour51:  # if time greater than 9
                if minnow<min51:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class51,int(((hour51-hournow)*60)+(min51-minnow)),time51))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class51,int(((hournow-hour51)*60)+(minnow-min51)),time51))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class31,int(((hour51-hournow)*60)+(min51-minnow)),time51))
        elif hournow==(hour51+1):
            if minnow<mine51:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class51,int(((hournow-hour51)*60)+(minnow-min51)),time51))
            else:
               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class52,int(((hour52-hournow)*60)+(min52-minnow)),time52))

        elif hournow<(hour52+1) :
            if hournow==hour52:  
                if minnow<min52: 
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class52,int(((hour52-hournow)*60)+(min52-minnow)),time52))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class52,int(((hournow-hour52)*60)+(minnow-min52)),time52))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class52,int(((hour52-hournow)*60)+(min52-minnow)),time52))
        elif hournow==hour52+1:
            if minnow<mine52:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class52,int(((hournow-hour52)*60)+(minnow-min52)),time52))
            else:
                 speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class53,int(((hour53-hournow)*60)+(min53-minnow)),time53))
        
        elif hournow<(hour53+1) : #class at 9:30
            if hournow==hour53:  # if time greater than 9
                if minnow<min53:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class53,int(((hour53-hournow)*60)+(min53-minnow)),time53))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class53,int(((hournow-hour53)*60)+(minnow-min53)),time53))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class53,int(((hour53-hournow)*60)+(min53-minnow)),time53))
        elif hournow==(hour53+1) :
            if minnow<mine53:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class53,int(((hournow-hour53)*60)+(minnow-min53)),time53))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class54,int(((hour54-hournow)*60)+(min54-minnow)),time54))
        elif hournow<(hour54+1) : #class at 9:30
            if hournow==hour54:  # if time greater than 9
                if minnow<min54:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class54,int(((hour54-hournow)*60)+(min54-minnow)),time54))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class54,int(((hournow-hour54)*60)+(minnow-min54)),time54))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class54,int(((hour54-hournow)*60)+(min54-minnow)),time54))
        elif hournow==(hour54+1) :
            if minnow<mine54:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class54,int(((hournow-hour54)*60)+(minnow-min54)),time54))
            else:
                speak("No more classes today , You have succesfully completed your classes. ")
        else:
             speak("No more classes today , You have succesfully completed your classes. ")


    #saturday i.e day 6
    if day==6: 
        if hournow<(hour61+1) : #class at 9:30
            if hournow==hour61:  # if time greater than 9
                if minnow<min61:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class61,int(((hour61-hournow)*60)+(min61-minnow)),time61))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class61,int(((hournow-hour61)*60)+(minnow-min61)),time61))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class61,int(((hour61-hournow)*60)+(min61-minnow)),time61))
        elif hournow==(hour61+1):
            if minnow<mine61:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class61,int(((hournow-hour61)*60)+(minnow-min61)),time61))
            else:
               speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class62,int(((hour62-hournow)*60)+(min62-minnow)),time62))

        elif hournow<(hour62+1) :
            if hournow==hour62:  
                if minnow<min62: 
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class62,int(((hour62-hournow)*60)+(min62-minnow)),time62))
                else:
                     speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class62,int(((hournow-hour62)*60)+(minnow-min62)),time62))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class62,int(((hour62-hournow)*60)+(min62-minnow)),time62))
        elif hournow==hour62+1:
               speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class62,int(((hournow-hour62)*60)+(minnow-min62)),time62))
        elif hournow==(hour62+2):
            if minnow<mine62:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class62,int(((hournow-hour62)*60)+(minnow-min62)),time62))
            else:
                 speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class63,int(((hour63-hournow)*60)+(min63-minnow)),time63))
        
        elif hournow<(hour63+1) : #class at 9:30
            if hournow==hour63:  # if time greater than 9
                if minnow<min63:  # if time less than 30 min
                     speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class63,int(((hour63-hournow)*60)+(min63-minnow)),time63))
                else:
                    speak("Hey {0} class already started {1} minutes ago ,that is at {2} ".format(class63,int(((hournow-hour63)*60)+(minnow-min63)),time63))
            else:
                speak("{0} class is going to start in {1} minutes ,that is at {2}".format(class63,int(((hour63-hournow)*60)+(min63-minnow)),time63))
        elif hournow==(hour63+1) :
            if minnow<mine63:
             speak("Hey , {0} class already started {1} minutes ago ,that is at {2} ".format(class63,int(((hournow-hour63)*60)+(minnow-min63)),time63))
            else:
                speak("No more classes today , You have succesfully completed your classes. ")
        else:
             speak("No more classes today , You have succesfully completed your classes. ")

        
             