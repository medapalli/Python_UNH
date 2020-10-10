import sys
import os
import datetime
from time import sleep

now = datetime.datetime.now()


# Check indefinitely (check every five seconds if path (directory/file) exits
while True:
    print("Continuous Monitoring of File Path/File")
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d %H:%M:%S\n"))
    
    path="C:\Python_UNH\Assignment\Homework6\Test21\Test31.txt"
    
    if os.path.exists(path):
        print("True")
        print("File exists at " + path + " Directory\n")
        sleep(5)
        

    else:
        print("File does not exist at " + path + " Directory\n")
        print("False")
        sleep(5)
        
