# Olivier Nshimiyimana

from aluLib import *

window_width = 800
window_height = 800

# Global variable for the size of the brush
brush = 5


# This function checks key presses, and determine what color we draw with next
def determine_color():

    if is_key_pressed("r"):     # Pressing 'r' will set drawing color to red
        set_fill_color(1, 0, 0)

    elif is_key_pressed("g"):   # Pressing 'g' will set drawing color to green
        set_fill_color(0, 1, 0)

    elif is_key_pressed("b"):   # Pressing 'b' will set drawing color to blue
        set_fill_color(0, 0, 1)

    elif is_key_pressed("y"):   # Pressing 'y' will set drawing color to yellow
        set_fill_color(1, 1, 0)

    elif is_key_pressed("a"):   # Pressing 'a' will set drawing color to black
        set_fill_color(0, 0, 0)

    # Pressing 'e' will set drawing color to default background and this will works as an eraser
    elif is_key_pressed("e"):
        set_fill_color(0.94, 0.94, 0.94)

    # This line sets the clear color to the default background color.
    set_clear_color(0.94, 0.94, 0.94)


# This function checks key presses, and determine how big the brush should be
def determine_brush_size():

    # We are using a variable we defined globally 'brush'
    global brush

    if is_key_pressed("+") and brush < 50:      # Radius for our drawing circle should not exceed 50
        brush += 1

    elif is_key_pressed("-") and brush > 1:     # Radius for our drawing circle should not be below 1
        brush -= 1


# This function draws the brush when necessary
def draw():

    draw_circle(mouse_x(), mouse_y(), brush)


def main():
    # This will let our user reset the screen by pressing 'x'
    if is_key_pressed("x"):
        clear()

    # This makes sure the circles we draw don't have a border
    disable_stroke()

    # Decide what color to draw with, or alternatively erase.
    determine_color()

    # Decide how big the brush should be
    determine_brush_size()

    # Draw if you should be drawing
    if is_mouse_pressed():
        draw()


start_graphics(main, width=window_width, height=window_height, framerate=100)
