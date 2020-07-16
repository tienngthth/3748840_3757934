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

class PiSenseHat:
    sense = SenseHat()
    sense.low_light = True
    
    @staticmethod
    def display_image_duration(image, time):
        PiSenseHat.sense.clear()
        PiSenseHat.sense.set_pixels(image)
        sleep(time)

    @staticmethod
    def get_data():
        temp = PiSenseHat.sense.get_temperature()
        humidity = PiSenseHat.sense.get_humidity()
        return (temp, humidity)

    @staticmethod
    def show_message(message, colour = whi):
        PiSenseHat.sense.clear()
        PiSenseHat.sense.show_message(message, text_colour = colour)
        
    @staticmethod
    def show_letter(letter, colour = whi):
        PiSenseHat.sense.clear()
        PiSenseHat.sense.show_letter(letter, colour)

    @staticmethod
    def detect_stick():
        for event in PiSenseHat.sense.stick.get_events():
            if event.action == "pressed":
                #PiSenseHat.sense.clear()
                return True
        return False



