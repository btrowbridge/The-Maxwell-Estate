from time import sleep


def basement(path):
    if path == 1:
        print('From the fireplace, you make it down a very long hallway into a muggy room.')
        sleep(3)
        print()
    elif path == 2:
        print('You continue to decend the spiral staircase until you reach a muggy room.')
        sleep(3)
        print()
    elif path == 3:
        print('Stunned by what had just occurred to you, you find yourself at the begining of a long passage.')
        print('You stand up and cautiosly traverse through this tunnel until you reach a muggy room.')
        sleep(3)
        print()
    else:
        print('ERROR: pathing  source undefined')
    print('''You look arount and notice that you are in some sort of cellar or basement.
There are many strange unfamiliar devices and etchings written on the floors and walls.
At the back of the room there is a balcony reaching out over the cliffside leading to ocean.
The room gives you a very strange feeling that something horrible has happened here.
You start to hear whispers of profanities. The very existence of this place alone
seems to make you feel ill. Unable to bear the ringing in your ears, you fall to your knees
and start coughing.''')
    sleep(25)
    print()
    print('''Regaining balance, you rise to your knees and stumble to the middle of the room.
As some of your focus returns, you see two coffins elevated on a pedestal at the center of the room.
When you approach the coffins you see a woman and a man. You lean over to check their vitals.
The woman appears to still be warm, she only appears to be asleep. However, she has no pulse.
The man seems dead wiht cold skin  he looks dead and has many bandages wrapped around his eye.
His veins however seem to be pulsing. Your vision becomes lucid hearing HIS voice...''')
    sleep(25)
    print()
    print('''"There she is... The love of my life.... I would give anything to have her back...
My heart is pumping for her... Its the closest I'll ever be with her again...
My ring as the link... To her... and this place..."''')
    sleep(5)
    print()
    print('''You look down and notice a weeding band on his left hand.
The same hand looks decayed, flesh falling off the bone.''')
    print()
    print('''This could be your only chance to end this nightmare. Choose wisely...''')
    print()
    print('1. Toss the ring: Throw it into the ocean and cast away the curse forever.')
    print('2. Take the ring: Make a run for it. You could probabbly escape.')
    print('3. Don the ring: Wear it as your own power')
    choice = ''
    options = [1,2,3]
    while choice not in options:
        print()
        choice = input("What do you do?: ")
        print()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1 or choice == 2 or choice == 3:
                decision = choice
                break
            else:
                print("Enter 1, 2, or 3")
                continue
        else:
            print("Enter 1, 2, or 3")
            continue
    print()
    sleep(5)
    if decision == 1:
        print('''You quickly yank the ring of the dead finger and make a run for the balcony.
you can hear the ghostly voice yell after you:
''')
        sleep(5)
        print('''"NO! What are you doing?! You'll kill us!"''')
        sleep(3)
        print()
        print('''You make it to the balcony and throw the ring with all your might.
as you do this you hear a large rumbling and the whole cliffside begins to shake. Without the ring the
castle begins to crash down and crumble. The balcony collapses and you fall to your watery grave.''')
        success = False
        print()
    if decision == 2:
        print('''You grab onto the ring and tug with all your might. However, you accidentally yank off
his whole finger. You make a run for the pat you came from and as you leave the door you hear the ghost say:''')
        print()
        sleep(5)
        print('''"Useless..."''')
        print()
        sleep(3)
        print('''As soon as you make it out the door the voices return louder than ever. Their screams pierce
your brain and cause you to fall to your knees once again. the noice is so painful you squirm in pain.
You feel sharp pains inside of you and your organs rupture and you eventually end.''')
        success = False
        print()
    if decision == 3:
        print('''You ease the ring off and slide it onto your finger. Immediately you feel a burning sensation.
The burning builds up all over your hand to an dizzying pain. Any attempt to remove the ring is unnsuccessful
as if the ring is welded to your hand. Your hand starts to decay, its as if it is rapidly aging.
You immediately change your mind and make it for the balcony. On your way over you fall and start to crawl.''')
        print()
        sleep(10)
        print('''"Don't you understand?! Those voices aren't because of me, it's because of THEM. They are
ridiculing me and mocking what I've done."''')
        print()
        sleep(5)
        print('You finally make it to the balcony')
        sleep(2)
        print()
        print('''"I have sacrificed so much for HER... To bring her back... But no... They want her dead
I didnt want this place to exist. They did... inside my mind..."''')
        print()
        sleep(5)
        print('''You finally stand up''')
        print()
        sleep(1)
        print('''They even tried to end me... but they forgot one thing...''')
        sleep(2)
        print()
        print('''You lean over the ledge and prepare to throw yourself over but as you begin to
shift your wait you feel a dead hand grab your wrist.''')
        print()
        sleep(5)
        print('''"MAXWELL NEVER DIES"''')
        success = True
        print()
    return success

