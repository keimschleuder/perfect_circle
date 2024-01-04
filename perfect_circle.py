import pyautogui as gui
import math
import time

gui.PAUSE = 0.0000001   # The delay between two actions of pyautogui

gui.keyDown('win')
gui.press('1')      # Your browser window number
gui.keyUp('win')

center = {
    "X": 990, # X coordinate of the center
    "Y": 530  # Y coordinate of the center
}
radius = 400        # radius
num_points = 10000  # number of points

# ---------------
# Do not touch!

circle_points = []
for i in range(num_points):
    angle = 2 * math.pi * i / num_points
    x = center["X"] + radius * math.cos(angle)
    y = center["Y"] + radius * math.sin(angle)
    circle_points.append((int(x), int(y)))

time.sleep(1)

# Draw the circle
for _ in range(2):
    for point in circle_points:
        gui.moveTo(point[0], point[1])

# 99.9% accuracy