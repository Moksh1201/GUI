import tkinter as tk
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

# Function to convert text to Morse code
def text_to_morse_code(text):
    morse_text = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_text += morse_code_dict[char] + ' '
    return morse_text

# Function to blink LED with Morse code
def blink_morse_code_signal():
    input_text = entry.get()[:12]
    morse_text = text_to_morse_code(input_text)
    
    for symbol in morse_text:
        if symbol == '.':
            GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on
            time.sleep(0.2)
            GPIO.output(led_pin, GPIO.LOW)   # Turn LED off
            time.sleep(0.2)
        elif symbol == '-':
            GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on
            time.sleep(0.6)
            GPIO.output(led_pin, GPIO.LOW)   # Turn LED off
            time.sleep(0.2)

# Function to exit the application
def exit_application():
    GPIO.cleanup()
    morse_start.destroy()

# Create the GUI window
morse_start = tk.Tk()
morse_start.title("Morse Code LED Blinker")

# Set the background color
morse_start.configure(bg="lightgray")

# Create and style a label for the title
title_label = tk.Label(morse_start, text="Morse Code LED Blinker", font=("Arial", 24, "bold"), padx=20, pady=10, fg="red", bg="gray")
title_label.pack()



# Create and style an input box
start = tk.Entry(morse_start, width=20, font=("Arial", 16))
start.pack()

# Create and style a button to blink Morse code (changed color to blue)
start_button = tk.Button(morse_start, text="Blink Morse Code", command=blink_morse_code_signal, bg="blue", fg="white", font=("Arial", 20))
start_button.pack()

# Create and style an instruction label
instruction_label = tk.Label(morse_start, text="Enter a word the word should not have more than 12 aplhabets", font=("Arial", 14), pady=10, bg="gray")
instruction_label.pack()

# Create and style an exit button
exit_button = tk.Button(morse_start, text="Exit", command=exit_application, bg="red", fg="white", font=("Arial", 20))
exit_button.pack()

# Run the GUI
morse_start.mainloop()
