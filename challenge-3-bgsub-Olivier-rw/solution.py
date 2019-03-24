# Olivier Nshimiyimana

from aluLib import *
from math import sqrt

# Load the foreground image given by user
FORE_IMG = load_image(input('Enter the name of the foreground file (with an extension):'))

# Load the old background as given by user
OLD_BG = load_image(input('Enter the name of the old background file (with an extension):'))

# Load the new background image given by user
NEW_BG = load_image(input('Enter the name of the new background file (with an extension):'))

# Set the width and height of the window according to those of foreground image given
WINDOW_W = (FORE_IMG.width()) * 3
WINDOW_H = FORE_IMG.height()

# A new copy of foreground image to overwrite with a new background
NEW_IMG = FORE_IMG.copy()
CHRO_IMG = FORE_IMG.copy()


# Function to replace old green pixels of the picture with new background pixels (Chromakey)
def replace_on_green():

    # This should loop through all the vertical pixels of the image
    for x_pixel in range(FORE_IMG.width()):

        # This should loop through all the horizontal pixels of the image
        for y_pixel in range(FORE_IMG.height()):

            # Let's get list rgb colors of foreground image at our current x & y
            fore_img_px = FORE_IMG.get_pixel(x_pixel, y_pixel)

            # Let's get list rgb colors of the new background image at our current x & y
            new_bg_px = NEW_BG.get_pixel(x_pixel, y_pixel)

            # Assign abbreviated names to their corresponding colors in the list
            r = fore_img_px[0]
            g = fore_img_px[1]
            b = fore_img_px[2]

            # If green dominates other colors, then the pixel is green enough
            if r < g and b < g:

                # We overwrite the current pixel with the matching pixel of the new background image
                CHRO_IMG.set_pixel(x_pixel, y_pixel, new_bg_px[0], new_bg_px[1], new_bg_px[2])

    # Draw the image
    draw_image(CHRO_IMG, 0, 0)

    # Text indicating which image we are drawing
    draw_text("<< Chromakey", FORE_IMG.width(), 50)

    # Save an edited image
    CHRO_IMG.save('output_chroma.jpg')


# This function will replace pixels from the old picture with the new background
def replace_on_old_bg():

    # This should loop through all the vertical pixels of the image
    for x_pixel in range(FORE_IMG.width()):

        # This should loop through all the horizontal pixels of the image
        for y_pixel in range(FORE_IMG.height()):

            # Let's get list rgb colors of the old image at our current x & y
            old_bg_px = OLD_BG.get_pixel(x_pixel, y_pixel)

            # Let's get list rgb colors of the new image at our current x & y
            new_image_px = NEW_IMG.get_pixel(x_pixel, y_pixel)

            # Let's get list rgb colors of new background image at our current x & y
            new_bg_px = NEW_BG.get_pixel(x_pixel, y_pixel)

            # This variable should hold the sum of three squares of color differences
            sum_of_distances = 0

            # We loop through all the our colors, adding the squares of their difference
            for a in range(len(old_bg_px)):
                sum_of_distances += (old_bg_px[a] - new_image_px[a]) ** 2

            # For the colors to be similar enough, they are ~0.29 apart in the values of their colors
            if 0.28 > sqrt(sum_of_distances):

                # We overwrite the current pixel with the matching pixel of the new background image
                NEW_IMG.set_pixel(x_pixel, y_pixel, new_bg_px[0], new_bg_px[1], new_bg_px[2])

    # Draw the image
    draw_image(NEW_IMG, 2 * FORE_IMG.width(), 0)

    # Text indicating which image we are drawing
    draw_text('Background Substitution >>', WINDOW_W/2, 500)

    # Save an edited image
    NEW_IMG.save('output_bgsub.jpg')


# Main function to call our two functions
def main():
    replace_on_green()
    replace_on_old_bg()


# Drawing the image
start_graphics(main, width=WINDOW_W, height=WINDOW_H)
