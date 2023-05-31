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
    global cities, visited, clues, victim, agent, current_location, finished, p
    finished = False
    p = 0
    cities = load_cities()
    visited, clues = [], []
    victim = select_victim()
    victim_location = f"{victim['Name']}, {victim['Country']}"
    stolen = choice(victim['Item'])
    finished = False
    clear()

    agent = input(f"Identify yourself, agent!\nWhat is your name?\n")    
    intro_sequence(agent,victim_location,stolen)    
    travel()
    current_location = victim

    # display_destination(victim)
    # at_destination = True
    # destination_options()

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