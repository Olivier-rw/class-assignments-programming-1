# SA 3 Instructions:

For this assignment, we are going to create some art leveraging lists.
The art we create is heavily inspired from string art: https://www.pinterest.com/falcoclan/string-art/

The idea is as follows: we will create a draw_line_art function that takes 9 parameters!
- The first 2 parameters indicate the starting point of line 1
- The next 2 parameters indicate the end point of line 1
- The next 2 parameters indicate the starting point of line 2
- The next 2 parameters indicate the end point of line 2
- Finally, the last parameter will tell us how many lines should connect the two primary lines

How do we figure out the intermediate lines? As you will notice from the example, there is a line going from the start 
of Line 1 to the end of Line 2, and vice versa.

We will always want to draw those lines. If the number of lines parameter given is 2, then those 2 are the only two 
lines we draw. Let's call them **edge lines.**

Now if we asked for 3 lines in total, we will the 2 edge lines as discussed above, the question is where
should the third line go? The answer is: From the middle of Line 1 to the middle of Line 2.

If we asked for 4 lines in total, we will the 2 edge lines, but how do we handle the extra 2 
lines? The answer is, we should divide Line 1 into thirds, that will give us 2 new points on Line 1

Similarly we divine Line 2 into thirds, giving use 2 new points on Line 2. We can connect these new points of both lines. 

In other words, find the point that is 1/3 of the way between the start of Line 1 and the end of Line 1, then the point 
that is 2/3 of the way there. Repeat that with Line 2, and that will give you the coordinates of the new lines

How do we find a point 1/3 of the way of Line 1? Well assuming we are going from _x1a, y1a_ (The start coordinates) 
to _x1b, y1b_ (The end coordinates), then the x coordinate of the point 1/3 of the way is _x1a + (1/3)*(x1b - x1a)_, 
or in other words, add 1/3 of the distance between x1a and x1b to the position of x1a

How do we handle y? Pretty much the same way we handle x. I'm sure you can figure it out.

We can generalize this to any fraction, not just 1/3, by the relevant fraction. Remember: We got 1/2 when we needed 3 
lines, and 1/3 when we needed 4. Notice a pattern?

You **MUST** write a function called _get_intermediate_values(start_value, end_value, line count)_. This function must 
return a List that contains the start value at the beginning, the intermediate values needed to create additional lines
up to line_count, then the end value.
 
For example if I call:
- _get_intermediate_values(200,250,2)_, it will  return **[200, 250]**
- _get_intermediate_values(100, 150, 3)_, it will return **[100, 125, 150]**
- _get_intermediate_values(100, 300, 4)_, it will return **[100, 166, 232,300]**

## Academic Honor System:
Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 
## What to turn in:
Make sure your git repository contains the following:
- A single python file for the line_art.
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occurred.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 
## Hints:
- The example you have is the result of calling:     draw_line_art(350, 50, 20, 80, 350, 300, 40, 220, 50)
- Don't focus on drawing the lines first, instead focus on finding the right points on Line 1 and Line 2. Try and just draw
a point at the coordinates you come up with in a color different from the lines, and make sure you like how things look.
- You should only need 1 while loop in this assignment. By this I don't mean that all your code is in a loop, but that I 
don't expect to see the word **while** more than once in your code. 
- Don't forget that you **must** use the function described above in your solution!

## Extra credit ideas:
Make sure to finish the key requirements first. If you do any major extra credit, include it in a separate python file.
These are optional additional challenges to entice your curiosity, and crank up the difficulty of the assignment. 
None of these actually count for extra marks.
- **Changing colors**: Can you make a gradient of color in your lines? Hint: The same way you compute what the next 
point should be, you can do some math to alter the colors following a set pattern.
- **Click control**: You could change the shape of your brush. What would drawing with triangles look like?
