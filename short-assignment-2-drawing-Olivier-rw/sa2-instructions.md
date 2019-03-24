# SA 2 Instructions:

For this assignment, we are going to create a drawing application!

Our canvas should allow its user to draw in at least 3 different colors of your choice, erase drawings, 
and control the size of our "brush"

You will achieve this first via keyboard controls:
- Pressing *r* should allow you to draw in red
- Pressing *g* should allow you to draw in green
- Pressing *y* should allow you to draw in yellow
- Pressing *e* should allow you to erase things that have been drawn

Now, pressing a button only sets the color, or sets us up for erasing.
In order to actually draw or erase anything, the user must **click** on the screen.

The size of the circle drawn by the user is what we call the **"brush"**
 
You should be able to make your brush bigger or smaller using the *+* and *-* keys. You will probably need to have 
a global brush_radius parameter. This should change by 5 whenever you press + or -
## Academic Honor System:
Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 
## What to turn in:
Make sure your git repository contains the following:
- A single python file for the drawing_app.
- A screenshot of a drawing made with your app.
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occurred.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 
## Hints:
- The size of the circles you draw may change each time. This is a great scenario to use global variables
- Erasing sounds tricky at first, but it's the exact same as drawing. Think about your background color!
- Recall that the aluLib guide online can help you figure out more colors, and how to catch user input
- What should happen if someone keeps pressing + while already at the largest size? what about -? 
the built in python functions **min** and **max** can help with this.
## Extra credit ideas:
These are optional additional challenges to entice your curiosity, and crank up the difficulty of the assignment. 
None of these actually count for extra marks.
- **Reset**: Sometimes the art just doesn't work. Reset the canvas to its initial state.
- **Different brushes**: You could change the shape of your brush. What would drawing with triangles look like?
- **Steal something from Paint**: The floor is yours
