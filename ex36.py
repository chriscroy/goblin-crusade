from __future__ import print_function
from msvcrt import kbhit, getwch
import time
import sys
import random
import winsound
def start_screen():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound("sounds/REBORN - Visions of Freedom WAV.wav", winsound.SND_ASYNC)
    print(f"""
 ██████╗  ██████╗ ██████╗ ██╗     ██╗███╗   ██╗
██╔════╝ ██╔═══██╗██╔══██╗██║     ██║████╗  ██║
██║  ███╗██║   ██║██████╔╝██║     ██║██╔██╗ ██║
██║   ██║██║   ██║██╔══██╗██║     ██║██║╚██╗██║
╚██████╔╝╚██████╔╝██████╔╝███████╗██║██║ ╚████║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝

 ██████╗██████╗ ██╗   ██╗███████╗ █████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗██╔══██╗██╔════╝
██║     ██████╔╝██║   ██║███████╗███████║██║  ██║█████╗
██║     ██╔══██╗██║   ██║╚════██║██╔══██║██║  ██║██╔══╝
╚██████╗██║  ██║╚██████╔╝███████║██║  ██║██████╔╝███████╗
        PRESS ENTER TO START THE CRUSADE""")

    choice = input()
    print("Type 1 to read the introduction, 2 to skip the introduction")
    choice = 0
    while choice not in range(1,2):
        choice = input()
        choice = int(choice)
        if choice == 1:
            print("Alchemist, noble, hatred of goblins")
            print("Description of your stuff")
            input("Press enter to continue")
            approach()
            break
        elif choice == 2:
            approach()
            break
        else:
            print("Type 1 to read the introduction, 2 to skip the introduction")
