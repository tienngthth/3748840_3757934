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

"""
Class PiSenseHat is to connect and use SenseHat API for sensor reading and display message to SenseHat
"""

class PiSenseHat:
    sense = SenseHat()
    sense.low_light = True
    
    #Display image in a specific ammount of time
    @staticmethod
    def display_image_duration(image, time = 0):
        PiSenseHat.sense.clear()
        PiSenseHat.sense.set_pixels(image)
        sleep(time)

    #Collect all environmental sensor data at that moment
    @staticmethod
    def get_context():
        temp_humidity = PiSenseHat.sense.get_temperature_from_humidity()
        temp_pressure = PiSenseHat.sense.get_temperature_from_pressure()
        humidity = PiSenseHat.sense.get_humidity()
        return (temp_humidity, temp_pressure, humidity)

    #Display message on the LED matrix
    @staticmethod
    def show_message(message, colour = whi, speed = 0.065):
        PiSenseHat.sense.clear()
        PiSenseHat.sense.show_message(message, text_colour = colour, scroll_speed = speed)
    
    #Display letter to the LED maxtrix
    @staticmethod
    def show_letter(letter, colour = whi):
        PiSenseHat.sense.clear()
        PiSenseHat.sense.show_letter(letter, colour)

    #Detect moving joystick to different direction
    @staticmethod
    def detect_stick():
        for event in PiSenseHat.sense.stick.get_events():
            if event.action == "pressed":
                return True
        return False

    #Detect pressing joystick down
    @staticmethod
    def detect_stick_middle():
        for event in PiSenseHat.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    return "middle"
                else:
                    return "pressed"
        return False

    #Get accelerometer sensor reading 
    @staticmethod
    def get_accelerometer(): 
        return PiSenseHat.sense.get_accelerometer_raw()

