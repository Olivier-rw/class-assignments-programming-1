# Olivier Nshimiyimana

from aluLib import *

# I'm providing you with a general structure, but feel free to remove ALL
# OF IT and do it your way

CARD_WIDTH = 100
CARD_HEIGHT = 145
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

# List of cards
cards = ['A', 'A', 'K', '2', '2', 'K']

# List containing states of our cards
state = [0, 0, 0, 0, 0, 0, 0, 0]


X_STR = []
X_END = []
Y_STR = []
Y_END = []


first = 0
second = 0

NO_OF_CLICKS = 0


# This function will draw the cards
def draw_cards():
    disable_stroke()
    global X_STR, X_END, Y_STR, Y_END
    # remove the line below once you start working on this
    i = 0
    dist_x = WINDOW_WIDTH // 21
    dist_y = WINDOW_HEIGHT // 3

    while i < len(cards):

        img_loader = 'assets/' + cards[i] + '.png'

        draw_image(load_image(img_loader), dist_x, dist_y)

        # These 4 lists will store the coordinates of where we drew our cards
        X_STR.append(int(dist_x))
        X_END.append(int(dist_x + CARD_WIDTH))
        Y_STR.append(int(dist_y))
        Y_END.append(int(dist_y + CARD_HEIGHT))

        dist_x += WINDOW_WIDTH / 7

        i += 1

    return

# This function decides what should happen given the state of the cards
# Are there any cards we should remove? any cards we should hide?
# You won't need this until milestone 3


def check_card_state():
    i = 0
    dist_x = WINDOW_WIDTH // 21
    dist_y = WINDOW_HEIGHT // 3

    while i < len(cards):

        if state[i] == 0:
            set_fill_color(0.18, 0.54, 0.34)
            draw_rectangle(dist_x, dist_y, CARD_WIDTH + 1, CARD_HEIGHT)

        if state[i] == 2:

            set_fill_color(0.2, 0.2, 0.2)
            draw_rectangle(dist_x, dist_y, CARD_WIDTH + 1, CARD_HEIGHT)

        dist_x += WINDOW_WIDTH / 7
        i += 1


# Check the mouse input, and flip relevant cards
def check_mouse_input():
    global state, NO_OF_CLICKS, first, second

    i = 0
    j = 0

    while i < len(cards):

        if mouse_x() in range(X_STR[i], X_END[i]) and mouse_y() in range(Y_STR[i], Y_END[i]):
            if is_mouse_pressed():

                if state[i] == 0:
                    state[i] = 1

                    NO_OF_CLICKS += 1

        i += 1

    if NO_OF_CLICKS == 2:
        first = state.index(1)
        j = first
        while j < len(cards):
            if state[j] == 1:
                second = j
            j += 1

        if cards[second] == cards[first]:
            state[second] = 2
            state[first] = 2
        else:
            state[second] = 0
            state[first] = 0

        NO_OF_CLICKS = 0


def main():
    # As mentioned, this is just a suggested structure. Feel free to change this if you prefer
    set_clear_color(0.2, 0.2, 0.2)
    clear()
    draw_cards()
    check_card_state()
    check_mouse_input()


# Keep a low framerate to your submission. 10 worked well for me, but experiment on your own.
start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=10)
