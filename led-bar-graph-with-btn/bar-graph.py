from gpiozero import LED,Button
from signal import pause 

ledPins = [2,3,17,27,22,18,23,24,25,8]
leds = [LED(pin=pin,  active_high=False) for pin in ledPins] 

button = Button(26,bounce_time = 0.05)

ledIndex = 0

def turnLedsOn():
    global ledIndex 
    if ledIndex == 10:
        ledIndex =0 
        for i in range(len(leds)):
            leds[i].off()
    leds[ledIndex].on()
    ledIndex +=1


button.when_pressed = turnLedsOn

pause()