import RPi.GPIO as GPIO
from time import sleep

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# Turn off GPIO warnings caused by us declaring our pins outside of the start_furby and stop_furby functions
GPIO.setwarnings(False)

def start_furby():
    # Drive the motor clockwise
    GPIO.output(12, GPIO.HIGH) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2

    # Set the motor speed
    GPIO.output(7, GPIO.HIGH) # Set PWMA

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

def stop_furby():
    # Reset all the GPIO pins by setting them to LOW
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    GPIO.output(7, GPIO.LOW) # Set PWMA
    GPIO.output(13, GPIO.LOW) # Set STBY

def main():
    # Set up GPIO pins
    GPIO.setup(7, GPIO.OUT) # Connected to PWMA
    GPIO.setup(11, GPIO.OUT) # Connected to AIN2
    GPIO.setup(12, GPIO.OUT) # Connected to AIN1
    GPIO.setup(13, GPIO.OUT) # Connected to STBY

#    start_furby()
#    sleep(10)
#    stop_furby()
    # Open file and check contents
#    with open(soundcard_status_file, 'r') as fh:
#        value = fh.read()
#        if value == 'RUNNING':
#            start_furby()
#        else:
#            stop_furby()

if __name__ == '__main__':
    main()
