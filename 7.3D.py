import RPi.GPIO as GPIO  # Import the Raspberry Pi GPIO library
import time  # Import the time library for delays

# Define GPIO pin numbers
TRIGGER_PIN = 17  # Define the trigger pin for the ultrasonic sensor
ECHO_PIN = 18     # Define the echo pin for the ultrasonic sensor
BUZZER_PIN = 25   # Define the pin for the buzzer

# Speed of sound in cm/s (approximate)
SPEED_OF_SOUND_CM_PER_S = 17150  # Speed of sound for distance calculation

# Set up GPIO (General Purpose Input/Output)
def setup_gpio():
    GPIO.setmode(GPIO.BCM)  # Set the GPIO numbering mode to BCM
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)  # Set the trigger pin as an output
    GPIO.setup(ECHO_PIN, GPIO.IN)      # Set the echo pin as an input
    GPIO.setup(BUZZER_PIN, GPIO.OUT)    # Set the buzzer pin as an output

# Create a PWM (Pulse Width Modulation) object for the buzzer
def setup_buzzer():
    buzzer = GPIO.PWM(BUZZER_PIN, 1000)  # Create a PWM object for the buzzer with a 1 kHz frequency
    buzzer.start(0)  # Start the buzzer with a 0% duty cycle (no sound)
    return buzzer

# Measure the distance from the ultrasonic sensor
def measure_distance():
    """
    Measure the distance from an ultrasonic sensor in centimeters.

    Returns:
        The distance in centimeters.
    """
    GPIO.output(TRIGGER_PIN, True)    # Send a short trigger pulse to the ultrasonic sensor
    time.sleep(0.00001)               # Wait for a short time
    GPIO.output(TRIGGER_PIN, False)   # Stop the trigger pulse

    pulse_start = 0  # Initialize variables for measuring the pulse duration
    pulse_end = 0

    while GPIO.input(ECHO_PIN) == 0:  # Wait for the echo signal to start
        pulse_start = time.time()     # Record the start time

    while GPIO.input(ECHO_PIN) == 1:  # Wait for the echo signal to end
        pulse_end = time.time()       # Record the end time

    pulse_duration = pulse_end - pulse_start  # Calculate the pulse duration
    distance = pulse_duration * SPEED_OF_SOUND_CM_PER_S  # Calculate the distance

    return round(distance, 2)  # Return the distance rounded to 2 decimal places

try:
    setup_gpio()       # Initialize the GPIO pins
    buzzer = setup_buzzer()  # Initialize the buzzer

    while True:  # Start an infinite loop for continuous measurement
        distance = measure_distance()  # Measure the distance
        print(f"Distance: {distance} cm")  # Print the distance

        # Adjust the buzzer intensity based on distance
        if distance < 20:  # If an object is closer than 20 cm
            intensity = int((20 - distance) * 5)  # Calculate intensity based on distance (adjust multiplier for sensitivity)
            buzzer.ChangeDutyCycle(intensity)  # Adjust buzzer intensity
        else:
            buzzer.ChangeDutyCycle(0)  # Turn off the buzzer if no object is close

        time.sleep(0.1)  # Pause for 0.1 seconds between measurements

except KeyboardInterrupt:  # Handle Ctrl+C to gracefully exit the program
    pass

finally:  # Cleanup GPIO and stop the buzzer when exiting
    buzzer.stop()  # Stop the buzzer
    GPIO.cleanup()  # Clean up GPIO configuration
