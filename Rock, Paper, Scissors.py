import random
def rockPaperScissors():
    computer_score = 0
    my_score = 0
    options = ["rock", "paper", "scissors"]
    print("Let's play a game of rock, paper scissors.\nI'll guess one, and you guess another.\nFirst to 3 points wins! Let's play!")
    playing = True
    while playing:
        my_guess = input("What do you chose? ").lower()
        computer_guess = random.choice(options)
        if my_guess == computer_guess:
            print("That was a tie.")
            print("Your score: " + str(my_score))
            print("My score: " + str(computer_score))
        elif my_guess == "rock":
            if computer_guess == "paper":
                computer_score += 1
                print("I won that one.")
                print("Your score: " + str(my_score))
                print("My score: " + str(computer_score))
            else:
                my_score += 1
                print("You won that one.")
                print("Your score: " + str(my_score))
                print("My score: " + str(computer_score))
        elif my_guess == "paper":
            if computer_guess == "scissors":
                computer_score += 1
                print("I won that one.")
                print("Your score: " + str(my_score))
                print("My score: " + str(computer_score))
            else:
                my_score += 1
                print("You won that one.")
                print("Your score: " + str(my_score))
                print("My score: " + str(computer_score))
        elif my_guess == "scissors":
            if computer_guess == "rock":
                computer_score += 1
                print("I won that one.")
                print("Your score: " + str(my_score))
                print("My score: " + str(computer_score))
            else:
                my_score += 1
                print("You won that one.")
                print("Your score: " + str(my_score))
                print("My score: " + str(computer_score))
        if my_score == 3:
            playing = False
        elif computer_score == 3:
            playing = False
    if my_score == 3:
        print("You won.")
    else:
        print("I won.")
while True:
    rockPaperScissors()
    restart = input("Do you want to play again? Yes or No. ").lower()
    if restart == "no":
        print("Thank you for playing.")
        break
    elif restart == "yes":
        continue