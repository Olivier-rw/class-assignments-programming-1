# SA 3 Instructions:

For this assignment, we are going to create a tool that helps us summarize articles. This will be an opportunity to 
further practice modifying Strings, as well as interacting with files.

Here is the idea on how to create a summary:
- Keep the first paragraph from the original text as the first paragraph of the summary, regardless of how large it is.
- Keep the last paragraph from the original text as the last paragraph of the summary, regardless of how large it is.
- For any additional paragraph, keep only the **first and last sentence** of the paragraph in your summary.

This means that a 1 paragraph or 2 paragraph article will not actually get summarized. In those cases your output should
look just like your input.

Your code should ask the user to supply the name of a txt file (for example test.txt), and create a new file named 
test.txt.sum which will contain your summary. I've provided 2 pieces of text and the output I got from them as a reference

You can assume that all sentences in your article properly end with a **.**

You do not need to use an OOP approach, although that would count for extra credit.

## Academic Honor System:
Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 
## What to turn in:
Make sure your git repository contains the following:
- A single python file for the summarizer.
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occurred.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 
## Hints:
- For now, don't worry about other forms of punctuation like ! or ?. Consider a sentence to be any sequence of alphanumeric
text that ends with '**.**'
- Paragraphs are delimited by new lines.
- We have multiple ways of reading a file, you can use any of them as long as things work. Recall that:
    - file.read() returns a String with the complete String.
    - file.readLines() returns a List of Strings, each representing one line from the file.
    - More info on reading and writing here: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
- Be polite, close your files!

## Extra credit ideas:
Make sure to finish the key requirements first. If you do any major extra credit, include it in a separate python file.
These are optional additional challenges to entice your curiosity, and crank up the difficulty of the assignment. 
None of these actually count for extra marks.
- **OO implementation**: Can you create a summarizer object that tackles these tasks?
- **More accurate sentences**: In our base solution, we ignore sentences that end with ? or !, and only focus on '.'.
Fix that!
- **Alternative summarizing schemes**: Can you find better ways to summarize? Make sure to share plenty comments about it
- **Summary report**: How much was cut creating your summary? How many sentences? How many words?
