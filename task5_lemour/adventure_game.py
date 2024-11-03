import time
import random
from colorama import Fore, Style


# print statment with time delay
def print_pause(str, delay=0):
    time.sleep(delay)
    print(str)


# intoduction the adventure game
def intro():
    print(Fore.YELLOW)
    print_pause("You find yourself standing in an open field ", 1)
    print_pause("filled with grassand yellow wildflowers.", 1)
    print_pause("Rumor has it that a wicked fairie is somewhere around here,", 1)
    print_pause("and has been terrifying the nearby village.", 1)
    print_pause("In front of you is a house.", 1)
    print_pause("To your right is a dark cave.", 1)
    print_pause("In your hand you hold your trusty ", 1)
    print_pause("but not very effective dagger.\n")
    print(Style.RESET_ALL)


# when going to field
def field():
    print(Style.DIM)
    print_pause("back to normal now", 1)
    print_pause("Enter 1 to knock on the door of the house", 1)
    print_pause("Enter 2 to peer into the cave.", 1)
    print_pause("What would you like to do?", 1)
    print(Style.RESET_ALL)


# whene going the cave and check the fight tool
def cave(fight_tool):
    if "gun" in fight_tool:  # if the tool with the player
        print(Fore.BLUE)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("You've been here before, and gotten all the good stuff", 2)
        print_pause("It's just an empty cave now.", 2)
        print_pause("You walk back out to the field.\n", 2)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(Style.RESET_ALL)

    else:  # if not have the tool add it to player
        print(Fore.CYAN)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        fight_tool.append("gun")
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical gun of Ogoroth!", 2)
        print_pause("You discard your silly old dagger ", 2)
        print_pause("and take the gun with you.", 2)
        print_pause("You walk back out to the field.\n", 2)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(Style.RESET_ALL)


# when going to the house of monster
def house(monster):
    print(Fore.MAGENTA)
    print("++++++++++++++++++++++++++++++++++++++++++")
    print_pause("You approach the door of the house.", 1)
    print_pause("You are about to knock ", 1)
    print_pause(f"when the door opens and out steps a{monster}.", 1)
    print_pause(f"Eep! This is the {monster} house!.", 1)
    print_pause(f"The{monster} attacks you!", 1)
    print_pause("ou feel a bit under-prepared for this,", 1)
    print_pause(" what with only having a tiny dagger.\n", 1)
    print("++++++++++++++++++++++++++++++++++++++++++")
    print(Style.RESET_ALL)


# when the player decide to fight the monster
def fight(tool):
    if "gun" not in tool:  # if not have the gun will dead
        print(Fore.RED)
        print("##################LOSS###################")
        print_pause("You do your best...", 1)
        print_pause("but your dagger is no match for the troll.", 1)
        print_pause("You have been defeated!", 1)
        print("########################################")
        print(Style.RESET_ALL)

    elif "gun" in tool:  # if have gun will win
        print(Fore.GREEN)
        print("******************************WIN****************************")
        print_pause("As the gorgon moves to attack you .", 1)
        print_pause(" unsheath your new gun.", 1)
        print_pause("The gun of Ogoroth shines brightly in your hand ", 1)
        print_pause(" as you brace yourself for the attack.But the gorgon ", 1)
        print_pause("takes one look at your shiny new toy and runs away!", 1)
        print_pause("You have rid the town of the gorgon. You are victorious!", 1)
        print("*************************************************************")
        print(Style.RESET_ALL)


# decide player would play again
def play_agin():
    choice = valid_input_string("Would you like to play again? (y/n)", ["y", "n"])
    if choice == "n":
        print_pause("Thanks for playing! See you next time.")
        exit(0)
    elif choice == "y":
        print_pause("Excellent! Restarting the game ...")


# valid input is string
def valid_input_string(prompt, options):
    while True:
        option = input(prompt).lower()
        if len(option) == 1 and (option) in options:
            return option


# valid input is numeric
def valid_input_numeric(prompt, options):
    while True:
        option = input(prompt)
        if option.isnumeric():
            if int(option) in options and (len(option) == 1):
                return int(option)


# the core of adventure game
def play_game():
    monster = random.choice(
        [
            "dinosaur",
            "snake",
            "scorpion",
        ]
    )

    tool = []
    intro()
    field()

    while True:
        choice_one = valid_input_numeric("Please enter 1 or 2.\n", [1, 2])
        if choice_one == 1:
            house(monster)
            choice_two = valid_input_numeric(
                "Would you like to (1) fight or (2)run away?", [1, 2]
            )
            if choice_two == 1:
                fight(tool)
                break
            elif choice_two == 2:
                print_pause("You run back into the field. Luckily,", 2)
                print_pause("you don't seem to have been followed.\n", 2)
            field()

        elif choice_one == 2:
            cave(tool)


# genarate the game
def game():
    while True:
        play_game()
        play_agin()


# starting adventuer game
adventure_game = game()
