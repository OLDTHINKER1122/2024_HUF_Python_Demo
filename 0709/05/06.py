import RPi.GPIO as GPIO
from time import sleep

btn_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  if GPIO.input(btn_pin) == GPIO.HIGH:
    print("no")
  elif GPIO.input(btn_pin) == GPIO.LOW:
    print("click")
  sleep(0.2)