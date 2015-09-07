#author : Raghav Thanigaivel ; raghav.thanigaivel@colorado.edu
#name : file2.py
#purpose : A script to emulate interface from 'War Games'
#date : 2015.08.27
#version : 0.4

in_str_1=input("Shall we play a game? ")

if(in_str_1=="chess"):
    print("Okay.")

else:
    in_str_2=input("Wouldn't you prefer a good game of chess? ")
    
    if(in_str_2=="chess"):
        print("Let's play battle chess.")
    
    else:
        print("Fine.")
    
quit()