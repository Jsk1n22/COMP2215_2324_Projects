# COMP2215_2324_Projects
##MicroPython Web Server and remote RickRoll Buzzer##
###Description###
This project uses the PiPico with the Cytron Maker board. It was designed to be a standard web server with a few extensions. I used the Pico's built in LED to blink out the last number of the Pico's allocated local IP address (e.g. 192.168.0.XX), so that when you connect the Pico to an external battery you can discover what its IP address and connect to it after counting the blinks. I saved the script as <code>main.py</code> to ensure it ran as soon as the Pico received power. The web page contained a button to turn the LED on/off, a measured reading of the Pico's temperature, and a button to activate the RickRoll buzzer.

I used the buzzer on the Maker board to buzz a 'RickRoll' (Rick Astley, Never Gonna Give You Up) chorus. By setting the buzzer to different frequencies, I could produce different musical notes. I used the github repository for the Maker Board to learn how to use the buzzer and get a list of the musical notes and their frequencies <code>pitches.py</code>. I looked up the melody for the song, and created an array of the musical notes and the gaps between them to replicate the song.

It was my first task on the PiPico and first time using python and micropython, I've linked the material that helped me to make the project below. When setting the code to be the <code>main.py</code>, I 'bricked' my Pico a couple times, as the broken code always ran and errored, locking me out from communicating with the Pico. I've linked the forum I found to solve this, the proposed solution did not work for me, I had to use the <code>flash_nuke.uf2</code> to reset my Pico instead.

###Possible extensions###
If I had more time before the deadline I would have aimed to add the following (I may implement these at a later date):
*The project currently only has a very basic html site, it could be extended to have a better web page.
*It currently supports three requests (lightOn?, lightOff?, and RickRoll?), so it could be extended to include more.
*It could have more song options.

###Material that helped###
*[https://www.w3schools.com/python/python_intro.asp W3 Schools python tutorial]
*[https://www.youtube.com/watch?v=TusJYxhISSY YouTube tutorial for starting MicroPython on a PicoW]
*[https://projects.raspberrypi.org/en/projects/get-started-pico-w/5 Setting up a Web Server on a PicoW]
*[https://github.com/CytronTechnologies/MAKER-PI-PICO Maker-Pi-Pico GitHub Repo]
*[https://forums.raspberrypi.com/viewtopic.php?t=305432 Rescuing a bricked Pico]

###GitHub Repository###
[link goes here]

##MicroPython Morse Code LED Blinker & Buzzer##
###Description###
This project uses the PiPico with the Cytron Maker board. It was designed to use the Maker board's buzzer and the PiPico's built in LED to synchronously describe the provided Morse Code visually through the LED and audibly through the buzzer. It can process all the letters and numbers in the english alphabet, and a few punctuation characters. I used my knowledge about the buzzer from the previous challenge, which I learnt from the GitHub linked below. I researched the morse code characters and used 1s to represent dashes, 0s for dots, with pauses between each letter. For example, SOS would be: [[0,0,0],[1,1,1],[0,0,0]]

###Possible extensions###
If I had more time before the deadline I would have aimed to add the following (I may implement these at a later date):
*The project currently only provides morse code for the hard coded string, and so it could be extended to receive the string to convert into morse code through a command line or a http request or similar.
*Potentially use the Maker Board's RGB light to blink in different colours to represent dots and dashes through colour.

###Material that helped###
*[https://github.com/CytronTechnologies/MAKER-PI-PICO Maker-Pi-Pico GitHub Repo]

###GitHub Repository###
[link goes here]



##LCD colour reaction speed game##
###Description###
This project uses the PiPico with the WaveShare 1.3 inch LCD. It is a game where four buttons on the LCD (A, B, X, Y) corresponded to a colour, and you get a point for pressing the button which represents the colour of the background of the LCD. If you press the correct colour, your score will increase, and your score is written on the LCD. After pressing a button, a new colour will instantly appear. I used the Waveshare LCD GitHub to learn about how to use the LCD, I used their provided LCD MicroPython object <code>LCD1inch3.py</code> to initialise the screen, then learnt how to control the buttons and change the colour of the LCD. I read the writing text to an LCD tutorial & used their <code>FONTS.py</code> to learn how to write text to the screen. I added in the game logic, colours, button controls, screen objects, and logic to clear the currently displayed text at a pixel level (as before the text was just overlapping with the previously drawn pixels).

###Possible extensions###
If I had more time before the deadline I would have aimed to add the following (I may implement these at a later date):
*Add a 10 second timer to make the game have rounds of 10s each
*Make the centre joystick (Select) button start a new round
*Keep a list of the highest scores

###Material that helped###
*[https://github.com/waveshare/LCD-show GitHub for the Waveshare LCD]
*[https://thepihut.com/blogs/raspberry-pi-tutorials/advanced-text-with-micropython-on-raspberry-pi-pico-displays Writing text to the WaveShare LCD]

###GitHub Repository###
[link goes here]
