#These must be at the top of the file or the QTEs don't work
#I do not understand why.
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

#decisions = ['SneakGuards' 'KillGuards' '']
def approach():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound("sounds/REBORN - Midnight Creeping WAV - Looped.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    inventory = ['Curare arrow', 'Smoke bomb', 'Fire spray', 'Acid vial', 'Pepper spray', 'Magic mushroom powder']
    print("Description of environment, cave entrance, time of day")
    print("Description of two goblin guards")
    print("Listen to the guards")
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
                1. Draw your dagger and fight them both!
                2. Pepper spray to make the fight easier
                3. Abandon quest
                4. Join the goblins""")
                print(inventory)
                choice = input()
                choice = int(choice)
                if choice == 1:
                    move = '1'
                    time_limit = 2.5 # in seconds
                    validation = timed_input('HIGH STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                    print(validation)
                    if validation == move:
                        move = '2'
                        validation = timed_input('LOW STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                        if validation == move:
                            move = '4'
                            validation = timed_input('HE\'S OPEN\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                            if validation == move:
                                move = '3'
                                #changing the time limit because one is down
                                time_limit = 4.5
                                validation = timed_input('MID STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                                if validation == move:
                                    move = '4'
                                    validation = timed_input('HE\'S OPEN\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                                    if validation == move:
                                        print("VICTORY! Lockpicks!")
                                        inventory.append("Lockpicks")
                                        cave_entrance(inventory)
                                        break
                                    elif validation is None:
                                        print("TOO SLOW!")
                                        dead()
                                        break
                                    else:
                                        print("WRONG MOVE!")
                                        dead()
                                        break
                                elif validation is None:
                                    print("TOO SLOW!")
                                    dead()
                                    break
                                else:
                                    print("WRONG MOVE!")
                                    dead()
                                    break
                            elif validation is None:
                                print("TOO SLOW!")
                                dead()
                                break
                            else:
                                print("WRONG MOVE!")
                                dead()
                                break
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
                        deadel()
                        break
                    else:
                        print("WRONG MOVE")
                        dead()
                        break
                elif choice == 2:
                    move = '1'
                    time_limit = 4 # in seconds
                    validation = timed_input('HIGH STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                    print(validation)
                    if validation == move:
                        move = '3'
                        validation = timed_input('MID STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                        if validation == move:
                            move = '4'
                            validation = timed_input('HE\'S OPEN\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                            if validation == move:
                                print("VICTORY! Lockpicks!")
                                inventory.append("Lockpicks")
                                cave_entrance(inventory)
                                break
                            elif validation is None:
                                print("TOO SLOW!")
                                dead()
                                break
                            else:
                                print("WRONG MOVE!")
                                dead()
                                break
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
                elif choice == 3:
                    print("You abandon your crusade")
                    abandon_crusade()
                    break
                elif choice == 4:
                    print("You join the goblins.")
                    join_goblins()
                    break
                else:
                    print("""
                    1. Draw your dagger and fight them both!
                    2. Pepper spray to make the fight easier
                    3. Abandon quest
                    4. Join the goblins""")

        elif choice == 2:
            #currently the same as the other easy fight
            print("You take one out and engage the other!")
            move = '1'
            time_limit = 4 # in seconds
            validation = timed_input('HIGH STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
            print(validation)
            if validation == move:
                move = '3'
                validation = timed_input('MID STAB\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                if validation == move:
                    move = '4'
                    validation = timed_input('HE\'S OPEN\n1. DUCK\n2. JUMP\n3. PARRY\n4. STRIKE', time_limit)
                    if validation == move:
                        print("VICTORY! Lockpicks!")
                        inventory.append("Lockpicks")
                        cave_entrance(inventory)
                        break
                    elif validation is None:
                        print("TOO SLOW!")
                        dead()
                        break
                    else:
                        print("WRONG MOVE!")
                        dead()
                        break
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

        elif choice == 3:
            choice = 0
            while not int(choice) in range(1,3):
                #print("Attempt to sneak by, but won't have lockpick options later")
                #wait convert it to QTE? how to do stealth?
                print("""
                1. Attempt to sneak by without a fight
                2. Use your smoke bomb to guarantee they don't spot you
                3. Abandon your crusade""")
                print(inventory)
                choice = input()
                choice = int(choice)
                if choice == 1:
                    print("RNG test, pretty easy")
                    easy_test = random.randrange(1,3)
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
                    print("You think better of it and abandon your crusade.")
                    abandon_crusade()
                    break
                else:
                    print(""""
                    1. Attempt to sneak by
                    2. Use your smoke bomb to guarantee they don't spot you
                    3. Abandon your crusade""")
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
                warg_den_cleared(inventory)
                break
            elif choice == 2:
                print("You go down the tunnel to the west.")
                duelist_room_cleared(inventory)
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
                print("Go down the tunnel to the west.")
                duelist_room_cleared(inventory)
                break
            elif choice == 2:
                print("Go down the tunnel to the east.")
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

    elif ("Rope" in inventory and "Lockpicks" in inventory and "Acid vial" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description + lockpick + acid + flee
        1. Go down the tunnel to the east
        2. Go down the tunnel to the west
        3. Lockpick option
        4. Pour acid on the lock
        5. Abandon your crusade""")
        print(inventory)
        choice = 0
        while not choice in range(1,5):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You go down the tunnel to the east.")
                warg_den_cleared(inventory)
                break
            elif choice == 2:
                print("You go down the tunnel to the west.")
                duelist_room(inventory)
                break
            elif choice == 3:
                print("This is where the lockpicking puzzle goes.")
                break
            elif choice == 4:
                print("You pour acid on the lock mechanism and go north.")
                chiefs_hallway(inventory)
                break
            elif choice == 5:
                print("You abandon your quest.")
                abandon_crusade()
                break
            else: print("""
            1. Go down the tunnel to the east
            2. Go down the tunnel to the west
            3. Lockpick option
            4. Pour acid on lock
            5. Abandon your crusade""")
            print(inventory)

    elif ("Lockpicks" in inventory and "Acid vial" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description + lockpick + acid
        1. Go down the tunnel to the east
        2. Go down the tunnel to the west
        3. Lockpick option
        4. Pour acid on the lock""")
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
                print("This is where the lockpicking puzzle goes.")
                break
            elif choice == 4:
                print("You pour acid on the lock.")
                chiefs_hallway(inventory)
                break
            else: print("""
            1. Go down the tunnel to the east
            2. Go down the tunnel to the west
            3. Lockpick option
            4. Pour acid on the lock""")
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

    elif ("Acid vial" in inventory and not "Chief's Heart" in inventory):
        print("""
        Standard description+lockpicking
        1. Go through the door to the east
        2. Go through the door to the west
        3. Pour acid on the door's lock""")
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
                print("This is where the lockpick puzzle goes.")
                break
            else:
                print("""
                Standard description+lockpicking options
                1. Go down the tunnel to the east
                2. Go down the tunnel to the west
                3. Pour acid on the locked door leading north""")
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
    print("The large goblin says, \"Are you ready?\" ")
    print("""
    1. Engage in honorable combat
    2. Set him on fire
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
                    print("Victory! You find a large key on him.")
                    inventory.append("Chief Key")
                    crossroads(inventory)
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
            print("You set him on fire, then finish him off, then take key.")
            inventory.remove("Fire spray")
            inventory.append("Chief Key")
            crossroads(inventory)
            break
        elif choice == 3:
            print("You decide to join the goblins.")
            join_goblins()
            break
        else:
            print("""
            1. Engage him in honorable combat
            2. Use fire spray
            3. Join the goblins""")

# timed input function
# Windows only
# python2 or python3
# this does not deal with arrow keys.
# this probably won't work in IDLE
# I copied this code off Reddit.
# I don't know how it works but it does.
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

def duelist_room_cleared(inventory):
    print("Description of the room and the dead goblin, nothing to do now but go back to the crossroads")
    crossroads(inventory)

def warg_den_cleared():
    print("Description of the room and the dead wargs, give choice to go to pond or back to crossroads.")
    crossroads(inventory)

def warg_den(inventory):
    #warg den is now the storage area
    print("You have entered the warg den.")
    print("There are two wargs sleeping next to each other in this storage area.")
    print(inventory)
    choice = 0
    if ("Fire spray" in inventory and "Meat" in inventory and "Fire Spray" in inventory):
        print("""
        1. Attack the wargs
        2. Set both of the wargs on fire
        3. Poison meat with magic mushroom powder and leave out
        """)
        while not choice in range(1,3):
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You attack the wargs and find some rope.")
                print("QTE")
                inventory.append("Rope")
                crossroads(inventory)
                break
            elif choice == 2:
                print("You set the wargs on fire and find some rope.")
                inventory.remove("Fire spray")
                inventory.append("Rope")
                crossroads(inventory)
                break
            elif choice == 3:
                print("You mix the mushroom powder with the meat and feed it to the dogs, then find some rope")
                inventory.remove("Meat")
                inventory.remove("Magic mushroom powder")
                inventory.append("Rope")
                crossroads(inventory)
                break
            else:
                print("""
                1. Attack the wargs
                2. Set both of the wargs on fire
                3. Poison meat with magic mushroom powder and leave out
                """)
    elif ("Fire spray" in inventory and not "Meat" in inventory):
        while not choice in range(1,2):
            print("""
            1. Attack the wargs
            2. Set both of the wargs on fire""")
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You attack the wargs and find some rope.")
                print("QTE")
                inventory.append("Rope")
                crossroads(inventory)
                break
            elif choice == 2:
                print("You set the wargs on fire and find some rope.")
                inventory.remove("Fire spray")
                inventory.append("Rope")
                crossroads(inventory)
                break
            else:
                print("""
                1. Attack the wargs
                2. Set both of the wargs on fire
                """)
    elif ("Meat" in inventory and "Magic mushroom powder" in inventory):
        while not choice in range(1,2):
            print("""
            1. Attack the wargs
            2. Feed the wargs poisoned meat""")
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You attack the wargs and find some rope.")
                print("QTE")
                inventory.append("Rope")
                crossroads(inventory)
                break
            elif choice == 2:
                print("You mix the mushroom powder with the meat and feed it to the dogs, then find some rope")
                inventory.remove("Meat")
                inventory.remove("Magic mushroom powder")
                inventory.append("Rope")
                crossroads(inventory)
                break
            else:
                print("""
                1. Attack the wargs
                2. Feed the wargs poisoned meat
                """)
    else:
        while not choice in range(1):
            print("""
            1. Attack the wargs""")
            choice = input()
            choice = int(choice)
            if choice == 1:
                print("You attack the wargs and find some rope.")
                print("QTE")
                inventory.append("Rope")
                crossroads(inventory)
                break
            else:
                print("""
                1. Attack the wargs
                """)
def pond(inventory):
    print("You have entered the underground pond area.")
    #something exists in the pond - remnant of previous residents?
    #ghost of christmas future?
    #cant refactor this, important!

def chiefs_hallway(inventory):
    print("You have entered the hallway leading to the Chief's chamber.")
    #this is where the concubines are now, grand hallway/lounge
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
