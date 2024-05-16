# Pakudex
Pakudex is a powerful and flexible recreation of the popular Pokemon game, allowing users to manage and interact with their own collection of unique creatures, called Pakuri. Inspired by the beloved features of the original Pokemon games, Pakudex offers a range of functionalities through a simple command-line interface. Whether you want to add new Pakuri, list your collection, or evolve their characteristics, Pakudex provides the tools you need with ease and efficiency.

## Features
* **Add**: Adds Pakuri with user-specified name to collection.
* **Evolve**: Increases the strength of specified Pakuri.
* **Sort**: Sorts all of the Pakuri in the collection alphabetically.
* **Show**: Displays all of the Pakuri in the collection along with their respective stats.

## Usage
The program is executed through the console. Here are some examples of usage:

#### Add

    Welcome to Pakudex: Tracker Extraordinaire!
    Enter max capacity of the Pakudex: 80
    The Pakudex can hold 80 species of Pakuri.
    
    Pakudex Main Menu
    -----------------
    1. List Pakuri
    2. Show Pakuri
    3. Add Pakuri
    4. Evolve Pakuri
    5. Sort Pakuri
    6. Exit
    
    What would you like to do? 3
    Enter the name of the species to add: test_pakuri
    Pakuri species test_pakuri successfully added!

    
#### Evolve and Show

    Pakudex Main Menu
    -----------------
    1. List Pakuri
    2. Show Pakuri
    3. Add Pakuri
    4. Evolve Pakuri
    5. Sort Pakuri
    6. Exit
    
    What would you like to do? 4
    Enter the name of the species to evolve: test_pakuri
    test_pakuri has evolved!
    
    Pakudex Main Menu
    -----------------
    1. List Pakuri
    2. Show Pakuri
    3. Add Pakuri
    4. Evolve Pakuri
    5. Sort Pakuri
    6. Exit
    
    What would you like to do? 2
    Enter the name of the species to display: test_pakuri
    Species: test_pakuri
    Attack: 172
    Defense: 288
    Speed: 237


#### Exception Handling

    Welcome to Pakudex: Tracker Extraordinaire!
    Enter max capacity of the Pakudex: 20
    The Pakudex can hold 20 species of Pakuri.
    
    Pakudex Main Menu
    -----------------
    1. List Pakuri
    2. Show Pakuri
    3. Add Pakuri
    4. Evolve Pakuri
    5. Sort Pakuri
    6. Exit
    
    What would you like to do? 2
    Enter the name of the species to display: test_pakuri
    Error: No such Pakuri!
