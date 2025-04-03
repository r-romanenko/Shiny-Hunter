# pip install keyboard
# should be quick

# pip install pyautogui
# should take longer, a couple minutes for me



from PIL import ImageGrab
import time
import keyboard
import pyautogui


def current_milli_time():
    return round(time.time() * 1000)



sleep_time = 3 # seconds to wait to allow user to switch to emulator
# seconds_to_wait = 3 # seconds to wait for user to be still (irrelevant)
confirm_key = 'x' # the key used to proceed with the program's steps
seconds_between_check = 5 # default value to mash x for before checking the pixel color

print(f"Sleeping for {sleep_time} seconds. Use this time to switch to Pokemon window.")
time.sleep(sleep_time)


start_time = current_milli_time()

print(f"Hover over the Reset button and press \'{confirm_key}\' ")

reset_x, reset_y = pyautogui.position()


keyboard.wait('x')
print(f"reset x: {reset_x}, reset y: {reset_y}")
reset_x, reset_y = pyautogui.position()


# then start counting for 5 seconds
start_time = current_milli_time()


print(f"Hover over Tepig and press \'{confirm_key}\'")
keyboard.wait('x')
x, y = pyautogui.position()

# one more thing I want to do is to have the user define how long to wait




print(f"Coordinates found! x: {x}, y: {y}")

# now we have the x and y of the pixel (or at least close) of what we want to look at
image = ImageGrab.grab()
color = image.getpixel((x, y))
print(f"color at {x}, {y} is: {color}")


# now I know where to check the color
# I need to now wait again for a certain amount of time, while mashing x
# then after that time is up, check if it's a shiny. If it is, break

start_time = current_milli_time()
regular_tepig_color = (189, 99, 49)
shiny_tepig_color = (189, 156, 49)

num_of_attempts = 0

while True:
    color = image.getpixel((x, y))
    if start_time + (seconds_between_check * 1000) < current_milli_time():
        start_time = current_milli_time()
        if color == regular_tepig_color:
            num_of_attempts += 1
            print(f"regular tepig #{num_of_attempts}")
        elif color == shiny_tepig_color:
            print(f"SHINY FOUND!!! ({num_of_attempts} tries)")
            break
        else:
            print(f"Uh oh! Not spotting any sort of tepig")
    
    # spam 'x'
    keyboard.press_and_release('x')
    time.sleep(0.1)


    
