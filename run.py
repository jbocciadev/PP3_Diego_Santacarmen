import cursor
from csv import DictReader
from os import system
from time import sleep
from random import shuffle, choice


def game():
    """
    Main function that initiates and calls different functions in sequence.
    """

    title_sequence()

    agent = get_agent()
    cities = load_cities()
    victim = select_victim(cities)
    suspects = load_suspects()
    thief = select_thief(suspects)
    thief_clues = generate_thief_clues(thief)
    create_escape_route(victim, cities, thief_clues)
    no_clue = [
        "I don't think I have seen anyone with that description.",
        "I'm sorry agent, but that doesn't ring a bell at all!",
        "I can't help you, sorry!",
        "Have you seen my cat? He is orange and wears a black collar",
        "One potato, two potatoes"
    ]
    visited = {victim["Name"]}
    victim_location = f"{victim['Name']}, {victim['Country']}"
    stolen = choice(victim['Item'])
    intro_sequence(agent, victim_location, stolen)
    travel("Headquarters", victim['Name'])
    current_location = victim
    game_result = run_game(current_location, suspects, cities, thief, no_clue, visited, agent)
    game_end(game_result, agent, stolen)
    replay_game()


def replay_game():
    """
    Invites the player to play again
    """
    sleep(1.5)
    cursor.show()
    clear()
    while True:        
        cont = input("Would you like to have another go? (Y/N)\n").strip().upper()
        if cont == "" or cont not in ["Y", "N"]:
            clear()
            print(f"'{cont}' is not a valid option.")
            continue
        elif cont == "N":
            print("Bye!")
            sleep(2)
            clear()
            exit()
        else:
            clear()
            main()


def game_end(game_result, agent, stolen):
    """
    Based on game outcome, displays a different message to the player.
    """
    if game_result == 0:
        clear()
        message = """Congratulations, agent {agent}!
You have caught the thief and {stolen} has been recovered successfully!
Another case solved!
""".format(agent = agent, stolen = stolen)
        t_print(f"{message}")
    elif game_result == 1:
        clear()
        message = """Agent {agent},
I regret to inform you that you have not caught the right suspect.
The thief has now run away and {stolen} will never be recovered again!
Better luck next time!
""".format(agent = agent, stolen = stolen)
        t_print(f"{message}")
    elif game_result == 2:
        message = """Agent {agent},
I am afraid you have run out of time.
The thief has escaped and {stolen} will never be recovered again!
Better luck next time!
""".format(agent = agent, stolen = stolen)
        t_print(f"{message}")


def clear():
    """
    Clears the terminal.
    See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    system("clear")


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


def select_victim(cities):
    """
    Shuffles list of cities and returns the first one as the victim.
    """
    shuffle(cities)
    victim = cities[0]
    return victim


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


def t_print(message):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        sleep(0.05)
        print(char, end='', flush=True)


def intro_sequence(user, victim_location, stolen):
    """
    Prints sequence introducing the user to the game and into the case to solve.
    """
    clear()
    t_print(f"Agent {user}, we have received a report from {victim_location} that {stolen} has been stolen.\n")
    sleep(1.5)
    t_print(f"You have 24 hours to catch the culprit.\n")
    sleep(1.5)
    t_print(f"Head over to the crime scene to begin your investigation, and good luck!\n")
    input("Press Enter to continue... ")
    cursor.hide()
    clear()


def display_destination(destination):
    """
    Prints the destination name to the console.
    """
    cursor.show()
    t_print(f"{destination['Name']}, {destination['Country']}\n")


def destination_options(p, agent):
    """
    Display main screen for the current location's
    options available to the player.

    Handles the user's selection and passes on
    to the next iteration of the outer loop having modified the value of var "p".
    """
    options = [
        "Learn more about this place.",
        "Interrogate witnesses.",
        "View my clues.",
        "View the usual suspects.",
        "Travel.",
        "Arrest suspect!"
    ]
    t_print(f"What do you want to do next, agent {agent}?\n\n")
    for i in range(len(options)):
        print(f"{i+1}_ {options[i]}")
    cursor.show()
    selection = input()
    clear()
    if selection == "1":
        p = 1
    elif selection == "2":
        p = 2
    elif selection == "3":
        p = 3
    elif selection == "4":
        p = 4
    elif selection == "5":
        p = 5
    elif selection == "6":
        p = 6
    else:
        print(f"You have selected '{selection}'. Please, make a valid selection")
        sleep(2)
        input("Press Enter to continue... ")
    return p


def interrogation_places(no_clue, current_location, clues, visited):
    """
    Loads options of landmarks for user to choose.
    Checks if user arrived following clues or travelled to wrong city.

    Displays real clues if user arrived correctly,
    or obviously useless clues if arrived incorrectly.
    """

    while True:
        t_print("Select where you want to speak to the witnesses:\n")
        sleep(0.5)
        city = current_location["Name"]
        give_clues = False
        options = current_location["Landmarks"]
        if current_location["Previous"] in visited or len(visited) == 1:
            give_clues = True
        for i in range(len(options)):
            print(f"{i+1}_ {options[i]}")
        print("\nR_ Return to previous screen.")

        valid_selections = ["1", "2", "3", "R", "r"]
        selection = input()
        if selection not in valid_selections:
            clear()
            print(f"You have selected {selection}. This is not a valid option. Please, select a valid option:")
            continue
        elif selection == "R" or selection == "r":
            return clues
        elif give_clues is False:  # Prints bogus clue
            clear()
            t_print(f'Witness: "{choice(no_clue)}\n"')
            input("Press Enter to continue... ")
            clear()
        else:
            clear()
            s = int(selection)-1
            clue = current_location["Clues_out"][s]
            t_print(f'Witness: "{clue}"\n')
            if clue not in clues:
                clues.append(f"[{city}]_ {clue}")
            input("Press Enter to continue... ")
            clear()


def display_clues(clues):
    """
    Prints the clues collected by the user
    """
    c_len = len(clues)
    if c_len == 0:
        t_print("You have collected no clues yet.\n")
    else:
        t_print("Clues collected:\n\n")
        for i in range(c_len):
            print(f"{i+1}_ {clues[i]}\n")
            sleep(0.5)
    return


def title_sequence():
    """
    Prints a title sequence for the game
    """
    title = """
 _              _                               _
