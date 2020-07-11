from sense_hat import SenseHat
import mysql.connector

sense = SenseHat()

class Context:
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
    
    def get_

while True:
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  password="raspberry"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)