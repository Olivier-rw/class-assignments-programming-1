class Disease:

    def __init__(self, infection, recovery, lethality):
        self.infection_rate = infection/100
        self.recovery_rate = recovery/100
        self.lethality_rate = lethality/100


