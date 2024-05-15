from pakuri import Pakuri  # imports Pakuri class


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakudex_array = []  # initializes blank array for pakuri to be stored in

    def get_size(self):
        return len(self.pakudex_array)  # returns size of array with pakuri

    def get_capacity(self):
        return self.capacity  # returns capacity specified by user

    def get_species_array(self):  # returns string list with species ordered
        if len(self.pakudex_array) == 0:
            return None
        else:
            return self.pakudex_array  # returns array if length is not zero

    def get_stats(self, species):  # returns int list with attack, speed, etc. stats of species at index 0,1,2
        print_species = ""  # initializes variables to be changed later
        print_attack = 0
        print_defense = 0
        print_speed = 0
        condition = 1  # sets
        for (index, j) in enumerate(self.pakudex_array):  # indexes through array
            if species == j.species:
                print_species = j.species  # assigns new variable to prior variables
                print_attack = j.attack
                print_defense = j.defense
                print_speed = j.speed
                condition = 2  # if this condition met, future section will run
                break
            elif index == len(self.pakudex_array):
                condition = 0
                print("Error: No such Pakuri!\n")
        if condition == 2:  # prints the following code if condition is 2
            print(f"Species: {print_species}")
            print(f"Attack: {print_attack}")
            print(f"Defense: {print_defense}")
            print(f"Speed: {print_speed}\n")
        if condition == 1:  # runs if no Pakuri matched
            print("Error: No such Pakuri!\n")

    def sort_pakuri(self):
        self.pakudex_array.sort()  # sort pakuri objects according to lexicographical ordering of names
        return True

    def add_pakuri(self, species):  # defines method for adding pakuri
        for i in self.pakudex_array:
            if i.species == species:
                return False  # returns False if the species matches
            if len(self.pakudex_array) == self.capacity:
                return None  # returns None if the end
        if len(self.pakudex_array) <= self.capacity:
            self.pakudex_array.append(Pakuri(species))
            return True

    def evolve_species(self, species):  # defines method for evolving species
        for (index, i) in enumerate(self.pakudex_array):
            if i.species == species:
                i.evolve()
                print(f"{species} has evolved!\n")
                break
            elif index+1 == len(self.pakudex_array):
                print("Error: No such Pakuri!\n")
                return False  # returns False value if

