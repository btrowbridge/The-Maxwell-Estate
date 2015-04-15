def statue():
    from random import randint
    from time import sleep
    #Intro/Instructions
    print('''You continue through the second level.
At the end of a hallway you see moonlight peering through a glass door.
you aproach the door and as soon as the moonlight touches the candelabra,
it begins to get very hot and burns your hand. You drop the candelabra and it breaks.
You enter through the door and into an outdoor garden on the roof of the mansion.
The garden is full of dead plants with the exception
of some large vines smothering the other plants.
In the very center you see a statue of a lady wearing a wedding gown.
She reaches her hand out as if she was being handed an object.''','\n')
    sleep(10)
    print('You hear the voice again...','\n')
    sleep(5)
    print('"Yes... this is her... isnt she beautiful... no... no... something is missing..."','\n')
    sleep(5)
    print("You observe that there are 3 objects at her feet:",'\n')
    #Object names may be altered within the list
    objects=['heart shaped pendant', 'rusty dagger', 'frosted mirror']
    print()
    #Listing objects 
    for i in range(len(objects)):
        if i==2:
            print(objects[i]+'.')
        else:
            print(objects[i]+', ', end='')
    print()
    print('Which object do you place in her hand?')
    print()
    print('1. Heart Shaped Pendant')
    print('2. Rusty Dagger')
    print('3. Frosted Miror')
    print()
    correct = 0
    #Prompt user to type in object
    choice = ''
    options = [1,2,3]
    while choice not in options:
        print()
        choice = input("Enter the number of your choice: ")
        print()
        if choice == "1" or choice == "2" or choice == "3":
            choice = int(choice)
            sleep(3)
        else:
            print("Enter a number 1,2 or 3")
            continue
    print("You reach out and place the %s in her hand" %(objects[choice - 1]))
    print()
    if correct == choice - 1:
        sleep(3)
        print('"Ah... yes... my love for her..."')
        print()
        sleep(1)
        print('The Statue begins to twist upward, revealing a spiral staircase.')
        print('You enter the staircase and begin your decent...')
        print()
        sleep(3)
        return True
    else:
        sleep(3)
        print('"Wait a minute... this seeems wrong..."')
        print('\n'*2)
        print('''The vines from the garden begin to grow rapidly toward your body.
Before you could react the vines wrap arount your throat and strangle you...''')
        correct= 0
        print()
        sleep(3)
        return False

