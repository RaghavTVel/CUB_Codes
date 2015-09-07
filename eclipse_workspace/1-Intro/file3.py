#author : Raghav Thanigaivel raghav.thanigaivel@colorado.edu
#name : file3.py
#purpose : A script for the new random number guessing program
#date : 2015.08.27
#version : 0.3

import random

ch=1
ctr=0

num_gen=random.randint(1,20)
#print("Number generated is "+str(num_gen))

while ch==1:
    num_in=input("Please enter a number: ")
    num_in=int(num_in)
    ctr=ctr+1

    if num_in>=1:
        if num_in<=20:
            if num_in<num_gen:
                print("Less")
            if num_in>num_gen:
                print("More")
            if num_in==num_gen:
                print("Equal")
                ch=0
        else:
            print("Number out of range")
    else:
        print("Number out of range")

if(ctr==1):
    print("Excellent")
if(ctr>=2):
    if(ctr<=19):
        print("OK")
if(ctr==20):
    print("Bad")
        
print("Guessed correctly in "+str(ctr)+" tries")
quit()