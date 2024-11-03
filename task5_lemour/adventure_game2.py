import time
import random
from colorama import Fore, Style, Back, init

# Initialize colorama for better cross-platform compatibility
init(autoreset=True)


# Print statement with time delay
def print_pause(message, delay=0):
    time.sleep(delay)
    print(message)


# Display the player's status (health, stamina, weapon)
def display_status(health, stamina, weapon):
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT)
    print(f"Health: {health} | Stamina: {stamina} | Weapon: {weapon}")
    print(Style.RESET_ALL)


# Simple text-based map of the game world
def display_map():
    print(Fore.WHITE + Back.GREEN)
    print(" " * 10 + "  Field  ")
    print("House", " " * 12, "Cave")
    print(" " * 10 + "  River  ")
    print(Style.RESET_ALL)


# Introduction to the adventure game
def intro(health, stamina, weapon):
    print(Fore.YELLOW)
    print_pause("You find yourself standing in an open field ", 1)
    print_pause("filled with grass and yellow wildflowers.", 1)
    print_pause("Rumor has it that a wicked fairie is somewhere around here,", 1)
    print_pause("and has been terrifying the nearby village.", 1)
    print_pause("In front of you is a house.", 1)
    print_pause("To your right is a dark cave.", 1)
    print_pause(
        "In your hand, you hold your trusty, but not very effective, dagger.\n", 1
    )
    print(Style.RESET_ALL)
    display_status(health, stamina, weapon)
    display_map()


# When going to the field
def field():
    print(Style.DIM)
    print_pause("Back to the field now", 1)
    print_pause("Enter 1 to knock on the door of the house", 1)
    print_pause("Enter 2 to peer into the cave.", 1)
    print_pause("What would you like to do?", 1)
    print(Style.RESET_ALL)


# When going to the cave and checking the fight tool
def cave(fight_tool, health, stamina):
    if "gun" in fight_tool:
        print(Fore.BLUE)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("You've been here before and gotten all the good stuff.", 2)
        print_pause("It's just an empty cave now.", 2)
        print_pause("You walk back out to the field.\n", 2)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    else:
        print(Fore.CYAN)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        fight_tool.append("gun")
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("It turns out to be a small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical gun of Ogoroth!", 2)
        print_pause("You discard your silly old dagger and take the gun with you.", 2)
        print_pause("You walk back out to the field.\n", 2)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    display_status(health, stamina, fight_tool[-1])


# When going to the house of the monster
def house(monster, health, stamina, weapon):
    print(Fore.MAGENTA)
    print("++++++++++++++++++++++++++++++++++++++++++")
    print_pause("You approach the door of the house.", 1)
    print_pause("You are about to knock ", 1)
    print_pause(f"when the door opens and out steps a {monster}.", 1)
    print_pause(f"Eep! This is the {monster}'s house!", 1)
    print_pause(f"The {monster} attacks you!", 1)
    print_pause("You feel a bit under-prepared for this, ", 1)
    print_pause("what with only having a tiny dagger.\n", 1)
    print("++++++++++++++++++++++++++++++++++++++++++")
    display_status(health, stamina, weapon)


# When the player decides to fight the monster
def fight(tool, health):
    if "gun" not in tool:
        print(Fore.RED)
        print("################## LOSS ###################")
        print_pause("You do your best...", 1)
        print_pause("But your dagger is no match for the troll.", 1)
        print_pause("You have been defeated!", 1)
        print("########################################")
    else:
        print(Fore.GREEN)
        print("****************************** WIN ****************************")
        print_pause("As the gorgon moves to attack, you unsheath your new gun.", 1)
        print_pause("The gun of Ogoroth shines brightly as you brace yourself.", 1)
        print_pause("The gorgon sees your shiny new weapon and runs away!", 1)
        print_pause("You have rid the town of the gorgon. You are victorious!", 1)
        print("*************************************************************")
    display_status(health, 100, tool[-1])  # Display status after the fight


# Decide if the player would play again
def play_again():
    choice = valid_input_string("Would you like to play again? (y/n) ", ["y", "n"])
    if choice == "n":
        print_pause("Thanks for playing! See you next time.")
        exit(0)
    elif choice == "y":
        print_pause("Excellent! Restarting the game ...")


# Valid input for string options
def valid_input_string(prompt, options):
    while True:
        option = input(prompt).lower()
        if len(option) == 1 and option in options:
            return option


# Valid input for numeric options
def valid_input_numeric(prompt, options):
    while True:
        option = input(prompt)
        if option.isnumeric() and int(option) in options:
            return int(option)


# The core of the adventure game
def play_game():
    monster = random.choice(["dinosaur", "snake", "scorpion"])
    health, stamina = 100, 100
    tool = ["dagger"]

    intro(health, stamina, tool[-1])
    field()

    while True:
        choice_one = valid_input_numeric("Please enter 1 or 2.\n", [1, 2])
        if choice_one == 1:
            house(monster, health, stamina, tool[-1])
            choice_two = valid_input_numeric(
                "Would you like to (1) fight or (2) run away? ", [1, 2]
            )
            if choice_two == 1:
                fight(tool, health)
                break
            elif choice_two == 2:
                print_pause("You run back into the field. Luckily,", 2)
                print_pause("you don't seem to have been followed.\n", 2)
            field()
            display_status(health, stamina, tool[-1])

        elif choice_one == 2:
            cave(tool, health, stamina)
            display_map()


# Generate the game loop
def game():
    while True:
        play_game()
        play_again()


# Start the adventure game
adventure_game = game()
