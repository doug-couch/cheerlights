from serial import Serial
import time
import requests
import json

# Setup serial connection to arduino

DEVICE = 'COM6'
BAUD = 115200
arduino = Serial(DEVICE, BAUD)

# I'm going to use a var to check if I've seen the color before
color = 'black'
cheerlights = color

# Read the thingspeak feed to get the current color
while True:
  try:
    clreq = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json') #.json['field1']
  except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
    pass
  cheerlights = str(json.loads((clreq.content))["field1"])
  if cheerlights != color:
    #New color, do stuff
    arduino.write(cheerlights.encode())
    print("Changing colors to:" + cheerlights)
  color = cheerlights
  time.sleep(16)