#inventory = ['Dagger', 'Curare arrow', 'Smoke bomb', 'Fire spray', 'Capsacin spray', 'Deathcap powder']
def approach():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound("sounds/REBORN - Midnight Creeping WAV - Looped.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    inventory = ['Dagger', 'Curare arrow', 'Smoke bomb', 'Fire spray', 'Acid vial', 'Capsacin spray', 'Deathcap powder', 'Firecrackers']
    print("Description of environment, cave entrance, time of day")
    print("Description of two goblin guards")
    print("Listen to the guards")
    #the guards must be killed for lockpicks to go straight for chief
    print("""
    1. Walk up and talk to them
    2. Ambush
    3. Attempt to sneak past
    4. Abandon quest""")
    print(inventory)
    choice = 0
    while not choice in range(1,4):
        choice = input()
        choice = int(choice)
        if choice == 1:
            choice = 0
            while not choice in range(1,4):
                print("Walk up, talk, print words, arrogant conversation")
                print("Goblins aren't scared at all, but not aggressive either")
                print("""
                1. Draw your dagger and fight!
                2. Fire curare arrow to take one out
                3. Abandon quest
                4. Join the goblins""")
                print(inventory)
                choice = input()
                choice = int(choice)
                if choice == 1:
                    #You're not a fighter, this is supposed to be a bad option.
                    print("Hard random fight.")
                    hard_fight = random.randrange(1,3)
                    if hard_fight == 3:
                        print("You win! You search their bodies and find lockpicks.")
                        inventory.append("Lockpicks")
                        cave_entrance(inventory)
                        break
                    else:
                        print("Death!")
                        dead()
                        break
                elif choice == 2:
                    choice = 0
                    while not int(choice) in range(1,5):
                        #print("Ambush, then easy deterministic fight.")
                        print(""""Choices
                        1. Obviously wrong combat choice
                        2. Obviously correct combat choice
                        3. Item combat choice
                        4. Pretty obviously wrong combat choice
                        5. Obviously wrong combat choice""")
                        print(inventory)
                        choice = input()
                        choice = int(choice)
                        if choice == 1:
                            print("Bad option")
                            dead()
                            break
                        elif choice == 2:
                            print("Good option! You find lockpicks on their corpse.")
                            inventory.append("Lockpicks")
                            cave_entrance(inventory)
                            break
                        elif choice == 3:
                            #this is a trap option, designed to drain items
                            print("Use Capsacin! You find lockpicks on their corpse.")
                            inventory.remove("Capsacin spray")
                            inventory.append("Lockpicks")
                            cave_entrance(inventory)
                            break
                        elif choice == 4:
                            print("Bad option")
                            dead()
                            break
                        elif choice == 5:
                            print("Bad option")
                            dead()
                            break
                        else:
                            print(""""Choices
                            1. Obviously wrong combat choice
                            2. Obviously correct combat choice
                            3. Item combat choice
                            4. Pretty obviously wrong combat choice
                            5. Obviously wrong combat choice""")
                            print(inventory)
                elif choice == 3:
                    abandon_crusade()
                    break
                elif choice == 4:
                    join_goblins()
                    break
                else:
                    print("""Choices
                    1. Draw your dagger and fight!
                    2. Fire curare arrow to take one out.
                    3. Abandon your quest
                    4. Join the goblins""")
                    break
        elif choice == 2:
            choice = 0
            while not int(choice) in range(1,5):
                #print("Ambush, then easy deterministic fight.")
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
                    dead()
                    break
                elif choice == 2:
                    print("Good option! You find lockpicks on their corpse.")
                    inventory.append("Lockpicks")
                    cave_entrance(inventory)
                    break
                elif choice == 3:
                    print("Use item option! You find lockpicks on their corpse.")
                    inventory.remove("Capsacin spray")
                    inventory.append("Lockpicks")
                    cave_entrance(inventory)
                    break
                elif choice == 4:
                    print("Bad option")
                    dead()
                    break
                elif choice == 5:
                    print("Bad option")
                    dead()
                    break
                else:
                    print(""""Choices
                    1. Obviously wrong combat choice
                    2. Obviously correct combat choice
                    3. Item combat choice
                    4. Pretty obviously wrong combat choice
                    5. Obviously wrong combat choice""")
                    print(inventory)
        elif choice == 3:
            choice = 0
            while not int(choice) in range(1,3):
                #print("Attempt to sneak by, but won't have lockpick options later")
                print("""
                1. Attempt to sneak by without a fight
                2. Use your smoke bomb to guarantee they don't spot you
                3. Use your firecrackers to distract them and guarantee success
                4. Abandon your crusade""")
                print(inventory)
                choice = input()
                choice = int(choice)
                if choice == 1:
                    print("RNG test, pretty easy")
                    easy_test = random.randrange(1,4)
                    if easy_test == 2 or 3:
                        print("You win!")
                        cave_entrance(inventory)
                        break
                    else:
                        print("You lose!")
                        dead()
                        break
                elif choice == 2:
                    print("Use smoke bomb, guaranteed")
                    inventory.remove("Smoke bomb")
                    cave_entrance(inventory)
                    break
                elif choice == 3:
                    print("Use firecrackers, guaranteed")
                    inventory.remove("Firecrackers")
                    cave_entrance(inventory)
                    break
                elif choice == 4:
                    print("You think better of it and abandon your crusade.")
                    abandon_crusade()
                    break
                else:
                    print(""""
                    1. Attempt to sneak by
                    2. Use your smoke bomb to guarantee they don't spot you
                    3. Use your firecrackers to distract them
                    4. Abandon your crusade""")
                    print(inventory)
        elif choice == 4:
            print("Abandon crusade, but actually triggers a long, happy ending.")
            abandon_crusade()
            break
        else:
            print(inventory)
            print("""
            1. Walk up and talk to them
            2. Ambush
            3. Attempt to sneak past
            4. Abandon crusade""")

def cave_entrance(inventory):
    print("Description of cave entrance, implication cave's too big for goblins")
    #this is where they cook fire, cooking fires, etc
    #print("Big drop, description of how you won't be able to get back up?")
    print(inventory)
#    print("Removing Lockpicks for testing purposes")
#    inventory.remove("Dagger")
#    inventory.append("Rope")
    print("""
    1. Go to crossroads
    2. also go to crossroads""")
    choice = 0
    while not choice in range(1,2):
        choice = input()
        choice = int(choice)
        if choice == 1:
            crossroads(inventory)
            break
        elif choice == 2:
            crossroads(inventory)
            break
        else:
            print("""
            1. Go to crossroads
            2. also go to crossroads""")

def crossroads(inventory):
    #if the player has rope, they have an option to leave and get a happy ending
    #There is an optional lockpicking puzzle here that allows the player go to
    #the chief and skip the other areas entirely
    #The checks for "chief's heart" tell if they've beaten him or not
    #description notes: fine door to north, long, smooth, organic tunnels to
    #the east and west, clearly not goblin construction, they must have killed
    #the residents
    if ("Rope" in inventory and "Chief's Heart" in inventory):
        print("""Final ending options
        1. Use the rope to escape""")
    #implement a check in the chief's room to give a rope if they don't have it
        choice = 0
        while not choice in range(1):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You escape! Final ending.")
                break
            else:
                print("1. Use the rope to escape")
    elif ("Rope" in inventory and "Lockpicks" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description + lockpick + flee
        1. Go down the tunnel to the east
        2. Go down the tunnel to the west
        3. Lockpick option
        4. Abandon your crusade""")
        print(inventory)
        choice = 0
        while not choice in range(1,4):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You go down the tunnel to the east.")
                warg_den(inventory)
                break
            elif choice == 2:
                print("You go down the tunnel to the west.")
                duelist_room(inventory)
                break
            elif choice == 3:
                print("This is where the hard lockpicking puzzle goes.")
                break
            elif choice == 4:
                print("You abandon your quest.")
                abandon_crusade()
                break
            else: print("""
            1. Go down the tunnel to the east
            2. Go down the tunnel to the west
            3. Lockpick option
            4. Abandon your crusade""")
            print(inventory)

    elif ("Rope" in inventory and "Chief Key" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description + unlock + flee
        1. Go down the tunnel to the east
        2. Go down the tunnel to the west
        3. Unlock the door
        4. Abandon your crusade""")
        print(inventory)
        choice = 0
        while not choice in range(1,4):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You go down the tunnel to the east.")
                warg_den(inventory)
                break
            elif choice == 2:
                print("You go down the tunnel to the west.")
                duelist_room(inventory)
                break
            elif choice == 3:
                print("You unlock the door and head north.")
                chiefs_hallway(inventory)
                break
            elif choice == 4:
                print("You abandon your crusade.")
                abandon_crusade()
                break
            else:
                print("""
                1. Go down the tunnel to the east
                2. Go down the tunnel to the west
                3. Unlock the door
                4. Abandon your crusade""")
                print(inventory)
    elif ("Chief Key" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description+unlock option
        1. Go down the tunnel to the east
        2. Go down the tunnel to the west
        3. Unlock the door""")
        print(inventory)
        choice = 0
        while choice not in range(1,3):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("Go through the tunnel to the west.")
                duelist_room(inventory)
                break
            elif choice == 2:
                print("Go through the tunnel to the east.")
                warg_den(inventory)
                break
            elif choice == 3:
                print("You unlock the chief's door and head north.")
                chiefs_hallway(inventory)
                break
            else:
                print("""
                1. Go down the tunnel to the east
                2. Go down the tunnel to the west
                3. Unlock the door""")
                print(inventory)
    elif ("Lockpicks" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description+lockpicking
        1. Go through the door to the east
        2. Go through the door to the west
        3. Try to pick the lock on the chief's door""")
        print(inventory)
        choice = 0
        while not choice in range(1,3):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You go down the tunnel to the east.")
                warg_den(inventory)
                break
            elif choice == 2:
                print("You go down the tunnel to the west.")
                duelist_room(inventory)
                break
            elif choice == 3:
                print("This is where the hard lockpick puzzle goes.")
                break
            else:
                print("""
                Standard description+lockpicking options
                1. Go down the tunnel to the east
                2. Go down the tunnel to the west
                3. Try to pick the lock on the chief's door""")
                print(inventory)
    else:
        print("""Standard description
        1. Go down the tunnel to the east
        2. Go down the tunnel to the west
        3. Try to force the door""")
        print(inventory)
        choice = 0
        while choice not in range(1,3):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("Go through the door to the west.")
                duelist_room(inventory)
                break
            elif choice == 2:
                print("Go through the door to the east.")
                warg_den(inventory)
                break
            elif choice == 3:
                print("You try to force the door, but you're not remotely strong enough to do that.")
            else:
                print("""Standard description
            1. Go through the door to the east
            2. Go through the door to the west
            3. Try to force the door""")
            print(inventory)

def duelist_room(inventory):
    print("You have entered a common area, filled with noncombatants.")
    print(inventory)
    print("The goblin says, \"Are you ready?\" ")
    print("""
    1. Engage in honorable combat
    2. Use capsacin spray
    3. Join the goblins""")
    choice = 0
    while not choice in range(1,3):
        choice = input()
        choice = int(choice)
        if choice == 1:
            move = '1'
            time_limit = 2 # in seconds
            validation = timed_input('HE SLASHES HIGH\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
            print(validation)
            if validation == move:
                move = '2'
                validation = timed_input('HE SLASHES LOW\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                if validation == move:
                    print("Test successful")
                elif validation is None:
                    print("TOO SLOW!")
                    dead()
                    break
                else:
                    print("WRONG MOVE!")
                    dead()
                    break
            elif validation is None:
                print("TOO SLOW")
                dead()
                break
            else:
                print("WRONG MOVE")
                dead()
                break
        elif choice == 2:
            print("Spray capsacin")
            remove.inventory("Capsacin spray")
            break
        elif choice == 3:
            print("You decide to join the goblins.")
            join_goblins()
            break
        else:
            print("""
            1. Engage him in honorable combat
            2. Use capsacin spray
            3. Join the goblins""")

# timed input function
# Windows only
# python2 or python3
# this does not deal with arrow keys.
# this probably won't work in IDLE

def print_flush(*args):
    print(*args, end='')
    sys.stdout.flush()

def timed_input(prompt='', timeout=None):
    if timeout is None:
        return input(prompt)
    print_flush(prompt)
    start = time.time()
    response = ''
    while time.time() - start < timeout:
        if kbhit():
            char = getwch()
            if char == '\r':
                break
            elif char == '\x08': # backspace
                if response:
                    print_flush(char, char)
                    response = response[:-1]
            else:
                print_flush(char)
                response += char
        time.sleep(0.01)
    else:
        response = None
    print()
    return response

### Test / Demo code:
def samurai():
    move = '1'
    time_limit = 2 # in seconds
    validation = timed_input('HE SLASHES HIGH\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
    print(validation)
    if validation == move:
        move = '2'
        validation = timed_input('HE SLASHES LOW\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
        if validation == key:
            print("Test successful")
        elif validation is None:
            print("TOO SLOW!")
        else:
            print("WRONG MOVE!")
    elif validation is None:
        print("TOO SLOW")
        dead()
    else:
        print("WRONG MOVE")
        dead()



def living_quarters(inventory):
    print("You have entered the goblin's living quarters.")
    #include description of wide variety of beds and goblins
    print(inventory)

def warg_den(inventory):
    print("You have entered the warg den.")
    print(inventory)

def storage_area(inventory):
    print("You have entered the storage area.")
    print(inventory)

def pond(inventory):
    print("You have entered the underground pond area.")
    #something exists in the pond - remnant of previous residents?
    #ghost of christmas future?

def shamans_quarters(inventory):
    print("You have entered the shamans_quarters.")
    print(inventory)

def chiefs_hallway(inventory):
    print("You have entered the hallway leading to the Chief's chamber.")
    print(inventory)
    #originally just one encounter before chief, but maybe add something?

def concubines(inventory):
    print("You have entered the room with the concubines.")
    print(inventory)

def goblin_chief(inventory):
    print("This is the goblin chief's room.")

def abandon_crusade():
    print("If at any time the player abandons their quest, they go here.")
    quit()

def join_goblins():
    print("If at any time the player decides to join the goblins, they go here")
    quit()

def dead():
    #player goes here whenever they die
    #stops music
    winsound.PlaySound(None, winsound.SND_ASYNC)
    #plays death music
    winsound.PlaySound("sounds/REBORN - The Fallen WAV.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    print("""
     ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██║  ███╗███████║██╔████╔██║█████╗
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

     ██████╗ ██╗   ██╗███████╗██████╗
    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝ """)
    choice = 0
    while not choice in range(1,2):
        print("Press 1 to return to main menu, press 2 to quit")
        choice = input()
        choice = int(choice)
        if choice == 1:
            start_screen()
        elif choice == 2:
            quit()
        else:
            print("Press 1 to return to main menu, press 2 to quit")
start_screen()
#approach(starting_inventory)
