#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import math


__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7
pin_to_circuit2 = 8

GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

def mainMenu():
    print("1.Light Sensor")
    print("2.Temperature sensor")
    print("3.Two sensor operation")
    
    selection=int(input("Enter Choice: "))
    if selection==1:
        print("@")
        try:
    # Main loop
            while True:
                print(rc_time(pin_to_circuit))
                if rc_time(pin_to_circuit) > 100000:
                    GPIO.output(11,GPIO.HIGH)
                else:
                    GPIO.output(11,GPIO.LOW)
        except KeyboardInterrupt:
                pass   
        finally:
            GPIO.cleanup()
    elif selection==2:
        print("@")
        try:
    # Main loop
            while True:
                st = math.log(rc_time(pin_to_circuit2) / 1000000.0) / 3950.0
                st += 1.0 / (22.0 + 273.15)
                st = (1.0 / st) - 273.15
                print("C. ",st)
                if rc_time(pin_to_circuit2) < 100000:
                    GPIO.output(16,GPIO.HIGH)
                else:
                    GPIO.output(16,GPIO.LOW)
        except KeyboardInterrupt:
                pass   
        finally:
            GPIO.cleanup()
    elif selection==3:
        print("1@1")
        try:
            while True:                
            
                print("-------------")
                print("light:",rc_time(pin_to_circuit))#light value
                
                if rc_time(pin_to_circuit) > 100000:
                    GPIO.output(11,GPIO.HIGH)
                else:
                    GPIO.output(11,GPIO.LOW)
                    
                st = math.log(rc_time(pin_to_circuit2) / 1000000.0) / 3950.0
                st += 1.0 / (22.0 + 273.15)
                st = (1.0 / st) - 273.15
                print("temp:",st)#temperature value
                
                if rc_time(pin_to_circuit2) < 100000:
                    GPIO.output(16,GPIO.HIGH)
                else:
                    GPIO.output(16,GPIO.LOW)
                    
        except KeyboardInterrupt:
                pass   
        finally:
            GPIO.cleanup()
            
    else:
        print("Invalid choice. Enter 1-3")
        mainMenu()
mainMenu()
