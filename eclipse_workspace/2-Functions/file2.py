import time
from time import strftime
import urllib.request
import re 

def timeReturn(page_string):
    time_mdt = re.search('\w\w\w[.]\s\d\d[,]\s\d\d[:]\d\d[:]\d\d\s\w\w\s[M][S][T]',page_string)
    time_edt = re.search('\w\w\w[.]\s\d\d[,]\s\d\d[:]\d\d[:]\d\d\s\w\w\s[E][S][T]',page_string)
    time_alaska = re.search('\w\w\w[.]\s\d\d[,]\s\d\d[:]\d\d[:]\d\d\s\w\w\s[A][K][S][T]',page_string)
    
    if hasattr(time_mdt,'group'):
        print("Network time in MDT: "+time_mdt.group(0))
    if hasattr(time_edt,'group'):
        print("Network time in EDT: "+time_edt.group(0))
    if hasattr(time_alaska,'group'):
        print("Network time in Alaska: "+time_alaska.group(0))
    
    return(time_mdt.group(0)[12:14]) #Returning 'minutes' portion of the MDT string to the main program for comparison

while True:
    new_page = urllib.request.urlopen("https://web.archive.org/web/20150205195107/http://tycho.usno.navy.mil/timer.html")
    page_str = new_page.read().decode("utf8")
    minutes_mdt = timeReturn(page_str)
    minutes_local = strftime("%M")

    if int(minutes_local)==int(minutes_mdt):
        print("Local computer time matches Network time")
    else:
        print("Local computer time is off")
    time.sleep(60)
