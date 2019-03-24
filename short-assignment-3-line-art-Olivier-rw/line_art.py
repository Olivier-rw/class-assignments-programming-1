# Olivier Nshimiyimana

from aluLib import *


# This function returns drawing coordinates according to line_count
def get_intermediate_values(start_value, end_value, line_count):
    i = 0
    # Initializing an empty list
    intermediate_values = []

    # Differentiation between our starting value and ending value
    line_len = end_value - start_value

    block_size = 0

    # Before we subtract one from our line_count, we need to make sure that it won't result n 0
    if line_count != 1:
        line_count -= 1

    # The loop to append values we are getting to our empty list
    while i <= line_count:

        # This will append the current block size to the start values
        intermediate_values.append(start_value + block_size)

        # This variable will track the previous value we appended to our list and increment it by the block size
        block_size += line_len / line_count

        i += 1

    # Returns a list of drawing coordinates
    return intermediate_values


# This function draws lines using the following parameters, with the line_count as number of lines.
def draw_line_art(x1a, y1a, x1b, y1b, x2a, y2a, x2b, y2b, line_count):

    i = 0

    # Line colors
    set_stroke_color(1, 0, 0)

    # Basic initial horizontal lines
    draw_line(x1a, y1a, x1b, y1b)
    draw_line(x2a, y2a, x2b, y2b)

    # List of coordinates on x1a, x1b, x2a, and y2b are returned respectively down here
    points_x1 = get_intermediate_values(x1b, x1a, line_count)
    points_y1 = get_intermediate_values(y1b, y1a, line_count)

    points_x2 = get_intermediate_values(x2b, x2a, line_count)
    points_y2 = get_intermediate_values(y2b, y2a, line_count)

    # This loop should run times the number of lines we passed by line_count
    while i < line_count:

        # This line draws a line from starting coordinates of line 1, and from ending coordinate of line 2
        draw_line(points_x1[i], points_y1[i], points_x2[len(points_x2) - 1 - i], points_y2[len(points_y2) - 1 - i])

        i += 1


def main():
    # This clear with black color wil make the screen always black
    set_clear_color(0, 0, 0)
    clear()

    # Start some line art, the first 4 parameters represent the coordinates of 2 points, which define a line
    # The next 4 coordinates also represent 2 points, which define a second line
    # The final parameter represents how many partial lines are desired
    draw_line_art(350, 50, 20, 80, 350, 300, 40, 220, 1)


start_graphics(main)