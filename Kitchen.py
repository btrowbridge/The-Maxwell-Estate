from random import randint
from time import sleep
def kitchenChoice():
    print("As the door closes behind you, you take a moment to look around.")
    print("You find yourself in the mansion's kitchen.")
    print("The kitchen is messy with plates lying around.")
    print("Many meals are just thrown into the sink untouched.")
    sleep(5)
    print()
    print("As you familiarize yourself with your new surroundings, You")
    print("notice footseps coming from the room you just came from.")
    print("You hear the voice again...")
    sleep(5)
    print()
    print('"He is coming... quick... he must not see you..."')
    print()
    sleep(3)
    print("decide to:")
    print("1. Run")
    print("2. Hide")
    print()
    choice = ''
    kitchenChoices = [1,2]
    while choice not in kitchenChoices:
        choice = input("Enter the number of your choice: ")
        print()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Enter 1 or 2")
                print()
                continue
        else:
            print("Enter 1 or 2")
            print()
            continue

def kitchenHide():
    print("You take a quick glance around, noting several places to hide.")
    print("You decide to hide: ")
    print("1. in the pantry.")
    print("2. in the walk-in freezer.")
    print("3. in the dumbwaiter")
    print("4. under the prep table")
    choice = ''
    hideSpots = [1,2,3,4]
    while choice not in hideSpots:
        choice = input("Enter the number of your choice: ")
        print()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                return choice
            else:
                print("Enter 1, 2, or 3")
                print()
                continue
        else:
            print("Enter 1, 2, or 3")
            print()
            continue

def butlerSearch(hidingSpot, searchNumber = 1):
    print()
    print("You make it to your hiding spot just as the door creeks open.  You ")
    print("quickley sneak a peek and observe an ederly butler closing the door.")
    print("His skin is grey and whithered and on his hip there is a keychain with many keys.")
    print("In his hand he is holding a sharp letter opener")
    print("Hastely, you pull your head back out of sight and wait.")
    print("You then begin to hear the butler's feet drag accross the ground")
    print('while saying "Rats... we have rats..." in a very ancient voice.')
    print()
    butlerPick1 = randint(1,4)
    if butlerPick1 == hidingSpot:
        return badEndButler2()
    if searchNumber > 1:
        butlerPick2 = randint(1,4)
        while butlerPick2 == butlerPick1:
            butlerPick2 = randint(1,4)
        if butlerPick2 == hidingSpot:
            return badEndButler2()
    else:
        return True 
        

def badEndButler1():
    sleep(3)
    print("Hearing the footsteps getting closer, you rush to the other side ")
    print("of the kitchen and twist the handle of the door in vain. The door is")
    print("locked.  Realizing that you have made the wrong choice, you spin ")
    print("around in an atempt to locate a hiding place, only to see the door ")
    print("opening as an elderly butler steps through. He quickly runs toward you")
    print("with a letter opener in his right hand and before you can react you feel")
    print("a sharp object pierce your ribcage.")
    print()
    return False

def badEndButler2():
    sleep(3)
    print("You notice the butler aproaching your hiding spot.  You hold your ")
    print("breath and hope the butler dosen't notice, as your heart thunders in ")
    print("your chest, as if it were making an atempt to burst out of your chest")
    print("and anounce your presence to the whole world.  Your hope does little ")
    print("to help you, as the butler gazes down on you...")
    sleep(3)
    print()
    print("He grabs you by the collar and with tremendous strength lifts you out")
    print("of your hiding spot and up into the air. you look into his lifeless eyes")
    print('"Filthy rat!" he yells as he cuts your throat open with the letter opener')
    print("You are dead")
    print()
    return False

def kitchen():
    if kitchenChoice() == 1:
        return badEndButler1()
    else:
        if butlerSearch(kitchenHide()):
            sleep(10)
            print("After a while, you hear the rustling of keys and the creeking of ")
            print("hinges in desperate need of oil, coming form the door opposite of")
            print("the one from which you entered.  After a few minutes have passed, ")
            print("you pop your head out only to observe an empty room.  You decide to ")
            print("continue your journey through the newly unlocked door.")
            print()
            sleep(10)
            return True
        else:
            return False
        

