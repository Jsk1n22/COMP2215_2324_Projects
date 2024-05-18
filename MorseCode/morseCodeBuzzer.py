###  This example code uses: Maker Pi Pico ;; Reference: www.cytron.io/p-maker-pi-pico

import machine
import time
import pitches
from pitches import *

def getMorse(letter):
    if letter==' ':
        return []
    elif letter == 'A':
        return [0, 1]
    elif letter == 'B':
        return [1, 0, 0, 0]
    elif letter == 'C':
        return [1, 1, 0, 1]
    elif letter == 'D':
        return [1, 0, 0]
    elif letter == 'E':
        return [0]
    elif letter == 'F':
        return [0, 0, 1, 0]
    elif letter == 'G':
        return [1, 1, 1]
    elif letter == 'H':
        return [0, 0, 0, 0]
    elif letter == 'I':
        return [0, 0]
    elif letter == 'J':
        return [0, 1, 1, 1]
    elif letter == 'K':
        return [1, 1, 0]
    elif letter == 'L':
        return [0, 1, 0, 1]
    elif letter == 'M':
        return [1, 1]
    elif letter == 'N':
        return [1, 0]
    elif letter == 'O':
        return [1, 1, 1]
    elif letter == 'P':
        return [0, 1, 1, 0]
    elif letter == 'Q':
        return [1, 1, 0, 1, 1]
    elif letter == 'R':
        return [0, 1, 1]
    elif letter == 'S':
        return [0, 0, 0]
    elif letter == 'T':
        return [1]
    elif letter == 'U':
        return [0, 0, 1]
    elif letter == 'V':
        return [0, 0, 0, 1]
    elif letter == 'W':
        return [0, 1, 1, 0]
    elif letter == 'X':
        return [1, 0, 0, 1]
    elif letter == 'Y':
        return [1, 1, 0, 0]
    elif letter == 'Z':
        return [1, 1, 0, 1]
    elif letter == '0':
        return [1, 1, 1, 1, 1]
    elif letter == '1':
        return [0, 1, 1, 1, 1]
    elif letter == '2':
        return [0, 0, 1, 1, 1]
    elif letter == '3':
        return [0, 0, 0, 1, 1]
    elif letter == '4':
        return [0, 0, 0, 0, 1]
    elif letter == '5':
        return [0, 0, 0, 0, 0]
    elif letter == '6':
        return [1, 0, 0, 0, 0]
    elif letter == '7':
        return [1, 1, 0, 0, 0]
    elif letter == '8':
        return [1, 1, 1, 0, 0]
    elif letter == '9':
        return [1, 1, 1, 1, 0]
    elif letter == '.':
        return [0, 1, 0, 1, 1, 1]  # Period
    elif letter == ',':
        return [1, 1, 0, 0, 1, 1]  # Comma

morseMsg = "sos sos"
buzzer = machine.PWM(machine.Pin(18)) 
buzzer.freq(3000)
internalLED = machine.Pin('LED', machine.Pin.OUT)

for c in morseMsg:
    c=c.upper()
    notes=getMorse(c)
    for n in notes:
        internalLED.value(1)
        buzzer.duty_u16(5000)        # sets the volume
        if n == 0:
            time.sleep(0.1)
        else:
            time.sleep(0.3)
        internalLED.value(0)
        buzzer.duty_u16(0)            # 0% volume
        time.sleep(0.3)
    time.sleep(0.6)
