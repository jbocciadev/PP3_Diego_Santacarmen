from random import choice
import cursor
from auxiliary import (sleep, t_print, clear,
                       travel, load_cities, load_suspects,
                       no_clue, select_victim, get_agent,
                       create_escape_route, select_thief,
                       generate_thief_clues)


def intro():
    title_sequence()
    agent = get_agent()
    return agent


def game(agent):
    """
    Main function that initiates and calls different functions in sequence.
    """

    cities = load_cities()
    victim = select_victim(cities)
    suspects = load_suspects()
    thief = select_thief(suspects)
    thief_clues = generate_thief_clues(thief)
    create_escape_route(victim, cities, thief_clues)
    visited = {victim["Name"]}
    victim_location = f"{victim['Name']}, {victim['Country']}"
    stolen = choice(victim['Item'])

    intro_sequence(agent, victim_location, stolen)

    travel("Headquarters", victim['Name'])
    current_location = victim

    game_result = run_game(
                    current_location, suspects,
                    cities, thief, no_clue, visited, agent)

    game_end(game_result, agent, stolen)
    replay_game(agent)


def replay_game(agent):
    """
    Invites the player to play again
    """
    sleep(1.5)
    cursor.show()
    clear()
    while True:
        cont = input(
                "Would you like to have another go? (Y/N)\n").strip().upper()
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
            game(agent)


def game_end(game_result, agent, stolen):
    """
    Based on game outcome, displays a different message to the player.
    """
    if game_result == 0:
        clear()
        message = """Congratulations, agent {agent}!
You have caught the thief and {stolen} has been recovered successfully!
Another case solved!
""".format(agent=agent, stolen=stolen)
        t_print(f"{message}")
    elif game_result == 1:
        clear()
        message = """Agent {agent},
I regret to inform you that you have not caught the right suspect.
The thief has now run away and {stolen} will never be recovered again!
Better luck next time!
""".format(agent=agent, stolen=stolen)
        t_print(f"{message}")
    elif game_result == 2:
        message = """Agent {agent},
I am afraid you have run out of time.
The thief has escaped and {stolen} will never be recovered again!
Better luck next time!
""".format(agent=agent, stolen=stolen)
        t_print(f"{message}")


def intro_sequence(user, victim_location, stolen):
    """
    Prints sequence introducing the user
    to the game and into the case to solve.
    """
    clear()
    t_print(
        f"Agent {user}, we have received a report from {victim_location} that {stolen} has been stolen.\n")
    sleep(1.5)
    t_print("You have 24 hours to catch the culprit.\n")
    sleep(1.5)
    t_print("Head over to the crime scene to begin your investigation, and good luck!\n")
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
    to the next iteration of the outer loop
    having modified the value of var "p".
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
    selection = input().strip()
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
        selection = input().strip()
        if selection not in valid_selections:
            clear()
            print(f"You have selected {selection}. This is not a valid option. Please, select a valid option:")
            continue
        elif selection == "R" or selection == "r":
            return clues
        elif give_clues is False:  # Prints bogus clue
            clear()
            t_print(f'Witness: "{choice(no_clue)}"\n')
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
        options = [
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10",
            "11", "12", "13", "r", "R"]

        for i in range(len(suspects)):
            suspect_name = str(
                suspects[i]["Name"] + ' ' + suspects[i]["Surname"])

            print(f"{i+1}_ {suspect_name}")
        print(f"\nR_ Return to previous screen.")
        selection = input().strip()
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
    Prints the travel options available
    to the player and handles the selection made
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

        destination = input().strip()
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
        selection = input().strip()
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


def run_game(
            current_location, suspects,
            cities, thief, no_clue, visited, agent):
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
                clues = interrogation_places(
                    no_clue, current_location, clues, visited)

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
    agent = intro()
    game(agent)
