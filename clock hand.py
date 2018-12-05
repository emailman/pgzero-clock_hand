from math import pi, sin, cos
from time import sleep

import pgzrun

# Screen size
WIDTH = 400
HEIGHT = 400

# Global variables
hand_length = 150

end_points = []
num_of_points = None

counter = 0


def offset(point):
    # Offset (0, 0) to the center of the screen
    return point[0] + WIDTH / 2, -point[1] + HEIGHT / 2


# Start the hand at the top of the screen
# Divide the circle into 60 pieces (360 / 6)
# Make sure the hand goes clockwise
for i in range(90, -270, -6):
    # A little trig goes a long way
    x = cos(i * pi / 180) * hand_length
    y = sin(i * pi / 180) * hand_length
    print('{:4d} degrees: x = {:6.2f}  y= {:6.2f}'.format(i, x, y))

    end_point = x, y
    end_points.append(end_point)

num_of_points = len(end_points)
print(num_of_points)


def update():
    global counter
    screen.clear()

    # print(counter)

    screen.draw.line(offset((0, 0)), offset(end_points[counter]), 'red')
    screen.draw.text(str(counter), (10, 10))

    counter += 1

    if counter == num_of_points:
        counter = 0

    sleep(1)


pgzrun.go()
