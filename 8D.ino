#include <Wire.h>

int ledPin = 12; // Defining the Arduino pin connected to the LED

void setup() {
  Wire.begin(0x60); // Initializing the I2C communication with the Arduino's address as 0x60

  Wire.onReceive(ledFunc); // Setup a callback function which will handle incoming I2C data

  pinMode(ledPin, OUTPUT); // Setting the LED pin as an output
  digitalWrite(ledPin, LOW); // Ensuring the LED is initially turned off
}

// Callback function to handle incoming I2C data
void ledFunc(int i) {
  while (Wire.available()) {
    char a = Wire.read(); // Reading the incoming data from the I2C bus

    digitalWrite(ledPin, a); // Control the LED based on the received data
  }
}

void loop() {
  delay(100);
}
