from random import *
population = []


class Person:

    def __init__(self, status, disease):
        self.status = status
        self.disease = disease

    def is_infected_recovered(self):
        if self.status == 1:
            if self.disease.recovery_rate >= random():
                return True

    def is_infected_dead(self):
        if self.status == 1:
            if self.disease.lethality_rate >= random():
                return True

    def is_susceptible_infected(self, another_person):
        if self.status == 0 and another_person == 1:

            if self.disease.infection_rate >= random():
                return True
