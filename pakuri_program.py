from pakuri import Pakuri
from pakudex import Pakudex  # imports classes


def menu():  # defines menu class that prints menu options
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity_condition = True  # sets the default value for condition checker
    while capacity_condition:
        try:  # exception handling to see if capacity is not a negative value
            max_capacity = int(input("Enter max capacity of the Pakudex: "))
            if max_capacity >= 0:
                capacity_condition = False
            else:
                print("Please enter a valid size.")
                continue
        except ValueError:  # prints text below if ValueError exception thrown
            print("Please enter a valid size.")
    initial_object = Pakudex(max_capacity)  # initializes Pakudex object with max_capacity parameter
    print(f"The Pakudex can hold {initial_object.get_capacity()} species of Pakuri.\n")
    loop_active = True  # sets the loop condition to true
    menu()  # calls menu function
    while loop_active:
        menu_selection_bool = True  # changes condition to false if outside of bounds
        while menu_selection_bool:
            try:  # try-catch statement to check conditions
                menu_choice = int(input("What would you like to do? "))
                if 0 < menu_choice < 7:
                    menu_selection_bool = False
                else:
                    print("Unrecognized menu selection!\n")  # error statement
                    menu()
            except ValueError:  # handles ValueError exception
                print("Unrecognized menu selection!\n")
                menu()
        if menu_choice == 1:  # performs below operations when menu selection is 1
            numbering = ""
            if initial_object.get_species_array() == None:
                print("No Pakuri in Pakudex yet!")
                menu()
            else:
                new_array = []  # initializes array to be placed
                new_string = ""  # initializes string to be printed with list
                for i in range(0, len(initial_object.pakudex_array)):
                    new_array.append(str(initial_object.pakudex_array[i].species))

                for j in range(0, len(new_array)):
                    new_string += ((str(j + 1)) + ". " + new_array[j] + "\n")
                print("Pakuri In Pakudex: ")
                print(new_string)
                menu()
        elif menu_choice == 2:  # displays the stats of the species
            selected_species = input("Enter the name of the species to display: ")
            initial_object.get_stats(selected_species)  # calls get_stats method
            menu()
            # call function to display all specifications of species
        elif menu_choice == 3:
            if len(initial_object.pakudex_array) == initial_object.capacity:
                print("Error: Pakudex is full!\n")
                menu()
                continue
            new_pakuri = input("Enter the name of the species to add: ")
            if initial_object.add_pakuri(new_pakuri) == True:
                initial_object.add_pakuri(new_pakuri)  # calls add function from pakudex
                print(f"Pakuri species {new_pakuri} successfully added!\n")
                menu()
            elif initial_object.add_pakuri(new_pakuri) == False:
                print("Error: Pakudex already contains this species!\n")
                menu()
            elif initial_object.add_pakuri(new_pakuri) == None:
                print("Error: Pakudex is full!\n")
        elif menu_choice == 4:  # evolves the species in question
            evolve_species = input("Enter the name of the species to evolve: ")
            initial_object.evolve_species(evolve_species)
            menu()
        elif menu_choice == 5:  # sorts the pakuri
            initial_object.sort_pakuri()  # sort pakuri using sort() function
            print("Pakuri have been sorted!\n")
            menu()
        elif menu_choice == 6:
            print("Thanks for using Pakudex! Bye!")
            loop_active = False  # exits out of loop


if __name__ == "__main__":
    main()
