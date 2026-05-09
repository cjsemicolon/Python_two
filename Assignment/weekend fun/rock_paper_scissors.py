# PSEUDOCODE
# Start
# Input player 1 choice
# Input player 2 choice
# If choices are the same
#     Print Tie
# Else
#     Check player 1 choice
#         Compare with player 2 choice
#         Print winner
# End

player1 = input("Player 1 enter rock, paper, or scissors: ")
player2 = input("Player 2 enter rock, paper, or scissors: ")

if player1 == player2:
    print("Tie")

else:
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
