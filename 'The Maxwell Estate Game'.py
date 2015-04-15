from time import sleep
from Kitchen import *
from Library import * 
from Candelabra import *
from Statue import *
from Hallway import *
from Basement import *
from Chamber import *

def theMaxwellEstate():
    #Game Begining
    print('-'*50)
    print('THE MAXWELL ESTATE')
    print('-'*50)
    print()
    print('''The night is still tonight in the hills of Northern Ireland.
In these hills lies a path seemingly buried as if it were meant to be forgotten.
Further down the path lies a lonely cliff just behind the hills.
Beyond the cliffside there was nothing but ocean.
However, on this cliff rests an old castle of mysterious origin...''','\n')
    sleep(10)
    print('Welcome to The Maxwell Estate...')
    print()
    sleep(3)
    gameStart = ''
    options = ["y","Y","n","N"]
    while gameStart not in options:
        gameStart = input('Would you like to play? (Y/N)')
        print()
    gameStart.lower()
    if gameStart == 'n':
        print('Good bye')
        life = False
        gameFinish = True
    if gameStart == 'y':
        life = True
        gameFinish = False
        print('~'*50)
        print()
        print('You and your friends are on a road trip through Ireland.')
        print("While you are in town you hear bar stories of a man named Joseph Maxwell.")
        print("This man was ridiculed both by the townspeople and the church for worshipping")
        print("old deities and practicing magic on the corpse of his dead wife.")
        print("Many attempts were made at his life until a seemingly fatal")
        print("attempt where one of the townspeople stabbed Maxwell in his eye.")
        print("However, Maxwell did not die and under his duress he retreated in a carriage")
        print("carrying his wife into the northern hillside...",'\n')
        sleep(15)
        print("Intrigued by the story, your friends decide that they will go explore the")
        print("northern region in search of adventure. While driving you and your friends find a mysterious unmapped")
        print("footpath on the groundclimbing up a very large hillside. You and your friends get out of the")
        print("car and begin to hike up the path. At the apex of the hill you spot a large mansion at the edge of")
        print("a cliff off in the distance. Amazed by this finding your group runs down the hill toward the mansion.")
        print("You hesitate... this place gives you a very unwelcoming vibe, the air is cold and the sun is fading away...",'\n')
        sleep(15)
        print("Noticing that you are falling behind, you chase after your friends down the hill toward the mansion.")
        print("Before you got close enough to your friends to say something they rush into the castle and shut the door.")
        print("As you approach you notice that this mansion almost takes the appearance of a small, old castle.")
        print('You stop to read a sign post reading “The Maxwell Estate.”')
        print("As it begins to get dark, you open the door and enter the estate...",'\n')
        sleep(15)
        print("After closing the door behind you, you look around. The main lobby room is dark but ")
        print("doesn’t appear to be too old despite the exterior of the mansion.")
        print("You look around and yell to your friends but you can’t hear them respond.")
        print("Instead a man’s voice echoes through the halls as if it were resonating inside of you...")
        sleep(15)

        #Restart Point
        while gameFinish != True:
            print()
            print('“Who are you… help me… find me.”','\n')
            sleep(2)
            print('You look around again and find a long hallway, stairs leading to a very dark second floor and a door leading to the kitchen.', '\n')
            sleep(1)
            print('Which direction do you explore?:')
            print("1. Down the Hallway")
            print("2. Up the Stairs")
            print("3. Into the Kitchen")
            choice = ''
            numChoices = [1,2,3]
            while choice not in numChoices:
                choice = input("Enter the number of your choice: ")
                print()
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 1 or choice == 2 or choice == 3:
                        path = choice
                        break
                    else:
                        print("Enter 1, 2, or 3")
                        print()
                        continue
                else:
                    print("Enter 1, 2, or 3")
                    print()
                    continue



            if path == 1 and life == True:
                print('~'*50)
                print()
                passHallway = hallway()
                if passHallway:
                    print('~'*50)
                    print()
                    passLibrary = library()
                    if passLibrary:
                        pathFinish = True
                    else:
                        life = False
                        pathFinish = False
                else:
                    life = False
                    pathFinish = False


                
            if path == 2 and  life == True:
                print('~'*50)
                print()
                passCandelabra = candelabra()
                if passCandelabra:
                    print('~'*50)
                    print()
                    passStatue = statue()
                    if passStatue:
                        pathFinish = True
                    else:
                        life = False
                        pathFinish = False
                else:
                    life = False
                    pathFinish = False


     
            if path == 3 and life == True:
                print('~'*50)
                print()
                passKitchen = kitchen()
                if passKitchen:
                    print('~'*50)
                    print()
                    passChamber = chamber()
                    if passChamber:
                        pathFinish = True
                    else:
                        life = False
                        pathFinish = False
                else:
                    life = False
                    pathFinish = False


            #Game Ending
            if pathFinish == True and life == True:
                print('~'*50)
                print()
                passBasement = basement(path)
                if passBasement:
                    sleep(5)
                    print('_'*50)
                    print()
                    print('''THE END''')
                    print('_'*50)
                    print()
                    sleep(5)
                    print('''Credits''')
                    print('''
           Group 6:
           
                    Inna Kravchunovska

                    Arthur Malanga 	

                    Adam Martin 	

                    Gabriela Martines

                    Jeffrey Thorpe 	
 	
                    Bradley Trowbridge
                    
                    

                    ... Thanks for Playing!''')
                    print()
                    sleep(3)
                else:
                    life = False

            #Restart Prompts    
            if life == False or passBasement == True:
                gameRestart = ''
                if life == False:
                    print('Game Over')
                    sleep(3)
                    gameRestart = input('Play Again? (Y/N)')
                while gameRestart not in options:
                    gameRestart = input('Play Again? (Y/N)')
                gameRestart.lower()
                print('_'*50)
                if gameRestart == "y":
                    life = True
                    gameFinish = False
                    continue
                elif gameRestart == "n":
                    life = False
                    gameFinish = True
                    print('Good bye')
                    break
                        
def main():
    theMaxwellEstate()


if __name__ == '__main__':
    main()
    
