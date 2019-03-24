

Short assignment 5: Analyzing our class
=======================
This is our first analytics problem. You've been provided with student_country_data.csv, a text file which follows this 
pattern: each line looks like

Student name, Country name, Cohort number.

The idea is to go through the file, and answer a few interesting questions about the data at hand, leveraging dictionaries 


Requirements
------------

Your program should go through the file, and create dictionaries that will help you achieve the following 2 functionalities:

- Print the name and country of every student who is the _only_ person from their country. For example, Musa Selekie 
Kanneh is the only person from Liberia, so his name and country should show up. 

- Ask the user for the name of a country, then print out how many students from that country are in cohort 1, then how 
many are in cohort 2.

Hints
-------------
- It should not be possible for me to make your code crash, so make sure to be consistent with using
dictionary.get(key) instead of directly using dictionary[key]
- You shouldn't be outputing anything until you have gone through the whole file and created your dictionaries.
- Remember the split method from the previous short assignment
- After you split your lines, I recommend you use the **trim()** method on each String you get. Trim means removing any 
whitespace at the beginning or end of the String, for example:
     - let **_test='  stuff\n'_**, test.trim() will return **_'stuff'_**, removing the space from the beginning, and the 
     newline symbol at the end.

Checkpoint 1 : Listing out sole representatives
---------------------------------------------
For this checkpoint cohort information does not matter, but we definitely want to connect the names of students with the 
countries they are from. Given that many students can come from the same country, I suggest creating a dictionary that 
works as follows:
- The key to the dictionary will be the name of the country.
- The value of the dictionary will be a list of student names. Those should be the students from said country.
- When you read a line from the file and find a brand new country you haven't seen before, insert the country as a key, 
with the corresponding value being a list of 1 element, the name of the student from that country.
- When you read a line from the file and find a country that is already in your dictionary, then you need to make sure you
don't overwrite the previous name! instead, append the new name to the list that already exists.

Once you create this dictionary, you only have to loop through and find the countries that only have a list of 1.


Checkpoint 2: Getting country information per cohort
----------------------------------------
Now we need to keep track of cohort information as well. This can be done in a few different ways, the path I took was to
create 2 dictionaries instead of 1. Based on the cohort I find in each line of the file, I decide which dictionary to update.

Once the dictonaries are created, then I ask the user for a country, and look it up in both. You have options on how to approach this:
- You can create dictionaries that map the country name to a number
- You can create dictionaries similar to checkpoint 1, where the country name maps to a list of students

Either way, you should be able to figure out how many students from a given country are in each cohort.

## Honor Code

Please make sure that you fully understand the Academic Honor System, and reach out if you need any clarifications. 


What to turn in
---------------

Make sure your git repository contains the following:
- A single python file for your submission.
- Optionally: a second python file for the extra credit version of the game
- A text file describing the following:
    - An acknowledgement of upholding the honor code, or information if any breach occurred.
    - Any extra credits or additional features you attempted.
    - Any notes you want to bring to the attention of the grader. 


Extra Credit
------------

You can add all sorts of features to the submission for extra
credit. Make sure, however, before you charge off and do extra credit
that you have the basic game working correctly, that you've designed it
as cleanly as possible, and that you've documented it well. Remember, the extra credit points don't really count for anything.

Also, **before you start any extra credit, save your basic submission source
code, and submit that as your main submission. Also take a screenshot
for submission before working on extra credit. Start a new Python file
for any extra credit.**  If you do pursue extra credit, include a text
file in your submission that tells us what extra-credit features you've
included.