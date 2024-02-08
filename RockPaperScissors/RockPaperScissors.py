import random 

def user_choice():
    while True:
        user_choice = input("Choose Rock , Paper or scissors ").lower()
        if(user_choice in ["Rock , Paper , Scissors"]):
            return user_choice
        else:
            print("Invalid text ! please choose among Rock , Paper or Scissors")



def computer_choice():
    choices = ["Rock , Paper , Scissors"]
    return random.choice(choices)

def determine_winner(user_choice , computer_choice):
    if(user_choice == computer_choice):
        return "It's a tie!"
    elif(user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "You win !"
    else:
        return "Computer wins !"

def main():
    print("Welcome to Rock , Paper , Scissors")
    while True:


        # user_choice = get_user_choice
        # computer_choice = get_computer_choice

        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice , computer_choice)
        print(result)
        
        play_again = input("Do you wanna play again( yes/no ):").lower()
        if(play_again != "yes"):
            print("Thanks for playing ! ")
            break


main()
