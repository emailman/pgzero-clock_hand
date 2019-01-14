from math import pi, sin, cos
from time import sleep

import pgzrun

"""
Show the second hand of a clock advancing one tic each second,
a minute hand advancing one tic each minute, and an hour hand
advancing 1 tic every other minute.

Display the number of hours, minutes and seconds as text in the window.
"""

# Screen size
WIDTH = 400
HEIGHT = 400

# Global variables
second_hand_length = 150
second_hand_color = 'red'

minute_hand_length = 150
minute_hand_color = 'blue'

hour_hand_length = 125
hour_hand_color = 'green'

center = (0, 0)

end_points_tic = []
end_points_hour = []

num_of_tics = None
num_of_hour_tics = None

second_counter = 0  # 0 - 59
minute_counter = 0  # 0 - 59
hour_counter = 0  # 0 - 11


def offset(point):
    # Offset (0, 0) to the center of the screen
    return point[0] + WIDTH / 2, -point[1] + HEIGHT / 2


# Start the hands at the 12 o'clock position
# Divide the circle into 60 pieces (360 / 6)
# Make sure the hands goes clockwise
for angle in range(90, -270, -6):
    # A little trig goes a long way to find the end point
    x = cos(angle * pi / 180) * second_hand_length
    y = sin(angle * pi / 180) * second_hand_length
    print('{:4d} degrees: x = {:6.2f}  y= {:6.2f}'
          .format(angle, x, y))

    # Add the end point coordinate to the list
    end_point = (x, y)
    end_points_tic.append(end_point)

num_of_tics = len(end_points_tic)
print(num_of_tics)

# Divide the circle into 360 pieces
# for the hour hand
for angle in range(90, -270, -1):
    # A little trig goes a long way to find the end point
    x = cos(angle * pi / 180) * hour_hand_length
    y = sin(angle * pi / 180) * hour_hand_length
    print('{:4d} degrees: x = {:6.2f}  y= {:6.2f}'
          .format(angle, x, y))

    # Add the end point coordinate to the list
    end_point = (x, y)
    end_points_hour.append(end_point)

num_of_hour_tics = len(end_points_hour)
print(num_of_hour_tics)


def draw():
    # Draw a white hub
    screen.draw.filled_circle(offset(center), 10, 'white')


def update():
    global second_counter, minute_counter, hour_counter

    screen.clear()

    # Draw the second hand with a dot at the end of it
    screen.draw.line(offset(center),
                     offset(end_points_tic[second_counter]), second_hand_color)
    screen.draw.filled_circle(offset(end_points_tic[second_counter]),
                              7, second_hand_color)

    # Draw the minute hand
    screen.draw.line(offset(center),
                     offset(end_points_tic[minute_counter]), minute_hand_color)

    # Draw the hour hand
    screen.draw.line(offset(center),
                     offset(end_points_hour[hour_counter]), hour_hand_color)

    # Update the display of the number of hours, minutes and seconds
    time_display = '{:02d} : {:02d} : {:02d}'.format(hour_counter // 30, minute_counter, second_counter)
    screen.draw.text(time_display, (WIDTH / 2 - 40, 10))

    # Tic
    second_counter += 1

    # Handle the second, minute and hour counters

    # Time to wrap the second counter and
    # advance the minute and hour counter?
    if second_counter == num_of_tics:
        second_counter = 0
        minute_counter += 1
        if minute_counter % 2 == 0:
            hour_counter += 1
            # Time to wrap the hour counter?
            if hour_counter == num_of_hour_tics:
                hour_counter = 0

        # Time to wrap the minuter counter?
        if minute_counter == num_of_tics:
            minute_counter = 0

    # Execute once per second
    sleep(.1)


pgzrun.go()
