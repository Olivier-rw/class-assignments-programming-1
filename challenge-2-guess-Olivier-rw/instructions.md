

Challenge 2: Guessing games
=======================

Our objective remains: developing the skill of **breaking down complex tasks into smaller, manageable chunks**.

"How did the ant eat the elephant? One bite at a time"


To support you in this, I've outlined a work plan that you can find after the game description, I encourage you to read 
through the milestones, and do them a step at a time

Note that I've provided a basic structure for the code in guess.py, feel free to build on top of that, or start completely 
from scratch. The choice is yours.

The game
--------
You are to display 6 cards in one line, hidden from sight. When a user clicks on a card, the card is revealed. The user can click on
another card, at which points one of two things happen:
- If the cards don't have the same value, they go back to being face down.
- If the cards have the same value, they go "out of play", their spots on the screen remain, but we can't interact with 
them anymore.

That is the basic experience of the game. Note the following:
- There should **never** be more than 2 cards revealed to the user
- 


Checkpoint 1 : drawing the cards
--------------------------------

You will notice that there is an assets folder included in this repository. In it, you will find images for cards.
To draw a card, follow the instructions below:

``` {.sourceCode .python}
from aluLib import *
# The variable below will store information about how to draw the Ace
img = load_image("assets/A.png")

  ## somewhere in a drawing function called by start_graphics:
  ## This will put the top left corner of the image at position 100, 150
  draw_image(img, 100, 150)
```

I store my cards in a list, for example:
```{.sourceCode .python}
cards = ['A', '2', 'A', 'K', '2', 'K']
```

When I want to draw the cards, I loop over the list, and for each String in it, I load the corresponding image, and then 
call draw_image as in the example above.

For this first checkpoint, create a draw_cards() function. It will go through our list of cards, and draw the images 
corresponding to each.

Note that we want our 6 cards in 1 line, with some space between each. You will have to think a bit about what the 
coordinates should be. Note that the cards are 100 pixels wide, and 145 pixels high
 
Once you can draw the 6 cards, you are ready for the next milestone. 

Checkpoint 2: Interacting with the cards
----------------------------------------

Next step is figuring out how to interact with the cards. In the final game, we will want to "flip" cards by clicking on
them. For now, create a function that does the following:
- Check if the mouse is clicked
- If it is, keep track of which point was clicked
- Now we need to find out if that point is within ***any*** of the 6 cards you've drawn: Re-use the same logic you used 
for the card position to check if the x position and y position of the clicked point is in the right range.
- If you are indeed clicking on one of the cards, print the index and value of that card.

Obviously printing the values of the card is not the point of this, but this establishes you can interact with the cards

Checkpoint 3: The state of the game
-----------------------------------

Next incremental step: So far we've only dealt with the images of the cards, but to get the game we want we 
need to:
- Draw the back of the cards
- Remove cards once they find a match.

In other words, each card can be in one of 3 states:
- Hidden
- Shown face up
- Removed

I created a list to keep track of the state of my cards - the idea is that state[i] stores the state of cards[i], telling
me how I should draw them. In my system:
- 0 indicates the card should be hidden.
- 1 indicates the card should be shown face up.
- 2 indicates the card is out of the game.
So for example:
```buildoutcfg
state = [0,0,0,0,0,0] # all cards are hidden
state = [1,0,1,0,0,0] # all cards are hidden except the first and third

state = [2,2,2,2,0,1] # The first 4 cards are out of the game
# The fifth card is hidden
# The last card is face up
```

Feel free to use different numbers or a different system, just make sure to comment it.
Now as you go through the cards to draw them, you should check the state first:
- If state is 0, hide the card (In my example, I just draw a blue rectangle as big as the card)
- If state is 1, show the card (That's what you are already doing if you finished milestone 1)
- If state is 2, we should show a blank spot instead, I'll let you figure out this one.

Make sure your draw_cards function now takes state into consideration, use the examples above and see if you get the 
right results. You are almost there!

Checkpoint 4: Finishing the game
-----------------------------------
At this point, we can draw different situations by changing the state list, but the state should really change based on 
our clicks. It might be good to think about the following questions and tips:
- Cards start in state 0 (face down), clicking them should flip them. 
- Remember though: Only 2 cards can be face up!
- Once a card is in state 1 (face up), what state can it go in? under what conditions?
- Once a card is in state 2 (removed), can it change state?


Design and style
----------------

Your program should be understandable with minimum possible effort.  The logic
should be as straightforward as possible.  The beauty of a program lies in its design and in its style.

### Functions

Don't be afraid to write functions that help your program out. I
mentioned a couple earlier. But you should feel free to write
more. Your functions should all be near the top of your code, not mixed in with code at the global level. This makes it easy to quickly see what functions you will be using.


### Documentation

You should include comments that tell the human reader what he or she needs
to understand in order to make sense of your program.  You should also choose descriptive variable and function names.
Meaningless names are bad, and misleading names are worse.

Grading
-------

Correctness:

-   Card are revealed when clicking them
-   Only 2 cards can be face up at a time
-   Once a pair is found, they are removed from the game. Other cards stay in the same location
-   If the 2 face up cards are different, flip them back face down

Coding proficiency:

- You correctly uses functions to organize the code's logic
- Drawing is done as per the standards of aluLib.
- Any logic in the code is handled clearly and elegantly. If statements are used appropriately.

Style:

-   Clear design and organization.
-   Good variable names, function names, and comments.
-   Functions where appropriate and not where inappropriate.

## Honor Code

Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 


What to turn in
---------------

Make sure your git repository contains the following:
- A single python file for the guess game.
- Optionally: a second python file for the extra credit version of the game
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occurred.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 


Extra Credit
------------

You can add all sorts of features to the game for extra
credit. Make sure, however, before you charge off and do extra credit
that you have the basic game working correctly, that you've designed it
as cleanly as possible, and that you've documented it well. Remember, the extra credit points don't really count for anything.

Also, **before you start any extra credit, save your basic submission source
code, and submit that as your main submission. Also take a screenshot
for submission before working on extra credit. Start a new Python file
for any extra credit.**  If you do pursue extra credit, include a text
file in your submission that tells us what extra-credit features you've
included.

You can add plenty of extra-credit features. Here is a list of ideas to
get you thinking, but by all means let your imagination go.

-  Add multiple rows of cards
-  Allow the user to restart a game, shuffling the cards so they are in different places
-  Keep track of how many moves it took to beat the game.
-  Hard mode: Finding pairs actually consolidates the list, moving cards closer together
