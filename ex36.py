import random
def start_screen():
    print(f"""
  ▄████  ▒█████   ▄▄▄▄    ██▓     ██▓ ███▄    █
 ██▒ ▀█▒▒██▒  ██▒▓█████▄ ▓██▒    ▓██▒ ██ ▀█   █
▒██░▄▄▄░▒██░  ██▒▒██▒ ▄██▒██░    ▒██▒▓██  ▀█ ██▒
░▓█  ██▓▒██   ██░▒██░█▀  ▒██░    ░██░▓██▒  ▐▌██▒
░▒▓███▀▒░ ████▓▒░░▓█  ▀█▓░██████▒░██░▒██░   ▓██░
 ░▒   ▒ ░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒
  ░   ░   ░ ▒ ▒░ ▒░▒   ░ ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░
░ ░   ░ ░ ░ ░ ▒   ░    ░   ░ ░    ▒ ░   ░   ░ ░
      ░     ░ ░   ░          ░  ░ ░           ░
                       ░
 ▄████▄   ██▀███   █    ██   ██████  ▄▄▄      ▓█████▄ ▓█████
▒██▀ ▀█  ▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ ▒████▄    ▒██▀ ██▌▓█   ▀
▒▓█    ▄ ▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   ▒██  ▀█▄  ░██   █▌▒███
▒▓▓▄ ▄██▒▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄
▒ ▓███▀ ░░██▓ ▒██▒▒▒█████▓ ▒██████▒▒ ▓█   ▓██▒░▒████▓ ░▒████▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░
  ░  ▒     ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░
░          ░░   ░  ░░░ ░ ░ ░  ░  ░    ░   ▒    ░ ░  ░    ░
░ ░         ░        ░           ░        ░  ░   ░       ░  ░
░                                              ░
                    PRESS ANY ENTER TO BEGIN THE CRUSADE""")

    choice = input()
    print("Type 1 to read the introduction, 2 to skip the introduction")
    while choice not in range(1,2):
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("Backstory, thief, brigand, hatred of goblins")
            print("Description of your stuff?")
            approach()
            break
        elif choice == 2:
            approach()
            break
        else:
            print("Type 1 to read the introduction, 2 to skip the introduction")

def approach():
    inventory = ['Rapier', 'Hidden blade', 'Poison', 'Smoke bomb', 'Noisemaker']
    print("Description of environment, cave entrance, time of day")
    print("Description of two goblin guards")
    print("Listen to the guards")
    #the guards must be killed for lockpicks to go straight for chief
    #
    print(f"Inventory: {inventory}")
    print("""
    1. Walk up and talk to them
    2. Ambush
    3. Attempt to sneak past
    4. Attempt to create distraction, steal
    5. Abandon quest""")
    choice = input()
    choice = int(choice)
    if choice == 1:
        print("Walk up, talk, print words, arrogant conversation")
        print("Goblins aren't scared at all, but not aggressive either")
        print("Choice")
        print(f"Inventory: {inventory}")
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("Hard random fight.")
            hard_fight = random.radrange(1,3)
            if hard_fight == 3:
                print("You win! You search their bodies and find lockpicks.")
                inventory.append("Lockpicks")
                cave_entrance(inventory)
            else:
                print("Death!")
        elif choice == 2:
            print("Uses tool, then easy random fight")
            easy_fight = random.radrange(1,3)
            if easy_fight == 2 or 3:
                print("You win! You search their bodies and find lockpicks!")
                inventory.append("Lockpicks")
                cave_entrance(inventory)
            else:
                print("You lose!")
        else:
            print("ERROR, INVALID INPUT")
    elif choice == 2:
        print("Ambush, then easy deterministic fight.")
        print(f"Inventory: {inventory}")
        print(""""Choices
        1. Obviously wrong combat choice
        2. Obviously correct combat choice
        3. Item combat choice
        4. Pretty obviously wrong combat choice
        5. Obviously wrong combat choice""")
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("Bad option")
        elif choice == 2:
            print("Good option! You find lockpicks on their corpse.")
            inventory.append("Lockpicks")
            cave_entrance(inventory)
        elif choice == 3:
            print("Use item option! You find lockpicks on their corpse.")
            inventory.remove("Poison")
            inventory.append("Lockpicks")
            cave_entrance(inventory)
        elif choice == 4:
            print("Bad option")
        elif choice == 5:
            print("Bad option")
        else:
            print("ERROR 1 - INVALID INPUT")

    elif choice == 3:
        print("Attempt to sneak by, but will get lost and die without torch")
        print("Choices")
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("RNG test, pretty easy")
        elif choice == 2:
            print("Use smoke bomb, guaranteed")
        elif choice == 3:
                print("Use noisemaker, guaranteed")
        else:
                print("ERROR - INVALID INPUT")
    elif choice == 4:
        print("Steal from goblins, RNG if succeed OR use tool OR fight")
        print("List of options")
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("RNG steal, odds in your favor")
        elif choice == 2:
            print("Noisemaker, guaranteed")
        else:
            print("ERROR 1 - INVALID INPUT")
    elif choice == 5:
        print("Abandon quest, but actually the only truly good ending.")
    else:
        print("ERROR 1 - INVALID INPUT")


def cave_entrance(inventory):
    print("Description of cave entrance, implication it's too big for goblins")
    print("Some challenge goes here - simple trap maybe?")
    print("Big drop, description of how you won't be able to get back up?")
    print(inventory)
    print("Removing Lockpicks for testing purposes")
    inventory.remove("Lockpicks")
    choice = input("Type 1 to go to crossroads")
    choice = int(choice)
    if choice == 1:
        crossroads(inventory)
    else:
        print("ERROR 2")

def crossroads(inventory):
    print("Entered the crossroads")
    print(inventory)
    if ("Rope" and "Chief's Heart" in inventory):
        print("""Final ending options
        1. Use the rope to escape""")
    elif ("Lockpicks" and not "Chief's Heart" in inventory):
        print("""Standard description+lockpicking options
        1. Go through the door to the east
        2. Go through the door to the west
        3. Try to pick the lock on the chief's door""")
    elif ("Chief Key" and not "Chief's Heart" in inventory):
        print(""""Standard description+unlock option
        1. Go through the door to the east
        2. Go through the door to the west
        3. Unlock the door""")
    elif ("Rope" and not "Chief's Heart" in inventory):
        print("""Standard description + flee
        1. Go through the door to the east
        2. Go through the door to the west
        3. Flee""")
    elif ("Chief's Heart" and not "Rope" in inventory):
        print("""Description of room but with chief's door open""")
#actually this seems bad, should make sure it can't happen
    else:
        print("""Standard description
    1. Go through the door to the east
    2. Go through the door to the west
    3. Try to force the door""")

start_screen()
#approach(starting_inventory)
