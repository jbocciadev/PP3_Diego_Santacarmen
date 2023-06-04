import os, time, csv, cursor, colorama
from random import shuffle, choice
from pprint import pprint

def main():
    """
    Main function that controls the flow of the game in sequence.
    """
    global cities, suspects, visited, clues, victim, agent, current_location, finished, p, thief_clues, no_clue, time_remaining
    finished = False
    p = 0 #p is the variable that controls the flow of the game. It tells the system which screen to load next in the while if-else loop.
    time_remaining = 24
    cities = load_cities()
    suspects = load_suspects()
    thief = select_thief()
    thief_clues = generate_thief_clues(thief)
    no_clue = ["I don't think I have seen anyone with that description.",
    "I'm sorry agent, but that doesn't ring a bell at all!","I can't help you, sorry!","Have you seen my cat? He is orange and wears a black collar","One potato, two potatoes"]
    visited, clues = set(), []
    victim = select_victim()
    visited.add(victim["Name"])
    escape_route = create_escape_route()
    victim_location = f"{victim['Name']}, {victim['Country']}"
    stolen = choice(victim['Item'])
    finished = False
    clear()
    #game_intro()
    #input("Press Enter to continue... ")
    clear()
    agent = input(f"Identify yourself, agent!\nWhat is your name?\n")    
    intro_sequence(agent,victim_location,stolen)    
    travel("Headquarters",victim['Name'])
    current_location = victim


    while finished == False:
        if time_remaining > 0:
            if p == 0:
                clear()
                display_destination(current_location)
                time.sleep(0.5)
                destination_options()
            elif p == 1:
                print(f"{current_location['Description']}\n \n")
                input("Press Enter to go back to the main screen... ")
                p = 0
                clear()
            elif p == 2:
                interrogation_places()
                p = 0
                clear()
            elif p == 3:
                display_clues()
                input("Press Enter to go back to the main screen... ")
                p = 0
            elif p == 4:
                display_suspects()
                p = 0
            elif p == 5:
                destination = travel_options()
                if current_location != destination:
                    travel(current_location["Name"], destination["Name"])
                    current_location = destination
                    visited.add(current_location["Name"])
                    countdown()
                p = 0                
            else:
                pass
        else:
            t_print(f"Agent {agent}! I am afraid you have run out of time and the thief has escaped. \nBetter luck next time!\n")
            cursor.show()
            finished = True

cursor.show()

###################### AUXILIARY FUNCTIONS ####################################

