from gpiozero import LED, Button
from signal import pause 

button = Button(26, bounce_time = 0.05)

redLed = LED(17)
blueLed = LED(27)
greenLed = LED(22)

ledIndex = 0

def switch():
    global ledIndex
    if ledIndex ==0 :
        redLed.on()
        blueLed.off()
        greenLed.off()
        ledIndex +=1 
    elif ledIndex == 1:
        redLed.off()
        blueLed.on()
        greenLed.off()
        ledIndex +=1
    else:
        redLed.off()
        blueLed.off()
        greenLed.on()
        ledIndex = 0 
    
button.when_pressed= switch

pause()
