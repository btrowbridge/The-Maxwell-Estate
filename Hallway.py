
from random import randint
from time import sleep
def hallway():    
    inventory = [] 
    lockedDoor=5
    hallDoors =[1,2,3,4]
    doorOption = [ 'N','n','Y','y']
    deathDoor = hallDoors.pop(randint(0,len(hallDoors)-1))

    keyDoor = hallDoors.pop(randint(0,len(hallDoors)-1))
    
    coinDoor = hallDoors.pop(randint(0,len(hallDoors)-1))
    
    trapDoor = hallDoors.pop(0)
           
    print('You find yourself standing in front of a long, dark hallway.')
    print('There are five doors. Two on either side, and one at the end.')
    print('As you inspect the hallway you find the doors are numbered, with 5 at the end.')
    print('The doors have even numbers on the right, with odd numbers on the left.')
    print('The voice returns...')
    sleep(10)
    print()
    print('"One of these doors are locked... make it through..."')
    print()
    doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
    print()
    doorsOptions = [0,1,2,3,4,5]
    doorsUnvisit = [0,1,2,3,4,5]
    while doorChoice!=lockedDoor or 'key' not in inventory:
        while doorChoice not in doorsOptions:
            if doorChoice.isdigit()== True and 0 <= int(doorChoice) <= 5:
                doorChoice = int(doorChoice)
            else:
                print('That is not an option')
                print()
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
                continue
        if doorChoice not in doorsUnvisit:
            print('There is nothing left in this room for you.')
            print()
            doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
            print()
            continue
        if doorChoice==0:
            print('You find yourself standing in front of a long, dark hallway.')
            print('There are five doors. Two on either side, and one at the end.')
            print('As you inspect the hallway you find the doors are numbered, with 5 at the end')
            print('The doors have even numbers on the right, with odd numbers on the left')
            print()
            doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
            print()
        if doorChoice==lockedDoor and 'key' not in inventory:
            print('The door is locked...')
            print()
            doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
            print()
        if doorChoice==0:
            print('You find yourself standing in front of a long, dark hallway.')
            print('There are five doors. Two on either side, and one at the end.')
            print('As you inspect the hallway you find the doors are numbered, with 5 at the end')
            print('The doors have even numbers on the right, with odd numbers on the left')
            print()
            doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
            print()
        if doorChoice==trapDoor:
            choice=input('You smell an errie oder... Do you open the door?(Y or N): ')
            print()
            while choice not in doorOption:
                choice=input('You smell an errie oder... Do you open the door?(Y or N): ')
                print()
            if choice=='N' or choice=='n':
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
            if choice=='Y' or choice=='y':
                print('There appears to be the decomposing corpse of the last person...')
                print('Better leave now.')
                print()
                doorsUnvisit.remove(doorChoice)
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
        if doorChoice==deathDoor:
            choice=input('The door handle is hot... Do you open it?(Y or N): ')
            print()
            while choice not in doorOption:
                choice=input('The door handle is hot... Do you open it?(Y or N): ')
                print()
            if choice=='N' or choice=='n':
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
            if choice=='Y' or choice=='y':
                sleep(3)
                print('A monsterous wall of fire pours forth from the open door!')
                print('You try to run as a scaley hand shoots out and drags you to your death...')
                print()
                return False
                break            
        if doorChoice==coinDoor:
            choice=input('There is a strong smell of metal... Do you proceed?(Y or N): ')
            print()
            while choice not in doorOption:
                choice=input('There is a strong smell of metal... Do you proceed?(Y or N): ')
                print()
            if choice=='N' or choice=='n':
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
            if choice=='Y' or choice=='y':
                print('There is only a small nightstand with a latch in the corner.')
                print()
                choice=input('Do you open it?: ')
                print()
                while choice not in doorOption:
                    choice=input('Do you open it?: ')
                    print()
                if choice=='N' or choice=='n':
                    print('You choose to ignore the dest and proceed back to the hallway.')
                    print()
                    doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                    print()
                if choice=='Y' or choice=='y':
                    print('You open the drawer and find some coins!')
                    inventory+=['coins']
                    print('"coins" are added to the inventory')
                    print('You exit and reenter the hallway.')
                    print()
                    doorsUnvisit.remove(doorChoice)
                    doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                    print()
        if doorChoice==keyDoor and 'coins' not in inventory:
            choice=input('The door is quite warped... enter anyway?(Y or N): ')
            print()
            while choice not in doorOption:
                choice=input('The door is quite warped... enter anyway?(Y or N): ')
                print()
            if choice=='N' or choice=='n':
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
            if choice=='Y' or choice=='y':
                print('There are strange slots in the wall...')
                print('You leave the room since there is nothing you can do.')
                print()
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
        if doorChoice==keyDoor and 'coins' in inventory:
            choice=input('The door is quite warped... Enter anyway?(Y or N): ')
            print()
            while choice not in doorOption:
                choice=input('The door is quite warped... Enter anyway?(Y or N): ')
                print()
            if choice=='N' or choice=='n':
                doorChoice=input('Which door do you choose?(only #s 1-5 and press 0 to repeat): ')
                print()
            if choice=='Y' or choice=='y':
                print('There are strange slots in the wall...')
                print('You insert the coins into the slots.')
                inventory = []
                print('There is a loud rumble as gears start to turn and key pops out!')
                print()
                inventory+=['key']
                print('"key" is added to the inventory')
                print()
                doorChoice=input('Which door do you choose?(only #s and press 0 to repeat): ')
                print()
        if doorChoice==lockedDoor and 'key' in inventory:
            print('You pull out the key and it fits in the door!')
            inventory.remove('key')
            print('The door opens and you proceed to the next room...')
            print()
            sleep(3)
            return True
            break

