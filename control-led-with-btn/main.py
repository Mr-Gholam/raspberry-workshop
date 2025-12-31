from gpiozero import LED, Button

button = Button(26)
led = LED(17)

def control():
    while True: 
        if(button.is_pressed):
            led.on()
            print("Button pressed, Led on")
        else:
            led.off()
            print("Button released, Led off")


if __name__ == "__main__":
    print("App is running, press the button")
    control()