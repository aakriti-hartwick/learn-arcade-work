import random

def main():

    print('Welcome to camel')
    print("You have stolen camel to make your way across the Mobi desert")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives")

    done = False
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    water_left = 3

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
            print("\nDistance Travelled:" +str(miles_travelled))
            print("You have " + str(water_left) + " drinks left.")
            print("The natives are " +str(miles_travelled - natives_distance) + " miles behind you.\n")

        elif user_choice.upper() == "D":
            print("\nYou slept for the whole night.")
            print("Your camel is satisfied.")
            natives_distance= natives_distance + random.randrange(7,14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

        elif user_choice.upper() == "C":
            thirst= thirst + 1
            print("\nYour camel ran in full speed.")
            miles_travelled = miles_travelled + random.randrange(10,20)
            camel_tiredness = camel_tiredness + random.randrange(1,3)
            natives_distance= natives_distance + random.randrange(7,14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

        elif user_choice.upper() == "B":
            thirst= thirst + 1
            print("\nYour camel ran in medium speed.")
            miles_travelled = miles_travelled + random.randrange(5,12)
            camel_tiredness = camel_tiredness + 1
            natives_distance= natives_distance + random.randrange(7,14)
            print("The natives are " + str(miles_travelled - natives_distance) + " miles behind you.\n")

        elif user_choice.upper() == "A":
            if water_left > 0:
                thirst = 0
                water_left = water_left - 1
                print("\nWow! That hit the spot.\n")
            else:
                print("\nYou ran out of water.\n")

        if thirst > 6:
            print("Your camel died.")
            done = True
            break
        elif thirst > 4:
            print("Your camel is thirsty. Drink water!\n")





main()