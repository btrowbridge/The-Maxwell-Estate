def chamber():
    from time import sleep
    print('You enter a dining room with many tables. This place looks like it was once very lively')
    print('On the wall you notice a mirror frame with mirror shards shattered on the ground.')
    print('Behind the frame there is a hidden pathway that goes further on.')
    print('You hear a slam and a yell from the butler "Where are those filthy rats?!"')
    print('You quickly run through the hidden passage and enter a barely lit room.')
    print('As you look around, you notice many torture devices that appear to be "seasoned."')
    print('The voice returns...')
    sleep(15)
    print()
    print('"How odd... I do not remember this room"')
    print()
    sleep(3)
    print('You hear loud footsteps of the butler heading towards this room from where you came')
    print('The only thing blocking the Exit is a drawbridge and three levers that control it')
    print('You must choose quickly which levers to pull (You may pull more than one)')
    print()
    sleep(3)

    lever1 = ''
    lever2 = ''
    lever3 = ''
    

    options = [ "Y", "y", "N", "n"]
    decisions = [ "1", "2"]
    print('Hurry you must choose Y or N!')
    print()
    while lever1 not in options:
        lever1 = input('Pull lever One? (Y/N) ')
        print()
    while lever2 not in options:
        lever2 = input('Pull lever Two? (Y/N) ')
        print()
    while lever3 not in options:
        lever3 = input('Pull lever Three? (Y/N) ')
        print()
    lever1 = lever1.upper()
    lever2 = lever2.upper()
    lever3 = lever3.upper()
    
    if lever1 == 'Y':
        if lever2 == 'Y':
            if lever3 == 'Y':
                print('You decide to take the time to pull all three levers.')
                print('As you finish pulling the last one, a Knife Flies out from behind you')
                print('and stabs you in the back. You lay paralyzed on the ground bleeding out.')      
                result = False
            else:
                print('You decide to pull only the first two levers.')
                print('Immediately The Floor gives out from under your feet and you begin falling')
                print('down a shaft. You reach your arms out and manage to randomly grab a ledge to')
                print('another shaft. You cannot see what lies below if you keep falling,')
                print('but the shaft in front of you smells rotten.')
                print()
                print('Do you let go and continue to fall or cimb through the shaft?')
                print()
                print('Options:')
                print('1. Fall')
                print('2. Climb')
                print()
                decision1 = input('What is your action?')
                print()
                sleep(3)
                while decision1 not in decisions:
                    print('You must choose a path your fingers are slipping!')
                    decision1 = input('What is your action? (1 or 2)')
                
                if decision1 == "1":
                    print('You fall another 20ft and land safely on some pillows.')
                    result = True
                elif decision1 == "2":
                    print('You climb through the shaft and it immediately falls off and you begin falling again.')
                    print('You land on spikes and lose all sense of pain.')
                    print('You begin to wonder what could have been as you slowly bleed out.')  
                    result = False
        elif lever2 == 'N':
            if lever3 == 'Y':
                print('You decide to only pull levers one and three.')
                print('The drawbridge drops down and you bolt across hearing the footsteps getting louder behind you.')
                print('You hear a terrifying squeak as the drawbridge starts going back up.')
                print('It goes back up at such terrifying speed that you can only flail around as it')
                print('launches you across the room into the wall breaking every bone in your body.')
                print('Your only regret... was having bones.')
                result = False
            else:
                print('You decide just to pull lever one.')
                print('As you do so nothing happens and all levers become unusable')
                print('You dont know what to do as a the butler, at least 6 1/2ft tall, comes bursting through the hallway.')
                print('Tt doesnt take long for him to notice you as he runs at you faster than you thought possible')
                print('He appears in front of you and backhands  you hard as you go flying and hit the wall. Paralyzed,')
                print('you wait there as he walks to deliver the final blow.')
                result = False
    elif lever1 == 'N':
        if lever2 == 'Y':
            if lever3 == 'Y':
                print('You decide to pull levers two and three; however this proves to be very wrong as a pendulum')
                print('swings across the room, removing your head.')
                result = False
            else:
                print('You decide to only pull lever two.')
                print('The walls begin closing in as you realize your mistake')
                print('A small tile on the floor slides away to reveal an etching.')
                print('You bend down to find the words "Answer and save yourself" as a question appears under the tile:')
                print()
                print('It is greater than God and more evil than the devil.')
                print('The poor have it, the rich need it and if you eat it you’ll die.')
                print()
                riddleAnswer = input('What is it? ')
                riddleAnswer = riddleAnswer.upper()
                print()
                if riddleAnswer == 'NOTHING':
                    print('The floor gives out from underneath you as you slide down through darkness and then land on some pillows.')
                    result = True
                else:
                    print('The Walls start closing in faster and you barely have time to curse as they crush you')
                    result = False
        else:
            if lever3 == 'Y':
                print('You choose to only pull lever three.')
                print('The draw bridge quickly lowers at an alarming speed.')
                print('Too busy celebrating you dont notice the draw bridge is extending longer than it should as it')
                print('comes down and squishes you like a bug.')
                result = False
            else:
                print('You choose not to pull any levers')
                print('The butler storms through the secret path, enters the room and begins charging at you.')
                print('You just sit there and accept your fate because you have obviously chosen death over life in this place.')
                result = False
    else:
        print('Error')

    print() 
    return result



