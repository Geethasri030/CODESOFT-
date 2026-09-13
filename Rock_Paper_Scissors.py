import random
your_score = 0
computer_score = 0
print("Welcome to Rock-Paper-Scissors Game!")
while True:
    your_choice = input("\nChoose rock, paper, or scissors: ").lower()
    game_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(game_options)
    print("You selected:", your_choice)
    print("Computer selected:", computer_choice)
    if your_choice == computer_choice:
        print("The match is tie!")
    elif (your_choice == "rock" and computer_choice == "scissors"):
    	print("You win this round!")
    	your_score=your_score+1
    elif (your_choice == "paper" and computer_choice == "rock"):
    	print("You win this round!")
    	your_score=your_score+1
    elif(your_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        your_score = your_score + 1
    else:
    	print("Computer wins this round!")
    	computer_score = computer_score+1
    play_again = input("Do you want to play this game again? (yes/no): ").lower()
    if play_again == "no":
        print("Well done, you played very well.")
        print("Final Score -> You:", your_score, "| Computer:", computer_score)
        break