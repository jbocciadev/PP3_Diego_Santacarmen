from time import sleep
from os import system
from csv import DictReader
from random import shuffle, choice
import cursor


no_clue = [
        "I don't think I have seen anyone with that description.",
        "I'm sorry agent, but that doesn't ring a bell at all!",
        "I can't help you, sorry!",
        "Have you seen my cat? He is orange and wears a black collar",
        "One potato, two potatoes"
    ]


def get_agent():
    input("Press Enter to continue... ")
    clear()
    while True:
        agent = input("Identify yourself, agent!\nWhat is your name?\n").strip()
        clear()
        if agent == "":
            print("You don't have a name? That is suspicious...")
            sleep(2)
            continue
        else:
            break
    return agent

def select_victim(cities):
    """
    Shuffles list of cities and returns the first one as the victim.
    """
    shuffle(cities)
    victim = cities[0]
    return victim


def clear():
    """
    Clears the terminal.
    See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    system("clear")


def t_print(message):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        sleep(0.05)
        print(char, end='', flush=True)


def travel(origin, destination):
    """
    prints a sequence simulating the waiting time of a trip to the destination.
    """
    trip = [".         ", " .        ", "  .       ", "   .      ", "    .     ", "     .    ", "      .   ", "       .  ", "        . ", "         ."]
    for i in range(10):
        clear()
        print(f"{origin}{trip[i]}{destination}")
        sleep(0.3)
        cursor.hide()
 
def load_cities():
    """
    Opens cities.csv file and returns list of dict elements with all cities in the file.
    """
    with open("cities.csv", encoding='utf-8-sig') as cities_file:
        cities = DictReader(cities_file, delimiter=',')
        c_list = []
        for city in cities:
            city["Landmarks"] = city["Landmarks"].split(",")
            city["Item"] = city["Item"].split(",")
            city["Clues_in"] = city["Clues_in"].split(",")
            c_list.append(city)
    return c_list


def create_escape_route(victim, cities, thief_clues):
    """
    Iterates through the list of cities and adds them to a new list (escape_route). Also adds clues of city i into city i-1 dict object
    to allow the system to present clues to the user.
    """
    route = [victim["Name"]]
    victim["Previous"] = ""
    for i in range(len(cities)):
        if cities[i]["Name"] not in route:
            route.append(cities[i]["Name"])
            cities[i-1]["Clues_out"] = cities[i]["Clues_in"]
            cities[i-1]["Clues_out"].append(choice(thief_clues))
            shuffle(cities[i-1]["Clues_out"])
            cities[i]["Previous"] = cities[i-1]["Name"]
        else:
            continue
    shuffle(cities)
    return route


def load_suspects():
    """
    Opens suspects.csv file and returns list of dict elements with all suspects in the file.
    """
    with open("suspects.csv", encoding='utf-8-sig') as suspects_file:
        suspects = DictReader(suspects_file, delimiter=',')
        s_list = []
        for suspect in suspects:
            s_list.append(suspect)
        return s_list


def select_thief(suspects):
    """
    Shuffles list of suspects and returns the first one as the thief.
    """
    thief = choice(suspects)
    return thief


def generate_thief_clues(thief):
    """
    Creates and returns list of thief-specific clues for the user to read, based on values in object.
    """
    clues = []
    feature = thief["Feature"]
    profession = thief["Profession"]
    eyes = thief["Eyes"]
    if thief["Gender"] == "male":
        pron = "he"
    else:
        pron = "she"
    clues.append(f"I saw the thief! {pron.capitalize()} had {thief['Hair']} hair.")
    if feature[0] == "a":
        clues.append(f"I saw {pron} had {feature}.")
    else:
        clues.append(f"I figured {pron} {feature}.")
    clues.append(f"Judging by the way {pron} was talking, I'm sure {pron} would have been a {profession}, or something similar.")
    clues.append(f"The person you are looking for has {eyes} eyes.")
    shuffle(clues)
    return clues
