import os, time, csv, cursor, colorama
from random import shuffle, randint, choice



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

def load_suspects():
    with open("suspects.csv", encoding='utf-8-sig') as suspects_file:
        suspects = csv.DictReader(suspects_file, delimiter=',')
        s_list = []
        for suspect in suspects:
            s_list.append(suspect)
        return s_list

        
def select_victim():
    shuffle(cities)
    victim = cities[0]
    return victim

def create_escape_route():
    route = [victim["Name"]]
    print(route)
    for i in range(len(cities)):
        if cities[i]["Name"] not in route:
            route.append(cities[i]["Name"])
            cities[i-1]["Clues_out"] = cities[i]["Clues_in"]
            print(cities[i-1]["Clues_out"])
            print(route)
            time.sleep(1)
        else:
            continue

def select_thief():
    shuffle(suspects)
    thief = suspects[0]
    return thief

def generate_thief_clues(thief):
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

def travel():    
    loading = "."
    for i in range(5):
        print(loading)
        loading += '.'
        time.sleep(1)
        clear()
        cursor.hide()

def t_print(message):
    for char in message:
        time.sleep(0.05)
        print(char, end='', flush=True)

def intro_sequence(user,victim_location,stolen):
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
    cursor.show()
    t_print(f"{destination['Name']}, {destination['Country']}\n")

def destination_options():
    """
    Display main screen for the current location's options available to the player.
    Handles the user's selection and passes on to the next iteration of the outer loop having modified the value of var "p".
    """
    options = ["Learn more about this place.","Interrogate witnesses.","View my clues.","View my suspects.","Travel."]
    t_print(f"What do you want to do next, agent {agent}?\n\n")
    for i in range(len(options)):
        print(f"{i+1}_ {options[i]}")

    cursor.show()
    selection = input()
    #check_selection_input(selection)
    clear()
    if int(selection) == 1:
        global p
        p = 1
    elif int(selection) == 2:
        p = 2
    elif int(selection) == 3:
        p = 3
    elif int(selection) == 4:
        p = 4
    elif int(selection) == 5:
        p = 5
    else:
        pass


def interrogation_places():
    
    x = True
    while x == True:
        t_print("Select where you want to speak to the witnesses:\n")
        time.sleep(0.5)
        options = current_location["Landmarks"]
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
        else:
            print(f"Selection = {selection}")
            exit()

    
    pass
    ############################################   CONTINUE HERE   #############################


#Main function definition---------------------------------------------------

def main():
    global cities, suspects, visited, clues, victim, agent, current_location, finished, p
    finished = False
    p = 0 #p is the variable that controls the flow of the game. It tells the system which screen to load next in the while if-else loop.
    cities = load_cities()
    suspects = load_suspects()
    thief = select_thief()
    thief_clues = generate_thief_clues(thief)

    visited, clues = [], []
    victim = select_victim()
    visited.append(victim["Name"])
    escape_route = create_escape_route()
    print(escape_route)
    
    victim_location = f"{victim['Name']}, {victim['Country']}"
    stolen = choice(victim['Item'])
    finished = False
#    clear()

    agent = input(f"Identify yourself, agent!\nWhat is your name?\n")    
    intro_sequence(agent,victim_location,stolen)    
    travel()
    current_location = victim


    while finished == False:
        if p == 0:
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
        else:
            pass

cursor.show()



main()