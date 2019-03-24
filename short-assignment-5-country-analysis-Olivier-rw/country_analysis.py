# Olivier Nshimiyimana

# Let open, read, and close our file
file = open('student_country_data.csv', 'r')

content = file.readlines()

file.close()

# Initializing our country to students dictionaries
Cohort1 = {}
Cohort2 = {}

# This will holds country names with number of students from that country
C_to_S = {}

# Looping through our lines
for line in content:

    # Split content on comma
    words = line.split(',')

    # Check for the cohort number
    if words[2].strip() == '1':

        # Check if the country is already on our keys
        if words[1] in Cohort1.keys():

            # Create a temporary list containing students in a given country
            list = Cohort1[words[1]]

            # Append the list with new student
            list.append(words[0])

            # Assign the list to our country key
            Cohort1[words[1]] = list

        else:

            # Create a new list with student name
            list_of_students = [words[0]]

            # Assign the list to our country key
            Cohort1[words[1]] = list_of_students

    # Check for the cohort number
    if words[2].strip() == '2':

        # Check if the country is already on our keys
        if words[1] in Cohort2.keys():

            # Create a temporary list containing students in a given country
            list = Cohort2[words[1]]

            # Append the list with new student
            list.append(words[0])

            # Assign the list to our country key
            Cohort2[words[1]] = list

        # If the country is not available in our dictionary
        else:

            # Create a new list with student name
            list_of_students = [words[0]]

            # Assign the list to our country key
            Cohort2[words[1]] = list_of_students


country = input('Which country do you want information for?\n')

# Check if country exists in our dictionary
if country not in Cohort1 and country not in Cohort2:
    print('Country not found!')

# Loop through both cohorts to get input country
for counter in Cohort1:
    # This maps country with number of students from that country
    C_to_S[counter] = len(Cohort1[counter])

    if counter == country:
        print(country, 'has', len(Cohort1[counter]), 'student(s) in Cohort', 1)

for counter in Cohort2:
    if counter == country:
        print(country, 'has', len(Cohort2[counter]), 'student(s) in Cohort', 2)

    # This maps country with number of students from that country
    # or if country is already there, it adds the number to that of Cohort 1
    if counter in C_to_S.keys():
        C_to_S[counter] = C_to_S[counter] + len(Cohort2[counter])
    else:
        C_to_S[counter] = len(Cohort2[counter])

# Print sole representatives and their countries
print('\nBonus info: \nFollowing students are sole representatives from their respective countries\n')
for country in C_to_S:
    if C_to_S[country] == 1:

        # Now we know this country has one representative, this check from which cohort he is in
        if Cohort1.get(country) is None:
            print(Cohort2[country][0], 'from', country)

        else:
            print(Cohort1[country][0], 'from', country)

# Fin!
