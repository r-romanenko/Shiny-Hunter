# About
This is a quick python script I wrote up that helps you perform an automated shiny hunt of specifically Tepig in a Pokemon Black/White emulator (I wrote this based on the `DeSmuME` emulator).

# Setup
Type these two commands into the terminal:

```pip install keyboard``` (should take less than a minute)

```pip install pyautogui``` (might take a couple of minutes)

# Running it
After installing the required dependencies (```keyboard``` and ```pyautogui```), you should be able to now run the program. 

* Make sure that the emulator is running, and the reset state is the dialogue before choosing your starter.
* Proceed through the game until Tepig exits the pokeball and is in battle.
* Switch over to vscode (or whatever you are using to run this python script)
* Press run. The console should output instructions, but I will also write them here:
  
  * Hover over Tepig's head, so that the color of the pixel that your mouse is pointing to doesn't change throughout the animation, and press `x`
  * Hover over the ```Reset``` button and start mashing 'x' until Tepig has been sent into battle and has been on the ground for at least a second or two.
  * Mash `x` until you've sent out Tepig into battle. Confirm it isn't a shiny and press `Reset`
  * The program should take it from there
* To make the program stop mashing `x`, click into the terminal/console where you're running the program and press `ctrl c` (or `command c` if you're on MacOS)

