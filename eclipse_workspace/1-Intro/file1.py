#author : Raghav Thanigaivel ; raghav.thanigaivel@colorado.edu
#name : file1.py
#purpose : A script to generate and compare random numbers from 1 to 20
#date : 2015.08.27
#version : 0.5

import random

num_gen=random.randint(1,20)
#print("Number generated is "+str(num_gen))

num_in=input("Please enter a number: ")
num_in=int(num_in)

if num_in>=1:
    if num_in<=20:
        if num_in<num_gen:
            print("Less")
        if num_in>num_gen:
            print("More")
        if num_in==num_gen:
            print("Equal")
    else:
        print("Number out of range")
else:
    print("Number out of range")

quit()