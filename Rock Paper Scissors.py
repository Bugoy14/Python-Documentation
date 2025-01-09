import random
choices = ['rock', 'paper', 'scissors']
winning_moves = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

while True:
    print(f"{' ':~>30}")
    print("Rock, Paper, Scissors Game")
    while True:
        user_input = input("Pick your move: ").lower()
        if user_input in choices:
            break
        print("Invalid move!")

    bot_choice = random.choice(choices)
    print(f"You picked {user_input}. Bot picked {bot_choice}")

    if user_input == bot_choice:
        print("It's a tie")
    elif winning_moves[user_input] == bot_choice:
        print("You win!")
    else:
        print("You lose!")

    while True:
        user_input = input("Play again? y/n: ").lower()
        if user_input in ['yes', 'y']:
            print()
            break
        elif user_input in ['no', 'n']:
            print("Thanks for playing!")
            exit()
        else:
            print('Yes or No Only!')
