from random import choice

while True:

    print("Enter R for Rock\nP for Paper\nS for Scissors\n")

    player1 = input('Choice: ').upper()

    possibilities =['R', 'P', 'S']
    
    computer = choice(possibilities)

    print('\nComputer choice is '+ computer)
    if player1 not in possibilities:
        print("Error you have entered an in valid option\n")
        break
    if player1 == computer:
        print("\nits a Tie")

    elif player1 and computer in ['S' 'P']:
        if player1 == 'S':
            print('Player Wins') 
        else:
            print('Computer wins') 
    elif player1 and computer in ['R','P']:
        if player1 == 'P':
            print('Player wins')
        else:
            print("Computer wins")
    elif player1 and computer in ['S', 'R']:
        if player1 == 'R':
            print('Player wins')
        else:
            print('Computer wins')             
    
    elif player1 == 'R' and computer == 'S':
        print('Player wins')
    elif player1 == 'R' and computer == 'P':
        print("computer wins")
    