def start_game():
    import random
    position = [2, 0]
    eggposition = random.choice(([0, 0], [0, 2], [1, 2], [2, 2]))
    haveeggs = ['false']
    basketposition = [1, 2]
    havebasket = ['false']

    def move(arg1):
        if arg1 == 'n':
            position[1] += 1
        elif arg1 == 'e':
            position[0] += 1
        elif arg1 == 's':
            position[1] -= 1
        elif arg1 == 'w':
            position[0] -= 1

    def find_egg():
        if (position[0] == eggposition[0] and position[1] == eggposition[1] and havebasket[0] == 'true'):
            haveeggs[0] = 'true'
            print("Congratulations, you found the egg! Now escape!")
        elif(position[0] == eggposition[0] and position[1] == eggposition[1]):
            print("You found the eggs, but you don't have the basket! Find the basket!")        

    def warning():
        print("You tried to enter a restricted area. Please follow the directions.")

    def room_information():
        if position[0] == 2 and position[1] == -1:
            print("\n")
            if(haveeggs[0] and havebasket[0]):
                print("Congratulations, you have beat the game!")
            else:
                print("You are outside without the eggs. Go get it!")
                direction = str(input("Please enter the lobby ('N'). ").lower())
                if direction != 'n':
                    warning()
                    room_information()
                else:
                    move(direction)
                    room_information()
                
        if position[0] == 2 and position[1] == 0:
            print("\n")
            print("You have entered the lobby.")
            find_egg()
            direction = str(input("Please enter the hallway ('N') or exit the building ('S'). ").lower())
            if direction != 's' and direction != 'n':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 2 and position[1] == 1:
            print("\n")
            print("You have entered the hallway.")
            find_egg()
            direction = str(input("Please walk down the hallway ('W'), enter the dining room ('N'), or enter the lobby ('S'). ").lower())
            if direction != 's' and direction != 'n' and direction != 'w':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 2 and position[1] == 2:
            print("\n")
            print("You have entered the Dining Room.")
            find_egg()
            direction = str(input("Please exit to the lobby ('S'). ").lower())
            if direction != 's':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 1 and position[1] == 2:
            print("\n")
            print("You have entered the kitchen.")
            find_egg()
            print("Congratulations! You have found the basket. Now find the eggs!")
            havebasket[0] = 'true'
            direction = str(input("Please enter the hallway ('S'). ").lower())
            if direction != 's':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 1 and position[1] == 1:
            print("\n")
            print("You have walked down the hallway.")
            find_egg()
            direction = str(input("Walk down further into Hallway ('W') or Go into the kitchen ('N') or to go back ('E'). ").lower())
            if direction != 'n' and direction != 'w' and direction != 'e':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 0 and position[1] == 1:
            print("\n")
            print("You have reached the end of the hallway.")
            find_egg()
            direction = str(input("Go into the Bedroom ('N') or Go into the bathroom ('S') or to go back ('E'). ").lower())
            if direction != 'n' and direction != 's' and direction != 'e':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 0 and position[1] == 0:
            print("\n")
            print("You have reached the Bathroom.")
            find_egg()
            direction = str(input("Go back to Hallway ('N').").lower())
            if direction != 'n':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
        elif position[0] == 0 and position[1] == 2:
            print("\n")
            print("You have reached the Bedroom.")
            find_egg()
            direction = str(input("Go back to Hallway ('S').").lower())
            if direction != 's':
                warning()
                room_information()
            else:
                move(direction)
                room_information()
    
    print("Let the game begin!")
    room_information()
