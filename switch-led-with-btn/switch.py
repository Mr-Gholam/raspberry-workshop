from gpiozero import LED, Button
from signal import pause 

button = Button(26, bounce_time = 0.05)

redLed = LED(17)
blueLed = LED(27)
greenLed = LED(22)

ledList = [redLed,blueLed,greenLed]

ledIndex = 0

for i in range(len(ledList)):
    ledList[i].off()

def switch():
    global ledIndex
    ledList[ledIndex-1].off()
    ledList[ledIndex].on()
    if ledIndex>= len(ledList)-1:
        ledIndex =0
    else:
        ledIndex +=1
    
button.when_pressed= switch

pause()
