from PIL import Image,ImageDraw,ImageFont


def drawHeader(d):
    fnt = ImageFont.truetype('weekLife/Roboto-Black.ttf', 70)
    fnt3 = ImageFont.truetype('weekLife/Roboto-Black.ttf', 25)
    w,h=d.textsize("Week's till now",font=fnt)
    w1,d1=d.textsize("When you get started?",font=fnt3)
    d.text(((1200-w-100)/2,40), "Week's of your life", fill=(0,0,0),font=fnt)
    d.text(((1200-w1+10)/2,130),"When you get started?", fill=(0,0,0),font=fnt3)

def drawWeeks(d,weeksFull):
    fnt2= ImageFont.truetype('weekLife/Roboto-Black.ttf', 20)
    offsetY=200
    for i in range(0,81,5):
        d.text((10,i*70+200),"{}".format(i),fill=(0,0,0),font=fnt2)

    offsetX=45
    offsetY=200
    dimension=25
    for i in range(161):
        for j in range(25):
            positionX=j*45+offsetX
            positionY=i*35+offsetY
            if(weeksFull):
                d.rectangle((positionX,positionY,positionX+dimension,positionY+dimension),fill=(0,0,0))
                weeksFull-=1
            else:
                d.rectangle((positionX,positionY,positionX+dimension,positionY+dimension),fill=(255,255,255),outline="black")