#Candelabra ROOM
def candelabra():
    from random import random
    from random import randint
    from time import sleep
    #INSTRUCTIONS/INTRO
    #print("Complete following task to move on to next level: ")
    #print('-'*50)
    #print()
    #print("There is a 5-candle candelabra that has at least one candle is lit at any \ngiven time. The objective is to have ALL candles lit.")
    #print("***Be warned*** You only have 10 MATCHES and remember that candles \nto either side will switch to either ON or OFF.")
    #print("If you pick FIRST(1) or LAST(5) candle, candle on the OPPOSITE end will switch, \nas well as the one NEXT your candle.")
    #print('-'*50)
    #print()
    # RANDOMLY STARTING CANDELABRA SEQUENCE (chooses candles that are ON or OFF)
    #userCandelabra is user-viewed candelabra
    userCandelabra=[]
    on=1
    off=0
    #candelabra is running in the back ground, calculating on or off candles 
    candelabra=[]
    valid=False
    
    while not valid:
        for i in range(0,5):
            #picks ON or OFF 
            state=round(random())
            if state==on:
                candelabra+=[on]
                userCandelabra+=['Candle '+str(i+1)+': ON']
            else:
                candelabra+=[off]
                userCandelabra+=['Candle '+str(i+1)+': OFF']
        print()
        print("You chose to climb the stairs to the second level of the mansion.")
        print("As you walk up the steps, you notice that the only light shining ")
        print("on the second level is a 5-candle candelabra sitting on a table.")
        print("Only %d of its candles are lit..." %(candelabra.count(1)))
        print()
        sleep(3)
        print("Everything else is consumed by an immense darkness...")
        print()
        sleep(3)
        print("You decide that it would be a good idea to take the candelabra with you.")
        print("However, as you try to pick it up the candelabra appears to be cemented")
        print("to the table by some force...")
        print("The voice returns...")
        print()
        sleep(10)
        print('"Light the candles... Traverse the darkness..."')
        print()
        sleep(3)
        print("After the voice fades you notice 10 matches in a matchbox are also")
        print("sitting on the table.")
        print()
        sleep(3)
        print("You pick up the matchbox and begin to light the candles.")
        print('\n'*2)
        sleep(3)
        #PROOFING THAT NO CANDELABRA IS ALL (ON) OR ALL (OFF)
        if 1 in candelabra and 0 in candelabra:
            valid=True
            for i in userCandelabra:
                print(i)
                print()
        elif 1 in candelabra:
            userCandelabra.pop()
            candelabra.pop()
            candelabra.append(0)
            userCandelabra.append('Candle 5: OFF')
            valid = True
            for i in userCandelabra:
                print(i)
                print()
        else:
            userCandelabra.pop()
            candelabra.pop()
            candelabra.append(1)
            userCandelabra.append('Candle 5: ON')
            for i in userCandelabra:
                print(i)
                print()
            valid=True
  
    #MATCHES AND TRIES 
    matches=10
    tries=0
    #looping until all candles are ON
    while 0 in candelabra:
        # looping until 10 matches are used
        while 0<matches or tries<10:
            position=input("Pick candle #: ")
            #ensures that user only picks candles unlit between 1 and 5.
            while type(position) != int:
                if position.isdigit():
                    position = int(position)
                    if 0 < position < 6:
                        if candelabra[position-1] == 1:
                            print('This candle is already lit')
                            position = input("Pick another candle #: ")
                            continue
                        else:
                            pass
                    else:
                        print("Invalid choice, pick candle number from 1 to 5.")
                        position=input("Pick candle #: ")
                        print()
                        continue
                else:
                    print("Invalid choice, pick candle number from 1 to 5.")
                    position=input("Pick candle #: ")
                    print()
                    continue
            else:
                print()
                tries+=1
                matches-=1
                #2 CANDLES ON EITHER SIDE SWITCH TOO
                #pre is preceeding candle
                pre=position-2
                #current is candle picked by user
                current=position-1
                if position==5:
                    #post is next candle after user's pick
                    post=position%5
                else:
                    post=position
                #shift shows the order of the candles 
                shift=[pre, current, post]
                #loops to change ON or OFF for user candles and two on either side
                for i in shift:
                    switch=(candelabra[i]+on)%2
                    candelabra[i]=switch
                userCandelabra=[]
                #visually describes to user which candles are on or off
                for i in range(len(candelabra)):
                    if candelabra[i]==1:
                        userCandelabra+=['Candle '+str(i+1)+': ON']                    
                    else:
                        userCandelabra+=['Candle '+str(i+1)+': OFF']
                # Counts attempts vs matches left     
                print("Attempt #",tries,'\t', matches,"matches remaining.\n")
                print()
                for i in userCandelabra:
                    print(i)
                    print()
                if tries ==1:
                    if 0 in candelabra:
                        print('*'*5)
                        print('After lighting the first candle, you notice that the candles next to')
                        print('the one you lit either went out or or lit depending on what they were')
                        print('previously. This could be trickier than expected...')
                        print('*'*5)
                        print()
                    elif  0 not in candelabra:
                        print('*'*5)
                        print('After lighting the first candle, you notice that the candles next to')
                        print('the one you lit either went out or lit depending on what they were')
                        print('previously. You got pretty lucky this time...')
                        print('*'*5)
                        print()
            # PASSED candelabra room
            if not 0 in candelabra:
                sleep(5)
                print("After lighting the candles, you attempt to lift the candelabra one more time.")
                print("You lift the candelabra with ease and move on, into the darkness of the second floor...")
                sleep(3)
                print()
            #Passing the level returns TRUE
                return True
        else:
            #Failed candelabra room
            print("Runing out of matches, you panic. You begin tug at the candelabra in vain")
            print("Over time, the darkness begins to grow as the candle flame begins to die.")
            print("You can no longer see the stairs from where you came from and it becomes harder to breathe")
            print("The darkness consumes you...")
            print()
            sleep(3)
            #Failing room returns FALSE
            return False

