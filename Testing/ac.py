import random

# Aakriti Chaudhary Camel game
# Welcome to my world where I programmed a textual game Camel

# Using main function
def main():

# What we are going to do in the game

    print('\nWelcome to camel')
    print("You have stolen camel to make your way across the Mobi desert")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the natives.\n")

# To watch things

    done = False

    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    water_left = 3

# player options to choose from

    while not done:

        print("A. Drink from your storage.")
        print("B. Go with medium speed.")
        print("C. Go with full speed")
        print("D. Stop for night.")
        print("E. Check status.")
        print("F. Quit.\n")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == 'F':

            print("Game end.")
            break

        elif user_choice.upper() =='E':

            print("\nDistance Travelled: " + str(miles_travelled) + " miles")
            print("You have " + str(water_left) + " drinks left.")
            print("Camel tiredness: " + str(camel_tiredness))
            print("Thirst level: " + str(thirst))
            print("The natives are " +str(miles_travelled - natives_distance) + " miles behind you.\n")


        elif user_choice.upper() == "D":

            print("\nYou slept for the whole night.")
            print("Your camel is satisfied.")
            camel_tiredness = 0
            natives_distance= natives_distance + random.randrange(7,14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")


        elif user_choice.upper() == "C":

            thirst= thirst + 1
            print("\nYour camel ran in full speed.")
            miles_travelled = miles_travelled + random.randrange(10,20)
            camel_tiredness = camel_tiredness + random.randrange(1,3)
            natives_distance= natives_distance + random.randrange(7,14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

            if random.randint(1, 20) == 1:
                print("You found an Oasis. You drank water, took rest and filled your canteen.\n")
                camel_tiredness = 0
                water_left = 3
                thirst = 0

            else:
                pass


        elif user_choice.upper() == "B":

            thirst= thirst + 1
            print("\nYour camel ran in medium speed.")
            miles_travelled = miles_travelled + random.randrange(5,12)
            camel_tiredness = camel_tiredness + 1
            natives_distance= natives_distance + random.randrange(7,14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

            if random.randint(1, 20) == 1:
                print("You found an Oasis. You drank water, took rest and filled your canteen.\n")
                camel_tiredness = 0
                water_left = 3
                thirst = 0

            else:
                pass


        elif user_choice.upper() == "A":

            if water_left > 0:
                thirst = 0
                water_left = water_left - 1
                print("\nWow! That hit the spot.\n")
            else:
                print("\nYou ran out of water.\n")

# Calculation and result of stats

        if thirst > 6:
            print("Your camel died.")
            done = True
            break
        elif thirst > 4:
            print("Your camel is thirsty. Drink water!\n")

        if camel_tiredness > 8:
            print("Your camel died. He was tired.\n")
            done = True
            break
        elif camel_tiredness > 5:
            print("Your camel is getting tired. Take rest.\n")

        if natives_distance >= miles_travelled:
            print("The natives caught you. Better luck next time.\n")
            done = True
            break
        elif miles_travelled - natives_distance <= 15:
            print("Run faster!! The natives are getting closer.\n")

        if miles_travelled >= 200:
            print("You crossed the desert. You won.\n")
            done = True
            break

main()