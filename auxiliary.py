from time import sleep
from os import system
from csv import DictReader
import cursor


no_clue = [
        "I don't think I have seen anyone with that description.",
        "I'm sorry agent, but that doesn't ring a bell at all!",
        "I can't help you, sorry!",
        "Have you seen my cat? He is orange and wears a black collar",
        "One potato, two potatoes"
    ]


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