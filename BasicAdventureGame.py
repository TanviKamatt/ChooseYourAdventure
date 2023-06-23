cont="yes"
while(cont=="yes"):
    name = input("Your name: ")
    print("welcome to this adventure" , name)

    answer = input("You're on a dirt road, which has now come to an end. You can go either left or right, Which way do you want to go? ").lower()

    if answer == "left":
        answer = input("You've come to a river. You can walk around it or you can swim accross. Type 'walk' to walk around or 'swim' to swim accross: ")

        if answer == "swim":
            print("You swam accross the river and were eaten by the alligator. You lose.")
        elif answer == "walk":
            print("You walked around for miles... eventually running out of water and energy. You lose.")
        else:
            print("Invalid input. You lose.")

    elif answer == "right":
        answer = input("You've come to a bridge. Oh! it looks wobbly, Do you want to cross it or head back? (cross/back) ").lower()

        if answer == "back":
            answer = input("Heading back you reach the main road. You see a car. would you like to drive it or walk? (drive/walk) ").lower()

            if answer == "drive":
                answer = input("You've come to an intersection. Do you want to go left or right? (left/right)").lower()

                if answer == "left":
                    answer = input("You've entered the jungle. Oh look! there are arrows drawn on the trees. Wonder where that leads to. want to follow the arrows? (yes/no) ").lower()

                    if answer == "yes":
                        print("You found the TREASURE. CONGRATS YOU WON! ")
                    elif answer == "no":
                        print("You go back. You lose.")
                    else:
                        print("Invalid input. you lose.")

                elif answer == "Right":
                    print("You're in a desert with no way out. You lose.")
                else:
                    print("Invalid Input. You Lose")

            elif answer == "walk":
                print("You walked around for miles... eventually running out of water and energy. You lose.")
        elif answer == "cross":
            answer = input("You've successfully crossed the river. You see a stranger. Would you like to talk to them? (yes/no) ")

            if answer == "yes":
                answer = input("the stranger gives you directions to some place. Want to follow the given directions? (yes/no) ").lower()

                if answer == "yes":
                    print("CONGRATULATIONS you've found the TREASURE. YOU WIN")
                elif answer == "no":
                    print("You ingore the stranger and wonder around until you're out of water and energy. You lose")

                else:
                    print("Invalid input. You lose.")
        else:
            print("Invalid Input. You Lose.")

    else:
        print("Invalid Input. You lose.")
    
    cont=input("Do you want to continue? (yes/no): ")
