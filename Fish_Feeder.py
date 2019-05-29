import math, time, subprocess
from adafruit_motorkit import MotorKit
from urllib.request import urlopen
from adafruit_motor import stepper
global ammount #92 for medium, 110 for small and large
kit = MotorKit ()
counter = 0
numdays = 0
foodType = "p" #s = small, m = medium, l = large
def update_time ():
    print ("Please enter the correct date and time in the following format:")
    print ("4 digit year,dash, 2 digit month, dash, 2 digit day space, 2 digit hour, colon, 2 digit minute, colon, 2 digit second.")
    print ("Please use military time.")
    print ("Example: 2019-05-21 13:00:00")
    print ("This may take a few minutes")
    now = input ("> ") 
        
    year = ""
    month = ""
    day = ""
    hour = ""
    minute = ""
    second = ""
    dayOfWeek = ""

    for i in range (len (now)):
        if 0 <= i <= 3:
            year += now [i]
            #print (year)
        elif 5 <= i <= 6:
            month += now [i]
            #print (month)
        elif 8 <= i <= 9:
            day += now [i]
            #print (day)
        elif 11 <= i <= 12:
            hour += now [i]
            #print (hour)
        elif 14 <= i <= 15:
            minute += now [i]
            #print (minute)
        elif 17 <= i <= 18:
            second += now [i]
            #print (second)

    month = int (month)
    if month == 1:
        mon = "Jan"
    elif month == 2:
        mon = "Feb"
    elif month == 3:
        mon = "Mar"
    elif month == 4:
        mon = "Apr"
    elif month == 5:
        mon = "May"
    elif month == 6:
        mon = "Jun"
    elif month == 7:
        mon = "Jul"
    elif month == 8:
        mon = "Aug"
    elif month == 9:
        mon = "Sep"
    elif month == 10:
        mon = "Oct"
    elif month == 11:
        mon = "Nov"
    elif month == 12:
        mon = "Dec"
    date = mon +' '+ day +' '+hour+':'+minute+':'+second+' '+'MDT'+' '+year
    #print(date)
    subprocess.run (["sudo", "date", "-s",  date]) #subprocess has output you can print this line to see it.
    #TO show the format needed for this process #####subprocess.run (["sudo", "date", "-s", 'June 21 10:00:00 MDT 2019'])
    #print ("hello")
    
def Prime():
    for i in range (15):
        print(15 - i)
        time.sleep(1)
    for i in range (ammount * 4):  ##72 out of 200 steps (200 steps should be 360 degrees)
        kit.stepper1.onestep(direction=stepper.BACKWARD)
        time.sleep(0.01)


##""" This code will run the motor every 10 seconds"""
##while True:
##    for i in range (ammount):  ##72 out of 200 steps (200 steps should be 360 degrees)
##        kit.stepper1.onestep(direction=stepper.BACKWARD)
##        time.sleep(0.01)
##    kit.stepper1.release()  #turns off motor
##    time.sleep(5) 

print ("Welcome to your fish feeder.")
print ("For the program to work properly, we need to know a few things first.")
print ("Is the date and time Listed in the top right corner correct? ")
print ()
good = False
while not good:
    choice = input ("Type 'Y' or 'y' for yes or 'N' or 'n' for no. ")
    if choice == "N" or choice == "n":
        update_time ()
        print("Time Updated")
        good = True
        
    elif choice == "Y" or choice == "y":
        break
    else:
        print ()
        print ("                                  Type only 'y' or 'n' nothing else... Try again.")
#asks for and updates food size
foodType = input("What size of food is being added? enter 's' 'm' or 'l'. ")
while(not(foodType == "s" or foodType == "l" or foodType == "m")):
    foodType = input("enter 's' 'm' or 'l'")
if((foodType == "s") or (foodType == "l")):
    ammount = 110
    #print(ammount)
elif(foodType == "m"):
    ammount = 92
    #print(ammount)
    
    
#asks for the feeding time
prime = 'j' 
while not (prime == 'y' or prime == 'Y' or prime == 'n' or prime == 'Y'):
    prime =  input("Are you changing the type of food? type only 'y' or 'n'. ")
if(prime == "Y" or prime == "y"):
    print("Empty out any remaining food of the previous type")
    print("Add new food to fill line plus 3 scoops")
    print("Hold something under the feeder while we prime the system")
    done = input("Once you enter 'd', you will have 15 seconds to get over to the feeder. ")
    if(done == "d"):
        Prime()
        print("Primed")

x = int(input("What hour do the fish need to be fed?   Make sure the hour is in military time."))
y = int(input("What minute do the fish need to be fed? "))
z = int(input("What second do the fish need to be fed? "))

print("Thank you, feeder is now running")
#program begins here        
##Time = time.strftime("%Y %m %d %H:%M:%S ")
##print (Time)
kit.stepper1.release()
while True:
    result_str = time.strftime("%Y %m %d %H:%M:%S ")
    #print (result_str)
    #res = urlopen('http://just-the-time.appspot.com/')
    #result = res.read().strip()
    #print (result)
    #b'2017-07-28 04:53:46'
    #result_str = result.decode('utf-8')
    #print (result_str)
    #'2017-07-28 04:53:46'
    year = ""
    month = ""
    day = ""
    hour = ""
    minute = ""
    second = ""

    for i in range (len (result_str)):
        if 0 <= i <= 3:
            year += result_str [i]
            #print (y)
        elif 5 <= i <= 6:
            month += result_str [i]
            #print (mon)
        elif 8 <= i <= 9:
            day += result_str [i]
            #print (d)
        elif 11 <= i <= 12:
            hour += result_str [i]
            #print (hour)
        elif 14 <= i <= 15:
            minute += result_str [i]
            #print (m)
        elif 17 <= i <= 18:
            second += result_str [i]
            #print (s)
    #hour = int (hour)-6
    month = int (month)
    if month == 1:
        mon = "Jan"
    elif month == 2:
        mon = "Feb"
    elif month == 3:
        mon = "Mar"
    elif month == 4:
        mon = "Apr"
    elif month == 5:
        mon = "May"
    elif month == 6:
        mon = "Jun"
    elif month == 7:
        mon = "Jul"
    elif month == 8:
        mon = "Aug"
    elif month == 9:
        mon = "Sep"
    elif month == 10:
        mon = "Oct"
    elif month == 11:
        mon = "Nov"
    elif month == 12:
        mon = "Dec"
    print ("The current time is", str(hour)+":"+(minute)+":"+ (second))
    print ("Today is", mon, str(day)+",", str(year)+".")
    print ("The feeder has run", counter, "time(s).")
    print ()
    if int (hour) == x and int (minute) == y and z <= int (second) < 8:
        for i in range (ammount):
            kit.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)
        kit.stepper1.release()
        counter += 1
    time.sleep (8)
