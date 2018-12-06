from math import pi, sin, cos
from time import sleep

import pgzrun

"""
Show the second hand of a clock advancing one second
for each cycle of the program.
Display the number of seconds as text in the window.
"""

# Screen size
WIDTH = 400
HEIGHT = 400

# Global variables
hand_length = 150

end_points = []
num_of_points = None

counter = 0  # 0 - 59


def offset(point):
    # Offset (0, 0) to the center of the screen
    return point[0] + WIDTH / 2, -point[1] + HEIGHT / 2


# Start the hand at the 12 o'clock position
# Divide the circle into 60 pieces (360 / 6)
# Make sure the hand goes clockwise
for angle in range(90, -270, -6):
    # A little trig goes a long way
    x = cos(angle * pi / 180) * hand_length
    y = sin(angle * pi / 180) * hand_length
    print('{:4d} degrees: x = {:6.2f}  y= {:6.2f}'
          .format(angle, x, y))

    # Add the end point coordinate to the list
    end_point = x, y
    end_points.append(end_point)

num_of_points = len(end_points)
print(num_of_points)


def update():
    global counter
    screen.clear()

    # print(counter)

    screen.draw.line(offset((0, 0)),
                     offset(end_points[counter]), 'red')
    screen.draw.text(str(counter), (10, 10))

    counter += 1

    # Loop the counter back to the top of the list
    if counter == num_of_points:
        counter = 0

    # Slow it down to execute once per second
    sleep(1)


pgzrun.go()
