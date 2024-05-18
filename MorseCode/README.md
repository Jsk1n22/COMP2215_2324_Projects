# MORSE CODE
This project uses the PiPico with the Cytron Maker board. It was designed to use the Maker board's buzzer and the PiPico's built in LED to synchronously describe the provided Morse Code visually through the LED and audibly through the buzzer. It can process all the letters and numbers in the english alphabet, and a few punctuation characters. I used my knowledge about the buzzer from the previous challenge, which I learnt from the GitHub linked below. I researched the morse code characters and used 1s to represent dashes, 0s for dots, with pauses between each letter. For example, SOS would be: [[0,0,0],[1,1,1],[0,0,0]]

## To run
1. Connect the Pico to the MakerBoard and plug in to your PC via micro USB
2. Download Thonny & connect to the Pi Pico
3. Download all files in this directory
4. Run <code>morseCodeBuzzer.py</code>
