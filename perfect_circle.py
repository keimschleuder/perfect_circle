import pyautogui as gui
import math
import time

gui.PAUSE = 0.0000001

# move to browser
gui.keyDown('win')
gui.press('1')
gui.keyUp('win')

# generate circle with radius of 200 pixels around 990, 530
center = {
    "X": 990, 
    "Y": 530
}
radius = 400
num_points = 10000

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