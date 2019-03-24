# Olivier Nshimiyimana

# Prompting user to provide filename
filename = input('Enter the name of your file (with its extension) :\n')

# Let's open the file given
f = open(filename, 'r')

# Create a list 'content' to hold the lines in our file
content = f.readlines()

# Close our file
f.close()

# Making filename from user input name
new_filename = filename + '.sum'

# Create a file with that name
new_file = open(new_filename, 'x')

# Write first paragraph directly to the new file
new_file.write(content[0] + '\n')

# Loop through the body part of the text
for paragraph in range(1, len(content)-1):

    # Skip the blank lines
    if content[paragraph] != '\n':

        # We split our paragraph into sentences
        sentence = content[paragraph].split('. ')

        # We write the first and the last sentence of the paragraph.
        new_file.write(sentence[0] + '. ' + sentence[-1] + '\n')


# Add the last paragraph of the text
new_file.write(content[-1])

# Close our summary file
new_file.close()
