###  This example code uses: Maker Pi Pico ;; Reference: www.cytron.io/p-maker-pi-pico

import machine
import time
import pitches
from pitches import *

def doTheRickRoll():
    buzzer = machine.PWM(machine.Pin(18))  # set pin 18 as PWM OUTPUT
    rickRoll = [A6, B6, D7, B6, FS7, 0, 0, FS7, 0, 0, E7, 0, 0,
            A6, B6, D7, B6, E7, 0, 0, E7, 0, 0, D7, CS7, B6, 0, 0,
            A6, B6, D7, B6, D7, 0, 0, E7, CS7, 0, A6, 0, A6, E7, 0, D7, 0]
    for i in rickRoll:
        if i == 0:
            buzzer.duty_u16(0)            # 0% volume
        else:
            buzzer.freq(i)                # set frequency (notes)
            buzzer.duty_u16(20000)        # sets the volume
        time.sleep(0.15)
