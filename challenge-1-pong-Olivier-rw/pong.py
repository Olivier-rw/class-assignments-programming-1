# Olivier Nshimiyimana

from aluLib import*

# Width and the height of our gaming window
window_W = 800
window_H = 600

# Middle point of the gaming window
CENTER_X = window_W / 2
CENTER_Y = window_H / 2

# Width and the height of our paddles
paddle_W = window_W / 50
paddle_H = window_H / 7.5

# Starting Y-coordinates for left and right paddle respectively
paddle_L = 0
paddle_R = window_H - paddle_H

# Incrementation of the paddle Y-coordinates
PADDLE_INCRE = 5

# Interval from vertical and horizontal walls to our paddles
INTERVAL_X = paddle_W * 2
INTERVAL_Y = window_H - paddle_H

# Initial X and Y coordinates for our ball
ball_X = CENTER_X
ball_Y = CENTER_Y

# Ball radius
ball_R = window_W // 75

# Incrementation values for X and Y coordinates of our ball
incre_X = paddle_W / 8
incre_Y = paddle_W / 8

# Boolean variable to track when user press space bar for the first time
START = False


# The first function draws the left and the right paddle
def draw_paddles():
    # Disabling outline
    disable_stroke()

    # Set the color of two paddles to 'white'
    set_fill_color(1, 1, 1)

    # Left paddle
    draw_rectangle(paddle_W, paddle_L, paddle_W, paddle_H)

    # Right paddle
    draw_rectangle(window_W - INTERVAL_X, paddle_R, paddle_W, paddle_H)

    # Middle line separating two blocks of the window
    draw_rectangle(CENTER_X - 2, 0, 4, window_H)


# This function controls the movements of the paddles
def paddles_moves():
    # Starting Y coordinates for both of our paddles
    # This function use them to move our paddles up and down
    global paddle_L, paddle_R

    # Pressing 'a', decreases Y coordinates of the left paddle, and this make it move closer to the top
    if is_key_pressed("a") and paddle_L > 0:    # It should decrease only when it is greater than 0
        paddle_L -= PADDLE_INCRE

    # Pressing 'z', increases Y coordinates of the left paddle, and this make it move closer to the bottom
    if is_key_pressed("z") and paddle_L < INTERVAL_Y:   # It should increase only when it is less than window height
        paddle_L += PADDLE_INCRE

    # Pressing 'k', decreases Y coordinates of the right paddle, and this make it move closer to the top
    if is_key_pressed("k") and paddle_R > 0:    # It should decrease only when it is greater than 0
        paddle_R -= PADDLE_INCRE

    # Pressing 'm', increases Y coordinates of the right paddle, and this make it move closer to the bottom
    if is_key_pressed("m") and paddle_R < INTERVAL_Y:   # It should increase only when it is less than window height
        paddle_R += PADDLE_INCRE


# This function draws our ball in form of a circle
def draw_ball():

    set_fill_color(0.1, 0.1, 0.1)

    # We are drawing using global variables defined above
    draw_circle(ball_X, ball_Y, ball_R)


# This function helps us to know when the ball hits the right paddle
def ball_tracker_r():

    edge_x_l = ball_X + ball_R      # The left X edge point of the ball, after adding the radius
    edge_y_l = ball_Y + ball_R      # The bottom Y edge point of the ball, after adding the radius
    edge_y_r = ball_Y - ball_R      # The top Y edge point of the ball, after removing the radius

    """ It should return true when the X coordinate of the ball is equal to the X- axis of the left face of the paddle, 
    and the Y coordinate is in the range between the top and down Y coordinates of the paddle """

    return edge_x_l == window_W - INTERVAL_X and paddle_R <= edge_y_l and edge_y_r <= (paddle_R + paddle_H)


# This function helps us to know when the ball hits the right paddle
def ball_tracker_l():
    edge_x_r = ball_X - ball_R      # The right X edge point of the ball, after removing the radius
    edge_y_l = ball_Y + ball_R      # The bottom Y edge point of the ball, after adding the radius
    edge_y_r = ball_Y - ball_R      # The top Y edge point of the ball, after removing the radius

    """ It should return true when the X coordinate of the ball is equal to the X- axis of the right face of the paddle, 
        and the Y coordinate is in the range between the top and down Y coordinates of the paddle """

    return edge_x_r == INTERVAL_X and paddle_L <= edge_y_l and edge_y_r <= paddle_L + paddle_H


# This function helps us to know when the ball hits the top and bottom sides of our window
def bounces_y_axis():
    edge_y_l = ball_Y + ball_R      # The bottom Y edge point of the ball, after adding the radius
    edge_y_r = ball_Y - ball_R      # The top Y edge point of the ball, after removing the radius

    # Return true if Y coordinate of the ball is between the Y coordinates of the top and the bottom of the window
    return 0 < edge_y_r and edge_y_l < window_H


# This function makes our ball move
def ball_moves():
    # To move the ball we'll be editing multiple global variables
    global ball_X, ball_Y, incre_X, incre_Y, START

    # This incrementation moves the ball in both X an Y directions
    ball_X += incre_X
    ball_Y += incre_Y

    # If 'bounces_y_axis()' returns False, Y axis of the ball changes direction
    if not bounces_y_axis():
        incre_Y *= -1

    # If 'ball_tracker_r()' returns True, X axis of the ball changes direction
    if ball_tracker_r():
        incre_X *= -1

    # If 'ball_tracker_l()' returns True, X axis of the ball changes direction
    if ball_tracker_l():
        incre_X *= -1

    # If X coordinate of the ball is equal to 0 or the window width the game should restart
    if ball_X == window_W or ball_X == 0:
        ball_X = CENTER_X
        ball_Y = CENTER_Y
        START = False       # The 'START' value also should be reset


# This controls what happens when Space bar is pressed
def space_bar():

    global START, ball_X, ball_Y

    # It should change the value of 'START' to 'True'
    if is_key_pressed(" "):
        START = True

        # It should also reset the ball coordinates to the initial position
        ball_X = CENTER_X
        ball_Y = CENTER_Y


# This function cancel all the processes and quit our game
def game_quit():
    # It should quit when user presses 'q'
    if is_key_pressed("q"):
        cs1_quit()


# The main function which call all other functions we used above
def main():
    set_clear_color(0.18, 0.54, 0.34)
    clear()
    draw_paddles()
    paddles_moves()
    draw_ball()
    space_bar()
    game_quit()
    ball_tracker_l()
    ball_tracker_r()

    # The move function executes only when 'START' is True
    if START:
        ball_moves()


# Start the gaming window
start_graphics(main, width=window_W, height=window_H, framerate=125)