| \. _  _  _   (  _  _ _|_ _  _ _  _ _ _  _  _   )
|_/|(/_(_|(_)  _)(_|| | | (_|(_(_|| | | |(/_| | !
        _|
"""

    description = """
    At "Where in the world is Diego Santacarmen?" you will have to chase
    the thief around the World while collecting clues.
    Arrest your suspect before time runs out!
    """
    clear()
    t_print("Where in the world is...")
    cursor.hide()
    sleep(1)
    print(title)
    sleep(2)
    for i in range(30):
        print("")
        sleep(.07)
    clear()
    t_print(description)
    sleep(2)
    cursor.show()
    clear()


def display_suspects(suspects):
    """
    Prints a list of usual suspects for the player to arrest the correct one
    """
    while True:
        t_print("Select a suspect to learn more:\n")
        options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "r", "R"]
        for i in range(len(suspects)):
            suspect_name = str(suspects[i]["Name"] + ' ' + suspects[i]["Surname"])
            print(f"{i+1}_ {suspect_name}")
        print(f"\nR_ Return to previous screen.")
        selection = input()
        if selection == "r" or selection == "R":
            return
        elif selection not in options:
            clear()
            print(f"You have selected {selection}. This is not a valid option. Please, select a valid option:")
            continue
        else:
            clear()
            suspect = suspects[int(selection)-1]
            for key, value in suspect.items():
                print(f"{key} : {value[0].upper()}{value[1:]}")
            input("Press Enter to continue... ")
            clear()
            continue


def travel_options(cities, visited, current_location):
    """
    Prints the travel options available to the player and handles the selection made
    """
    clear()
    cursor.hide()
    t_print("Please choose your next destination: \n\n")
    options = ["r", "R"]
    seen = " (Already visited)"
    while True:
        for i in range(len(cities)):
            # message = ""
            city = cities[i]["Name"] + ", " + cities[i]["Country"]
            if current_location == cities[i]:
                continue
            if cities[i]["Name"] in visited:
                city += seen
            print(f"{i}_ {city}")
            options.append(str(i))
        print("\nR_ Return to the previous screen.")

        destination = input()
        if destination == "r" or destination == "R":
            return current_location
        elif destination not in options:
            clear()
            t_print(f"Your selection is not valid. Please make a valid selection:\n\n")
            continue
        else:
            break
    return cities[int(destination)]


def countdown(time_remaining):
    """
    Prints a countdown sequence with the time remaining for the game to be over
    """
    clear()
    cursor.hide()
    for i in range(5):
        if time_remaining >= 0:
            clear()
            print(f"Time remaining: {time_remaining} hours.")
            time_remaining -= 1
            sleep(1)
    return time_remaining


def arrest(thief, suspects, agent):
    """
    Prints list of suspects and handles user's selection
    to determine if the arrest is correct.
    """
    t_print(f"Agent {agent}, select a suspect based on your clues to proceed with the arrest:\n\n")
    sleep(0.3)
    options = ["r", "R"]
    while True:
        for i in range(len(suspects)):
            suspect = suspects[i]["Name"] + ' ' + suspects[i]["Surname"]
            print(f"{i+1}_ {suspect}")
            options.append(str(i+1))
        print("R_ Return to the previous screen.")
        selection = input()
        if selection not in options:
            clear()
            t_print(f"Your selection is not valid. Please select a valid option:\n\n")
            continue
        elif selection == 'r' or selection == 'R':
            clear()
            return
        elif suspects[int(selection)-1] == thief:
            # Returns 0 if the player selected the correct suspect, 1 otherwise
            return 0
        else:
            return 1


def run_game(current_location, suspects, cities, thief, no_clue, visited, agent):
    """
    Main game function, loops constantly and displays a different
    set of options depending on the value of p.

    Returns 0 if the thief is caught,
    1 if the caught suspect was not the thief and
    2 if time has run out.
    """
    p = 0   # p is the variable that controls the flow of the game.
    time_remaining = 24
    clues = []
    finished = False
    while finished is False:
        if time_remaining > 0:
            if p == 0:
                clear()
                display_destination(current_location)
                sleep(0.5)
                p = destination_options(p, agent)
            elif p == 1:
                print(f"{current_location['Description']}\n \n")
                input("Press Enter to go back to the main screen... ")
                p = 0
                clear()
            elif p == 2:
                clues = interrogation_places(no_clue, current_location, clues, visited)
                p = 0
                clear()
            elif p == 3:
                display_clues(clues)
                input("Press Enter to go back to the main screen... ")
                p = 0
            elif p == 4:
                display_suspects(suspects)
                p = 0
            elif p == 5:
                destination = travel_options(cities, visited, current_location)
                if current_location != destination:
                    travel(current_location["Name"], destination["Name"])
                    current_location = destination
                    visited.add(current_location["Name"])
                    time_remaining = countdown(time_remaining)
                p = 0
            elif p == 6:
                result = arrest(thief, suspects, agent)
                if result == 0:
                    finished = True
                    return 0
                else:
                    finished = True
                    return 1
        else:
            return 2
            finished = True

if __name__ == '__main__':
    game()
