import serial
import time
import serial.serialutil

altitude = 0

ser = serial.Serial("COM9", 9600)
def get_arduino_value():
    return altitude

def loop():
    global altitude
    with open("Altitude.csv", 'w') as file:
        try:
            start = time.perf_counter()
            print("0.0000, 0", file=file)
            while True:
                altitude = ser.readline().decode().strip()
                print(f'{(time.perf_counter()-start):.3f}, {altitude}')
                print(f'{(time.perf_counter()-start):.3f}, {altitude}', file=file)
        except KeyboardInterrupt:
            print("User terminated operation.")
            print("User terminated operation.", file=file)
        except serial.serialutil.SerialException:
            print("Arduino disconnected.")
            print("Arduino disconnected.", file=file)

if __name__ == "__main__":
    loop()