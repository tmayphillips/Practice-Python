player_one = input("Player 1 enter your choice: ")
player_two = input("Player 2 enter your choice: ")

if player_one == "rock":
    if player_two == "scissors":
        print("Player 1 wins")
    elif player_two == "paper":
            print("Player 2 wins")
    else:
        print("TIE")

if player_one == "scissors":
    if player_two == "paper":
        print("Player 1 wins")
    elif player_two == "rock":
        print("Player 2 wins")
    else:
        print("TIE")

if player_one == "paper":
    if player_two == "rock":
        print("Player 1 wins")
    elif player_two == "scissors":
        print("Player 2 wins")
    else:
        print("TIE")
