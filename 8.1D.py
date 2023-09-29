# Import necessary libraries
import smbus  # Library for I2C communication
import time   # Library for time-related functions

# Define constants for I2C configuration
I2C_BUS = 1              # I2C bus number (1 for Raspberry Pi)
BH1750_ADDR = 0x23       # I2C address of the BH1750 sensor

# Create an I2C bus object
bus = smbus.SMBus(I2C_BUS)

# Turn on the sensor by sending a command
bus.write_byte(BH1750_ADDR, 0x01)  # 0x01 is the command to power on the sensor
time.sleep(0.2)                   # Wait for the sensor to initialize

try:
    while True:
        # Read data from the sensor
        data = bus.read_i2c_block_data(BH1750_ADDR, 0x20)  # Read 2 bytes of data
        lux = (data[1] + (256 * data[0])) / 1.2  # Calculate light intensity in lux

        # Categorize the light level
        if lux > 10000:
            light_level = "Too Bright"
        elif lux > 1000:
            light_level = "Bright"
        elif lux > 100:
            light_level = "Medium"
        elif lux > 10:
            light_level = "Dark"
        else:
            light_level = "Too Dark"

        # Print the light intensity and category
        print(f"Light Intensity: {lux} lux ({light_level})")

        time.sleep(1)  # Wait for 1 second before the next reading

except KeyboardInterrupt:
    # Handle Ctrl+C to exit the program gracefully
    print("KeyboardInterrupt")

finally:
    # Turn off the sensor by sending the power-off command
    bus.write_byte(BH1750_ADDR, 0x00)  # 0x00 is the command to power off the sensor

