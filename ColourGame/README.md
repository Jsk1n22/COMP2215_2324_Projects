## LCD colour reaction speed game
### Description
This project uses the PiPico with the WaveShare 1.3 inch LCD. It is a game where four buttons on the LCD (A, B, X, Y) corresponded to a colour, and you get a point for pressing the button which represents the colour of the background of the LCD. If you press the correct colour, your score will increase, and your score is written on the LCD. After pressing a button, a new colour will instantly appear. I used the Waveshare LCD GitHub to learn about how to use the LCD, I used their provided LCD MicroPython object <code>LCD1inch3.py</code> to initialise the screen, then learnt how to control the buttons and change the colour of the LCD. I read the writing text to an LCD tutorial & used their <code>FONTS.py</code> to learn how to write text to the screen. I added in the game logic, colours, button controls, screen objects, and logic to clear the currently displayed text at a pixel level (as before the text was just overlapping with the previously drawn pixels).

## To run
1. Connect the Pico to the LCD and plug in to your PC via micro USB
2. Download Thonny & connect to the Pi Pico
3. Download all files in this directory
4. Run <code>ColourGame.py</code>

### Possible extensions
If I had more time before the deadline I would have aimed to add the following (I may implement these at a later date):
* Add a 10 second timer to make the game have rounds of 10s each
* Make the centre joystick (Select) button start a new round
* Keep a list of the highest scores

### Material that helped
* [https://github.com/waveshare/LCD-show GitHub for the Waveshare LCD]
* [https://thepihut.com/blogs/raspberry-pi-tutorials/advanced-text-with-micropython-on-raspberry-pi-pico-displays Writing text to the WaveShare LCD]
