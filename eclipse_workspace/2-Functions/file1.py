import time
from time import strftime

def timeComparer(no):
    seconds = strftime("%S")
    print("Time in seconds is: "+seconds)
    if int(no)==int(seconds):
        print("Guessed correct!")
        quit()
    else:
        print("Wrong guess!")
        
attempts = 5

while attempts>0:
    number = input("\nEnter a number between 1 and 59: ")
    timeComparer(number)
    attempts = attempts-1

quit()


        
    