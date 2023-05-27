import os, time, csv, cursor, colorama
from random import shuffle, randint, choice
from pprint import pprint


"""
1_Create a city class with template for creating the different city elements                                    - NOT NECESSARY
2_randomly select a city as the victim                                                                          - DONE
3_randomly select a second city as the hiding place
4_randomly select another 4 cities where there will be clues
5_create a list of places visited so the user can fly back
6_create a list of clues collected along the way so the user can consult at any point in the game
7_create presentation screens for the different cities using the ASCII art and description from city object
"""


def clear():
    """
    Clears the terminal. See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system("clear")

def load_cities():
    with open("cities.csv", encoding='utf-8-sig') as cities_file:
        cities = csv.DictReader(cities_file, delimiter=',')
        c_list = []
        for city in cities:
            city["Landmarks"] = city["Landmarks"].split(",")
            city["Item"] = city["Item"].split(",")
            c_list.append(city)
    return c_list

        
def select_victim():
    shuffle(cities)
    victim = cities.pop()
    return victim

def travel():
    loading = "."
    for i in range(5):
        print(loading)
        loading += '.'
        time.sleep(1)
        clear()

#Main function definition---------------------------------------------------

def main():
    global cities, visited, clues
    cities = load_cities()
    visited, clues = [], []
    victim = select_victim()
    victim_location = f"{victim['Name']}, {victim['Country']}"
    stolen = choice(victim['Item'])
    
    user = input(f"Identify yourself, agent!\nWhat is your name?\n")
    
    clear()
    cursor.hide()
    print(f"Agent {user}, we have received a report from {victim_location} that {stolen} has been stolen.")
    time.sleep(3)
    print(f"You have 24 hours to catch the culprit.")
    time.sleep(2)
    print(f"Head over to the crime scene to begin your investigation, and good luck!")
    time.sleep(3)
    clear()

    travel()



main()