# Arduino Live Data Feed

## Overview

This project consists of two main components: A Python script (`AltitudeOut.py`) and an Arduino script (`UltrasonicSensor.ino`). The project aims to monitor and store live altitude data from an Arduino board into a CSV file.

## Components

1. **Python Script (`AltitudeOut.py`)**
    - Reads data from an Arduino device via a serial connection.
    - Includes functionality to handle disconnections and user interruptions gracefully.
    - Saves the data to a CSV file.

2. **Arduino Script (`UltrasonicSensor.ino`)**
    - Measures distance using an ultrasonic sensor connected to the Arduino board.
    - Sens the distance data over the serial port to the connected computer.

## Requirements

### Hardware
- Arduino board (e.g., Arduino UNO)
- Ultrasonic sensor (e.g., HC-SR04)
- Jumper Wires
- Breadboard

### Software
- Python 3.x
- Pyserial
- Arduino IDE

## Setup and Installation

### Arduino

1. Connect the ultrasonic sensor to the Arduino as follows:
    - VCC to 5V
    - GND to GND
    - Trig to digital pin 9
    - Echo to digital pin 8

2. Open the `UltrasonicSensor.ino` script in the Arduino IDE.
3. Upload the script to the Arduino board.

### Python

1. Install the required Python packages:
    ```
    pip install pyserial serial
    ```
2. Ensure the Arduino is connected to the computer and note the COM port (e.g., `COM9`).
3. Update the COM port in the `AltitudeOut.py` scrip if necessary.
4. Run the Python script:
    ```
    python AltitudeOut.py
    ```

## Usage

1. After running the Python script, a CSV file `Altitude.csv` is created, storing all the altitude values with the corresponding timestamps.
2. Use Ctrl+c to terminate the data collection and close the application.

## Script Details

### Python Script (`AltitudeOut.py`)

- **Loop:**
    - Continuously reads altitude data from the serial port and saves the data to the CSV file.

### Arduino script (`UltrasonicSensor.ino`)

- **Setup:**
    - Initializes serial communication.
    - Sets the ultrasonic sensor pins.

- **Loop:**
    - Sends a trigger pulse tp the ultrasonic sensor.
    - Reads the echo pulse duration.
    - Calculates the distance based on the duration.
    - Sends the distance data over the serial port.

## Notes

- Ensure the Arduino is properly connected to the specified COM port before running the Python script.
- The Python script will create an `Altitude.csv` file to log the altitude data.

## Troubleshooting

- **KeyboardInterrupt**: The script can be terminated using keyboard interrupts (Ctrl+c).
- **SerialException**: Check the Arduino connection and the specified COM port.

## References

- [Arduino](https://www.arduino.cc)
- [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html)
