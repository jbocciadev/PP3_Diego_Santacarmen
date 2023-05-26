import os, time, csv


"""
1_Create a city class with template for creating the different city elements
2_randomly select a city as the victim
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


def run_game():
    stolen = "The FIFA world cup trophy"
    victim_location = "Buenos Aires, Argentina"

    user = input(f"Identify yourself, agent!\nWhat is your name?\n")
    clear()
    print(f"Agent {user}, we have received a report from {victim_location} that {stolen} has been stolen.")
    time.sleep(3)
    print(f"You have 24 hours to catch the culprit.")
    time.sleep(2)
    print(f"Head over to the crime scene to begin your investigation, and good luck!")

def main():
    run_game()


#main()

with open("cities.csv", encoding='cp1252') as cities_file:
    cities = csv.reader(cities_file, delimiter=",")
    c_list = []
    for city in cities:
        c_list.append(city)
    print(c_list[0])