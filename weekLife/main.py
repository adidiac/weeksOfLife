from datetime import date, datetime, timedelta
from time import daylight, sleep
from PIL import Image,ImageDraw,ImageFont
from weekLife.draw import *
from weekLife.weeksCalculator import *

def introduction():
    print("Helllooo! :)")
    sleep(1)
    print("I know you want motivation.")
    sleep(2)
    print('Then, how about to generate somethin for you that will help')
    sleep(2)
    print("Still, i will need your birthday")
    sleep(2)
    year=input("Let's start with your year\n")
    month=input("Now the month\n")
    day=input("Finally let me know and your day\n")
    print("Well done, i made something for you in life.png")
    return (year,month,day)

def createFromInput():
    img = Image.new('RGB', (1200, 6000), color = 'white')
    d = ImageDraw.Draw(img)
    year,month,day=introduction()
    weeksFull=getNumberOfWeeksTillNow(1999,4,19)
    drawHeader(d)
    drawWeeks(d,weeksFull)
    img.save('life.png')

def createFromArgs(year,month,day):
    img = Image.new('RGB', (1200, 6000), color = 'white')
    d = ImageDraw.Draw(img)
    weeksFull=getNumberOfWeeksTillNow(1999,4,19)
    drawHeader(d)
    drawWeeks(d,weeksFull)
    img.save('life.png')