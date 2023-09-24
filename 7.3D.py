
import RPi.GPIO as GPIO
import time

# Define GPIO pin numbers
TRIGGER_PIN = 17
ECHO_PIN = 18
BUZZER_PIN = 25

# Speed of sound in cm/s
SPEED_OF_SOUND_CM_PER_S = 17150

# Set up GPIO
def setup_gpio():
    # Use Broadcom GPIO numbering
    GPIO.setmode(GPIO.BCM)
    # Set trigger pin as an output
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    # Set echo pin as an input
    GPIO.setup(ECHO_PIN, GPIO.IN)
    # Set buzzer pin as an output
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Create a PWM object for the buzzer
def setup_buzzer():
    buzzer = GPIO.PWM(BUZZER_PIN, 1000)  # Set buzzer frequency to 1 kHz
    buzzer.start(0)  # Start with 0% duty cycle (no sound)
    return buzzer

def measure_distance():
    """
    Measure the distance from an ultrasonic sensor in centimeters.

    Returns:
        The distance in centimeters.
    """
    # Send a short trigger pulse
    GPIO.output(TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, False)

    # Measure the time it takes for the echo signal to return
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate the distance based on the speed of sound
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * SPEED_OF_SOUND_CM_PER_S

    return round(distance, 2)

try:
    setup_gpio()
    buzzer = setup_buzzer()

    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")

        # Adjust the buzzer intensity based on distance
        if distance < 20:
            buzzer.ChangeDutyCycle(50)  # Set buzzer to 50% intensity
        else:
            buzzer.ChangeDutyCycle(0)   # Turn off the buzzer

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    buzzer.stop()
    GPIO.cleanup()
