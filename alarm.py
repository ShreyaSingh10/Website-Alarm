# Import the time module, it provides various time-related
# functions.
import time
import os
# Import the webbrowser module, it is used to
# display various HTML documents to the user.
import webbrowser
 
# First Input: It is the time of the form
# 'Hours:Minutes:Seconds' that you'll
# use to set the alarm.
url = input("Enter your url")
Set_Alarm = input("Set the website alarm as H:M:S:")
 
# Second Input: It is the URL that you want
# to open on the given time.
 
# This is the actual time
Actual_Time = time.strftime("%I:%M:%S")
 
# This is the while loop that'll print the time
# until it's value will be equal to the alarm time
while (Actual_Time != Set_Alarm):
    #print ("The time is " + Actual_Time)
    Actual_Time = time.strftime("%I:%M:%S")
 
# This if statement plays the role when its the time for alarm and executes the code within it.
if (Actual_Time == Set_Alarm):
    print ("You should see your webpage now :-)")
 
    # We are calling the open() function from the webrowser module. opens the alarm and takes us to the website
    webbrowser.open(".\\tune\\Cavin.mp3")
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)