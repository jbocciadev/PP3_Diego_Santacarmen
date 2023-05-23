import os, time

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


main()