def clear():
    """
    Clears the terminal. See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    os.system("clear")

def load_cities():
    """
    Opens cities.csv file and returns list of dict elements with all cities in the file.
    """
    with open("cities.csv", encoding='utf-8-sig') as cities_file:
        cities = csv.DictReader(cities_file, delimiter=',')
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
        suspects = csv.DictReader(suspects_file, delimiter=',')
        s_list = []
        for suspect in suspects:
            s_list.append(suspect)
        return s_list

        
def select_victim():
    """
    Shuffles list of cities and returns the first one as the victim.
    """
    shuffle(cities)
    victim = cities[0]
    return victim

def create_escape_route():
    """
    Iterates through the list of cities and adds them to a new list (escape_route). Also adds clues of city i into city i-1 dict object
    to allow the system to present clues to the user.
    """
    route = [victim["Name"]]
    for i in range(len(cities)):
        if cities[i]["Name"] not in route:
            route.append(cities[i]["Name"])
            cities[i-1]["Clues_out"] = cities[i]["Clues_in"]
            cities[i-1]["Clues_out"].append(choice(thief_clues))
            shuffle(cities[i-1]["Clues_out"])
            cities[i-1]["Previous"] = cities[i]["Name"]
        else:
            continue
    return route

def select_thief():
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

def travel(origin,destination):    
    """
    prints a sequence simulating the waiting time of a trip to the destination.
    """
    trip = [".         "," .        ","  .       ","   .      ","    .     ","     .    ","      .   ","       .  ","        . ","         ."]
    for i in range(10):
        clear()
        print(f"{origin}{trip[i]}{destination}")
        # print(origin, end=" ")
        # print(trip[i], end=" ")
        # print(destination)
        time.sleep(0.3)
        cursor.hide()

def t_print(message):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        time.sleep(0.05)
        print(char, end='', flush=True)

def intro_sequence(user,victim_location,stolen):
    """
    Prints sequence introducing the user to the game and into the case to solve.
    """
    clear()
    t_print(f"Agent {user}, we have received a report from {victim_location} that {stolen} has been stolen.\n")
    time.sleep(1.5)
    t_print(f"You have 24 hours to catch the culprit.\n")
    time.sleep(1.5)
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

def destination_options():
    """
    Display main screen for the current location's options available to the player.
    Handles the user's selection and passes on to the next iteration of the outer loop having modified the value of var "p".
    """
    options = ["Learn more about this place.","Interrogate witnesses.","View my clues.","View the usual suspects.","Travel.","Arrest suspect!"]
    t_print(f"What do you want to do next, agent {agent}?\n\n")
    for i in range(len(options)):
        print(f"{i+1}_ {options[i]}")
    global p
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
    else:
        print(f"You have selected '{selection}'. Please, make a valid selection")
        time.sleep(2)
        input("Press Enter to continue... ")


def interrogation_places():
    """
    Loads options of landmarks for user to choose.
    Checks if user arrived following clues or travelled to wrong city.
    Displays real clues if user arrived correctly, or obviously useless clues if arrived incorrectly.
    """
    
    while True:
        t_print("Select where you want to speak to the witnesses:\n")
        time.sleep(0.5)
        city = current_location["Name"]
        give_clues = False
        options = current_location["Landmarks"]

        if current_location["Previous"] in visited or len(visited) == 1:
            give_clues = True
        for i in range(len(options)):
            print(f"{i+1}_ {options[i]}")
        print("R_ Return to previous screen.")

        valid_selections = ["1","2","3","R","r"]        
        selection = input()
        if selection not in valid_selections:
            clear()
            print(f"You have selected {selection}. This is not a valid option. Please, select a valid option:")
            continue
        elif selection == "R" or selection == "r":
            return
        elif give_clues == False:
            clear()
            t_print(f"choice(no_clue)\n")
            input("Press Enter to continue... ")
        elif selection == "1":
            clear()
            s = int(selection)-1
            clue = current_location["Clues_out"][s]
            t_print(f'Witness: "{clue}"\n')
            if clue not in clues:
                clues.append(f"[{city}]_ {clue}")        
            input("Press Enter to continue... ")
            clear()
        elif selection == "2":
            clear()
            s = int(selection)-1
            clue = current_location["Clues_out"][s]
            t_print(f'Witness: "{clue}"\n')
            if clue not in clues:
                clues.append(f"[{city}]_ {clue}")          
            input("Press Enter to continue... ")
            clear()
        elif selection == "3":
            clear()
            s = int(selection)-1
            clue = current_location["Clues_out"][s]
            t_print(f'Witness: "{clue}"\n')
            if clue not in clues:
                clues.append(f"[{city}]_ {clue}")           
            input("Press Enter to continue... ")
            clear()
        else:
            print(f"Selection = {selection}")
            exit()

def display_clues():
    c_len = len(clues)
    if c_len == 0:
        t_print(f"You have collected no clues yet.\n")
    else:
        t_print(f"Clues collected:\n")
        for i in range(c_len):
            t_print(f"{i+1}_ {clues[i]}\n")
    return
    
def game_intro():
    title = """
      ____  _                     _____             __                                           ___ 
     / __ \(_)__  ____ _____     / ___/____ _____  / /_____ __________ __________ ___  ___  ____/__ |
    / / / / / _ \/ __ `/ __ \    \__ \/ __ `/ __ \/ __/ __ `/ ___/ __ `/ ___/ __ `__ \/ _ \/ __ \/ _/
   / /_/ / /  __/ /_/ / /_/ /   ___/ / /_/ / / / / /_/ /_/ / /__/ /_/ / /  / / / / / /  __/ / / /_/  
  /_____/_/\___/\__, /\____/   /____/\__,_/_/ /_/\__/\__,_/\___/\__,_/_/  /_/ /_/ /_/\___/_/ /_(_)   
               /____/                                                                                
"""
    description = """
    At "Where in the world is Diego Santacarmen you will have to chase the thief around the World collecting clues.
    Arrest your suspect before time runs out!
    """
    t_print("Where in the world is...")
    cursor.hide()
    time.sleep(1)
    print(title)
    time.sleep(2)
    for i in range(20):
        print("")
        time.sleep(.07)
    clear()
    t_print(description)
    cursor.show()

def display_suspects():
    while True:
        t_print("Select a suspect to learn more:\n")
        options = ["1","2","3","4","5","6","7","8","9","10","11","12","13","r","R"]
        for i in range(len(suspects)):
            suspect_name = str(suspects[i]["Name"] + ' ' + suspects[i]["Surname"])
            print(f"{i+1}_ {suspect_name}")
        print("R_ Return to previous screen.")
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

def travel_options():
    global cities, visited, current_location
    clear()
    cursor.hide()
    t_print("Please choose your next destination: \n\n")
    options = ["r","R"]
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
        print("R_ Return to the previous screen.")
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

def countdown():
    global time_remaining, finished
    clear()
    cursor.hide()
    for i in range(5):
        if time_remaining >= 0:
            clear()
            print(f"Time remaining: {time_remaining} hours.")
            time_remaining -= 1
            time.sleep(1)
        







    

main()