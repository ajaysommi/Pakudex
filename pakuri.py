
class Pakuri:
    def __init__(self, species):  # constructor for Pakuri class
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    def __lt__(self, next_species):
        return self.species < next_species.species

    def get_species(self):  # returns the species
        return self.species

    def get_attack(self):  # returns the attack
        return self.attack

    def get_defense(self):  # returns the defense
        return self.defense

    def get_speed(self):  # returns the speed
        return self.speed

    def set_attack(self, new_attack):  # assigns variable to new_attack
        self.attack = new_attack

    def evolve(self):  # a) double the attack; b) quadruple the defense; and c) triple the speed
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
