import tkinter as tk
from smbus import SMBus

addr = 0x60                 # Defining the I2C address of the LED control device

bus = SMBus(1)              # Initializing the I2C bus

# Function to turn on the LED
def turn_on_led():
    bus.write_byte(addr, 0x1)  # Send '1' to turn on the LED
    status_label.config(text="LED turned on")  # Update status label

# Function to turn off the LED
def turn_off_led():
    bus.write_byte(addr, 0x0)  # Send '0' to turn off the LED
    status_label.config(text="LED turned off")  # Update status label

# Creating a tkinter window
app = tk.Tk()
app.title("LED Control")

# Creating buttons to turn the LED on and off
on_button = tk.Button(app, text="LED ON", command=turn_on_led, bg="green")
off_button = tk.Button(app, text="LED OFF", command=turn_off_led, bg="red")

# Creating a label to display the status
status_label = tk.Label(app, text="Status: ")

# Pack the buttons and status label in the window
on_button.pack()
off_button.pack()
status_label.pack()

# Starting the main loop
app.mainloop()
