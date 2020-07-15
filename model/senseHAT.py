from sense_hat import SenseHat
from time import sleep

# Define some colors
whi = (255, 255, 255)
bla = (0, 0, 0)
red = (255, 0, 0)
ora = (255, 165, 0)
yel = (255, 255, 0)
gre = (0, 77, 0)
blu = (102, 153, 255)
vio = (238, 130, 238)
pur = (255, 51, 255)
bro = (102, 102, 51)
dpu = (102, 0, 102)
cre = (255, 255, 153)
gol = (255, 232, 102)
gra = (102, 51, 0)

class SenseHAT:
    sense = SenseHat()
    sense.low_light = True

    @staticmethod
    def display_image_duration(image, time):
        SenseHat.sense.clear()
        SenseHAT.sense.set_pixels(image)
        sleep(time)

    @staticmethod
    def get_data():
        temp = SenseHAT.sense.get_temperature()
        humidity = SenseHAT.sense.get_humidity()
        return (temp, humidity)

    @staticmethod
    def show_message(message, color = whi):
        SenseHat.sense.clear()
        SenseHAT.sense.show_message(message, text_colour = color)

    @staticmethod
    def detect_stick():
        for event in SenseHat.sense.stick.get_events():
            if event.action == "pressed":
                return True
        return False