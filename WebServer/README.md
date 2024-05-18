## MicroPython Web Server and remote RickRoll Buzzer
This project uses the PiPico with the Cytron Maker board. It was designed to be a standard web server with a few extensions. I used the Pico's built in LED to blink out the last number of the Pico's allocated local IP address (e.g. 192.168.0.XX), so that when you connect the Pico to an external battery you can discover what its IP address and connect to it after counting the blinks. I saved the script as <code>main.py</code> to ensure it ran as soon as the Pico received power. The web page contained a button to turn the LED on/off, a measured reading of the Pico's temperature, and a button to activate the RickRoll buzzer.

I used the buzzer on the Maker board to buzz a 'RickRoll' (Rick Astley, Never Gonna Give You Up) chorus. By setting the buzzer to different frequencies, I could produce different musical notes. I used the github repository for the Maker Board to learn how to use the buzzer and get a list of the musical notes and their frequencies <code>pitches.py</code>. I looked up the melody for the song, and created an array of the musical notes and the gaps between them to replicate the song.

It was my first task on the PiPico and first time using python and micropython, I've linked the material that helped me to make the project below. When setting the code to be the <code>main.py</code>, I 'bricked' my Pico a couple times, as the broken code always ran and errored, locking me out from communicating with the Pico. I've linked the forum I found to solve this, the proposed solution did not work for me, I had to use the <code>flash_nuke.uf2</code> to reset my Pico instead.

## To run
1. Connect the Pico to the Maker board and plug in to your PC via micro USB
2. Download Thonny & connect to the Pi Pico
3. Download all files in this directory
4. When the Pi received power, <code>main.py</code> will run
