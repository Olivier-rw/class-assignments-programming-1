from person import *
from disease import *
from aluLib import *
from random import *

# Constants for drawing
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 500
BAR_HEIGHT = 80
BAR_Y_COORD = 300
LEGEND_SIZE = 30
LEGEND_OFFSET = 250
LEGEND_TEXT_OFFSET = 210

# Setting up the population
# The values here are provided as a demo to the visualization, you will want to replace them by
# user input in your final solution.
original_population_size = int(input('Enter the number of total population'))  # This should start coming from user input.
immune_count = int(input('Enter the number of immune population')) # This should start coming from user input.
infected_count = int(input('Enter the number of infected population')) # This should start coming from user input.
deceased_count = int(input('Enter the number of deceased population'))  # This should start at 0 in your final result.
susceptible_count = original_population_size - immune_count - infected_count - deceased_count

infection_rate = int(input('Enter the infection rate:'))
recovery_rate = int(input('Enter the recovery rate:'))
lethality_rate = int(input('Enter the mortality rate:'))

# Keep the initial number of infected people
initial_infected = infected_count

# total_population variable to be recorded in a csv file
total_population = infected_count + immune_count + susceptible_count

CONTACT_NUMBER = 10  # Constant for how many people each Person meets a day.

# Keep track of how many days it's been
day_count = 0
target_duration = 100  # This should start coming from user input.

# You will have to update this list with the right kind of Person objects.
population = []

# Create our csv file with the titles
file = open('Report.csv', 'w')
file.writelines('Total population'+','+'Susceptible'+','+'Infected'+','+'Immune'+','+'Dead')

# Creating a disease object with the right parameters
disease_object = Disease(infection_rate, recovery_rate, lethality_rate)


def assign_population():
    for person in range(infected_count):
        population.append(1)
    for person in range(susceptible_count):
        population.append(0)
    for person in range(immune_count):
        population.append(2)

    shuffle(population)


# You won't need to change this function, it will display a visual summary of each population
def draw_status():
    clear()
    set_font_size(24)
    draw_text("Total population is: " + str(immune_count + infected_count + susceptible_count), 10, 30)

    draw_text("Simulation has been running for " + str(day_count) + " days", 10, 75)

    # Figure out how large we should make each population
    susceptible_width = (susceptible_count / original_population_size) * WINDOW_WIDTH
    infected_width = (infected_count / original_population_size) * WINDOW_WIDTH
    immune_width = (immune_count / original_population_size) * WINDOW_WIDTH
    dead_width = (deceased_count / original_population_size) * WINDOW_WIDTH

    # Start with susceptible
    set_fill_color(0, 1, 0)
    # Draw the bar
    if susceptible_count != 0:
        draw_rectangle(0, BAR_Y_COORD, susceptible_width, BAR_HEIGHT)
    # Draw the legend:
    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 30, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Susceptible', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 60)

    # Draw infected
    set_fill_color(1, 0, 0)
    if infected_count != 0:
        draw_rectangle(susceptible_width, BAR_Y_COORD, infected_width, BAR_HEIGHT)

    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 75, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Infected', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 105)

    # Draw immune
    set_fill_color(0, 0, 1)
    if immune_count != 0:
        draw_rectangle(susceptible_width + infected_width, BAR_Y_COORD, immune_width, BAR_HEIGHT)

    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 120, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Immune', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 150)

    # Draw diseased
    set_fill_color(0.2, 0.7, 0.7)
    if deceased_count != 0:
        draw_rectangle(susceptible_width + infected_width + immune_width, BAR_Y_COORD, dead_width, BAR_HEIGHT)

    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 165, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Dead', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 195)


def check_the_infected():
    # Go over your population and check on each infected person
    # Did they get better today? Did they pass away?

    # We will be editing these global variables in this function
    global population, infected_count, immune_count, deceased_count, total_population

    # Go over each person in our population
    for person in range(len(population)):

        # Creating a person object using Person class
        person_object = Person(population[person], disease_object)

        # If is_infected_recovered() returns a true value
        if person_object.is_infected_recovered():

            # We move the person from infected to immune population
            population[person] = 2
            infected_count -= 1
            immune_count += 1

        # If is_infected_dead() returns a true value
        if person_object.is_infected_dead():

            # We move the person from infected and total population to dead
            population[person] = 3
            infected_count -= 1
            total_population -= 1
            deceased_count += 1


def check_the_susceptible():
    # Go over your population and check on each susceptible person
    # Who did they meet today? Did they get infected from anyone?

    # We will be editing these global variables in this function
    global population, susceptible_count, infected_count

    # Go over each person in our population
    for person in range(len(population)):

        # Creating a person object using Person class
        person_object = Person(population[person], disease_object)

        # Go through some number(CONTACT_NUMBER) of people to meet a day
        for contact in range(CONTACT_NUMBER):

            # Generate a random index from our total population
            random_person_index = randint(0, len(population)-1)

            # If is_susceptible_infected returns a true value given a person at a random index
            if person_object.is_susceptible_infected(population[random_person_index]):

                # We move the person from susceptible to infected population
                population[person] = 1
                susceptible_count -= 1
                infected_count += 1

                # The loop breaks when our person get infected by anyone from the people he/she met
                break

    population = []


def write_csv():
    # Each cycle, you should write down the values of each population into a csv file, so that we can export our data
    # to a spreadsheet and share it with others.

    # Writing a csv file
    file.writelines('\n' + str(total_population) + ',' + str(susceptible_count) + ',' + str(infected_count) + ',' +
                    str(immune_count) + ',' + str(deceased_count))


def generate_final_report():
    # Once your simulation is done, you must print out the following:
    # What percentage of the population survived?
    # What is R0?
    # Does that mean we've suffered an epidemic?

    print('The percentage of people who survived is :',
          str(round((susceptible_count + immune_count) / original_population_size) * 100))


def compute_r0():

    if initial_infected >= 5:
        r0 = 'R0:' + str(((infected_count + deceased_count) - initial_infected) / initial_infected)
        if ((infected_count + deceased_count) - initial_infected) / initial_infected > 1:
            print("We are dealing with epidermic")
    else:
        r0 = "Can't compute R0"
    print(r0)




def main():

    global day_count

    assign_population()

    # Draws the visual representation
    draw_status()

    # Loop over the infected population to determine if they could recover or pass away
    check_the_infected()

    # Loop over the healthy population to determine if they can catch the disease
    check_the_susceptible()

    # Update our output CSV
    write_csv()

    day_count += 1

    # End the simulation once we reach the set target.
    if day_count == 20:
        compute_r0()

    if day_count == target_duration:
        generate_final_report()

        # Closing our file once we reach the set target
        file.close()

        cs1_quit()


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=1)
