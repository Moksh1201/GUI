# Import necessary modules
from tkinter import * # Module for creating GUI
import tkinter.font # Module for working with fonts
from gpiozero import LED # Module for controlling GPIO pins
import RPi.GPIO as GPIO # Module for GPIO pin numbering 

# Set pin numbering scheme  
GPIO.setmode(GPIO.BCM)

# Create LED objects 
red_led = LED(17) 
blue_led = LED(22)
green_led = LED(24)

# Create main window
main_window = Tk()  
main_window.title("LED GUI")

# Create font
my_font = tkinter.font.Font(family='Helvetica', size=30, weight='bold')

# Function to toggle red LED  
def toggle_red_led():
  if red_led.is_lit:
    red_led.off()
    red_button["text"] = "Turn Red LED ON"
  else:
    red_led.on()
    red_button["text"] = "Turn Red LED Off"
    
    blue_led.off()
    blue_button["text"] = "Turn Blue LED On"
    
    green_led.off()
    green_button["text"] = "Turn Green LED On"
      
# Function to toggle blue LED
def toggle_blue_led():
  if blue_led.is_lit:
    blue_led.off()
    blue_button["text"] = "Turn Blue LED ON"
  else:
    blue_led.on()
    blue_button["text"] = "Turn Blue LED Off"
    
    red_led.off()
    red_button["text"] = "Turn Red LED On"
    
    green_led.off()
    green_button["text"] = "Turn Green LED On"
    
# Function to toggle green LED  
def toggle_green_led():
  if green_led.is_lit:
    green_led.off()
    green_button["text"] = "Turn Green LED ON"
  else:
    green_led.on()
    green_button["text"] = "Turn Green LED Off"
    
    red_led.off()
    red_button["text"] = "Turn Red LED On"
    
    blue_led.off()
    blue_button["text"] = "Turn Blue LED On"
    
# Function to exit GUI    
def quit_gui():
  GPIO.cleanup()
  main_window.destroy()
  
# Create button to toggle red LED  
red_button = Button(main_window, text='Turn Red LED On', font=my_font, 
                   command=toggle_red_led, bg='Red', height=1, width=50)
red_button.grid(row=0, column=1)

# Create button to toggle blue LED
blue_button = Button(main_window, text='Turn Blue LED On', font=my_font,
                    command=toggle_blue_led, bg='Blue', height=1, width=50)
blue_button.grid(row=1, column=1) 

# Create button to toggle green LED
green_button = Button(main_window, text='Turn Green LED On', font=my_font,
                     command=toggle_green_led, bg='Green', height=1, width=50)
green_button.grid(row=2, column=1)

# Create exit button 
exit_button = Button(main_window, text='Exit', font=my_font, command=quit_gui, 
                    bg='Gray', height=1, width=50)
exit_button.grid(row=3, column=1)
