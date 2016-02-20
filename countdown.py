#Countdown Timer

#learn more manipulations from https://www.codecademy.com/learn/python 

import os
from time import sleep
print "Welcome to the Countdown program (coded in Python) \nCreated by Akshit Arora <akshit.arora1995@gmail.com>"
print "Right now: ";os.system("date")
hou = input("How many hours? ")
minu = input("How many minutes? ")
sec = input("How many seconds? ")
sec = hou*60*60 + minu*60 + sec
for i in range(0,sec):
	print (sec - i)/60/60; print'hours left';
	print (sec - i)/60%60; print'minutes left';
	print (sec - i)%60; print'seconds left';
	sleep(1);

print 'Blastoff!' 
os.system("date")
print 'wake up! NOW! '
os.system("play alarm_titanium.mp3")

