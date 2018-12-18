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

center = (0, 0)

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
    # A little trig goes a long way to find the end point
    x = cos(angle * pi / 180) * hand_length
    y = sin(angle * pi / 180) * hand_length
    print('{:4d} degrees: x = {:6.2f}  y= {:6.2f}'
          .format(angle, x, y))

    # Add the end point coordinate to the list
    end_point = (x, y)
    end_points.append(end_point)

num_of_points = len(end_points)


def draw():
    # Draw a white hub
    screen.draw.filled_circle(offset(center), 10, 'white')


def update():
    global counter
    screen.clear()

    # print(counter)

    # Draw a red line with a red dot at the end of it
    screen.draw.line(offset(center),
                     offset(end_points[counter]), 'red')
    screen.draw.filled_circle(offset(end_points[counter]),
                              7, 'red')

    # Update the display of the number of seconds
    screen.draw.text(str(counter), (WIDTH / 2 - 10, 10))

    counter += 1

    # Loop the counter back to the top of the list
    if counter == num_of_points:
        counter = 0

    # Slow it down to execute once per second
    sleep(.1)


pgzrun.go()
