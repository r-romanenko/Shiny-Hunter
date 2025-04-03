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



# wait 5 seconds
sleep_time = 3
seconds_to_wait = 3
seconds_between_check = 20

print(f"Sleeping for {sleep_time} seconds. Use this time to switch to Pokemon window.")
time.sleep(sleep_time)
# print("after sleep")


start_time = current_milli_time()


print(f"Checking if you're still for {seconds_to_wait} seconds.")
print(f"Hover over the Reset button for {seconds_to_wait} seconds.")

reset_x, reset_y = pyautogui.position()
# prev_reset_x, prev_reset_y = reset_x, reset_y

# print(f"Checking if you're still for {seconds_to_wait} seconds.")

# while start_time + (seconds_to_wait * 1000) > current_milli_time():
#     reset_x, reset_y = pyautogui.position()

#     if prev_reset_x != reset_x or prev_reset_y != reset_y:
#         # restart
#         start_time = current_milli_time()

#     prev_reset_x = reset_x
#     prev_reset_y = reset_y

keyboard.wait('x')
reset_x, reset_y = pyautogui.position()


# then start counting for 5 seconds
start_time = current_milli_time()


keyboard.wait('x')
x, y = pyautogui.position()
# prev_x, prev_y = x, y

print(f"Checking if you're still for {seconds_to_wait} seconds again.")
print(f"Hover over Tepig for {seconds_to_wait} seconds.")

# while start_time + (seconds_to_wait * 1000) > current_milli_time():
#     x, y = pyautogui.position()

#     if prev_x != x or prev_y != y:
#         # restart
#         start_time = current_milli_time()

#     prev_x = x
#     prev_y = y



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

num_of_regulars = 0

while True:
    color = image.getpixel((x, y))
    if start_time + (seconds_between_check * 1000) < current_milli_time():
        start_time = current_milli_time()
        if color == regular_tepig_color:
            print("regular tepig")
            num_of_regulars += 1
        elif color == shiny_tepig_color:
            print(f"SHINY FOUND!!! ({num_of_regulars} tries)")
            break
    
    # spam 'x'
    keyboard.press_and_release('x')
    time.sleep(0.1)


    
