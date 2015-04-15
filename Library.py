#Library#
from time import sleep
def library():
    fireplace = True
    print("You enter the room to find a grand fireplace about five feet tall.")
    print("The fire is roaring and as you examine the room, you see that the")
    print("only door in the room is the one you came in through. The room is")
    print("lit by the fireplace and several candles on the wall to your left.")
    print("On the wall to your right is a large bookcase filled on every")
    print("shelf with books. As you look at the bookcase more carefully,")
    print("you realize that a majority of the books are torn and burnt.")
    print("In fact, there are only three books that have legible covers.")
    print("The voice begins to speak...")
    print()
    sleep(10)
    print('"The books... hold the secret... through the fire..."')
    print()
    sleep(3)
    print("The three books are:")
    print("1. \"Three Tales\" by Fyodor Dostoyevsky")
    print("2. \"Adam Bede\" by George Eliot")
    print("3. The Holy Bible")
    print()
    sleep(2)
    book1 = False
    book2 = False
    book3 = False
    while fireplace == True:

        books = ['"Three Tales" by Fyodor Dostoyevsky','"Adam Bede" by George Eliot','The Holy Bible']
        sleep(5)
        print('Your options at this point are:')
        print()
        print("1. examine \"Three Tales\" by Fyodor Dostoyevsky")
        print("2. examine \"Adam Bede\" by George Eliot")
        print("3. examine The Holy Bible")
        print("4. burn the books")
        print("5. examine the fireplace")
        valid = False
        while valid == False:
            choice = input("Enter the number of your choice: ")
            print()
            if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
                valid = True
            else:
                print("Enter a number from 1 throuh 5")
                print()
                    
        
        if choice == "1":
            print("You open the book and realize all the text has been blacked")
            print("out. The only passage not blacked out reads:")
            print()
            print("\"They say, the sun brings life to the world. The sun will")
            print("rise and look is it not a corpse? Everything is dead and there")
            print("are corpses everywhere. Just people and around them")
            print("silence__that is the world! \"Love one another\"__who said that?")
            print("Whose command is that? The pendulum swings unfeelingly, antagonistically.")
            print("It's two o'clock at night. Her slippers are standing by her bed,")
            print("as if waiting for her....")
            print("No, seriously, when they take her away tomorrow, what shall I do?.\"")
            print()
            book1 = True
        if choice == "2":
            print("You open the book and see all the text has been blacked out except:")
            print()
            print("\"Our dead are never dead to us until we have forgotten them:")
            print("they can be injured by us, they can be wounded;")
            print("they know all our penitence, all our aching")
            print("sense that their place is empty,")
            print("all the kisses we bestow on the")
            print("smallest relic of their presence.\"")
            print()
            book2 = True
        if choice == "3":
            print("You open the book and realize all the text has been blacked out except for:")
            print()
            print("John 11:25-27:")
            print("25 Jesus said to her, \"I am the resurrection and the life.")
            print("The one who believes in me will live, even though they die;")
            print("26 and whoever lives by believing in me will never die.")
            print("Do you believe this?\" 27 \"Yes, Lord,\" she replied,")
            print("\"I believe that you are the Messiah, the Son of God,")
            print("who is to come into the world.\"")
            print()
            book3 = True
        if choice == "4":
            sleep(3)
            print("Realizing that these studies might have something to do")
            print("with Maxwell's magic you decide to take the remaining books")
            print("and throw them into the fireplace to get rid of them.")
            print("You then stand in the middle of the room not sure what to do.")
            print("You then hear a loud high pitch scream so loud it hurts.")
            print("You cover your ears and cringe. All of a sudden you hear the")
            print("voice say \"YOU FOOL!\" and everything goes dark.")
            print()
            return False
            break
        if choice == "5":
            sleep(3)
            print("Over the fireplace you see letters appear now.")
            print("It reads:")
            print()
            #HARD: print("\"NED DEAVER DET UNDOA WILTE HAVOU THEMER FORARE GOTUSTEN.\"")
            print('"ROU EDDA RAE VERNE DADE TINUL EW AHVE GOFORTENT EMTH"')
            print()
            print("You realize now that the letters above the fireplace must be an") 
            print("anagram and one of the books must have an answer")
            if (book1 == True) and (book2 == True) and (book3 == True): 
                print('Having read all the books you decide to approach the fireplace')
                print()
                print("Which book do you wish to recite a phrase from?")
                print()
                print("1. \"Three Tales\" by Fyodor Dostoyevsky")
                print("2. \"Adam Bede\" by George Eliot")
                print("3. The Holy Bible")
                valid = False
                while valid == False:
                    bookNumber = input("Enter the number of your choice: ")
                    print()
                    if bookNumber == "1" or bookNumber == "2" or bookNumber == "3":
                        valid = True
                    else:
                        print("Enter a number 1,2 or 3")
                        print()
                if bookNumber == "1":
                    recite="Everything is dead and there are corpses everywhere."
                elif bookNumber == "2":
                    recite="Our dead are never dead to us until we have forgotten them."
                elif bookNumber== "3":
                    recite="I am the resurrection and the life. \n The one who believes in me will live, even though they die."
                print("You approach the fireplace and recite the line, "+'"'+recite+'"')
                answer = "2"
                print()
                sleep(5)
                if bookNumber == answer:
                    print("You feel the air in the room drop in temperature and the candles lighting")
                    print("the room and the fire quickly go out. It's so dark now you can't see anything")
                    print("except the smoke from the once very alive fire. As the smoke clears,")
                    print("you can see a passageway through the fireplace and a light further down")
                    print("in passage. Knowing that this is the only way to go, you step through the")
                    print("fireplace and follow the dim light.")
                    fireplace = False
                    print()
                    return True
                    break
                else:
                    print("The letters over the fireplace shake violently. The candles and the fireplace")
                    print("seem to burn brighter and you feel the temperature in the room immediately rise.")
                    print("One candle falls to the floor and lights the rug on fire. The fire quickly spreads")
                    print("to the bookcase and you run for the door you entered the room in.")
                    print("It's locked now and won't budge no matter how hard you pull. The monster-like fire")
                    print("grows and quickly engulfs the entire room and you.")
                    print()
                    return False
                    break
            else:
                print("Since you haven't read all the books, you decide to return to the bookcase")
                continue

