import os, time
import pyautogui as pg
cnfm = input('Do you want to proceed?\n')
still=''
r=0
def keypress(key,n=1):
    for i in range(n):
        pg.press(key)
response=response = os.system('ping google.com')

def retry():
    for i in range(4):
        print('Retrying in ' ,4-i)
        time.sleep(0.3)

while response and r<3:
    response = os.system('ping google.com')
    print('It seems you '+still+'aren\'t connected to internet now, i\'ll wait for you')
    retry()
    still='still '
    r+=1
else:
    print('Seems there\'s some issue while pinging. If  date & time not updated after this, troubleshoot your internet then retry opening the application')
    retry()

pg.click(1300,760)
time.sleep(1)
pg.click(1250,690)
time.sleep(2)
keypress('tab',6)
time.sleep(.5)
keypress('right',2)
time.sleep(.5)
keypress('tab')
time.sleep(.5)
keypress('enter')
time.sleep(.5)
keypress('tab',2)
time.sleep(.5)
keypress('enter')
time.sleep(.5)
keypress('tab')
time.sleep(.5)
keypress('enter')
time.sleep(.5)
keypress('tab',2)
time.sleep(.5)
keypress('enter')
