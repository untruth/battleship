#battleship game

from random import randint

#empty board
board = []
#set column and row size (square)
grid_size = 8

#create a grid
for i in range(0, grid_size):
    board.append(["O"] * grid_size)

#print the grid
def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship")
print_board(board)

#select random row and column for ship to be in
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#create the battleships
#set number of battleships
battleships = 5
#set up list of co-ordinates for ships
ships_list = []
# set location of ships
for i in range(battleships):
    #how many ships have been created
    number_of_ships = len(ships_list)
    #while the number of ships hasn't been reached, create new ships
    while not number_of_ships == battleships:
        ship_row = random_row(board)
        ship_col = random_col(board)
        if (ship_row, ship_col) not in ships_list:
            ships_list.append((ship_row, ship_col))
            break

#print ships_list for debugging
print(ships_list)

#playing the game - input row and column, set number of guesses allowed
guesses = 4
for i in range(guesses):
    #make a guess
    print("Turn", i + 1)
    #the -1 is to take account of the user input starting at 1 not 0
    guess_row = int(input("Guess Row:")) - 1
    guess_col = int(input("Guess Col:")) - 1

    if (guess_row, guess_col) in ships_list: #correct guess
        print("Congratulations! You sank a battleship!")
        if i == guesses - 1: #if out of guesses then go to game over
            break
        else:
            board[guess_row][guess_col] = "*"
            print_board(board)
    else:
        if guess_row not in range(grid_size) or guess_col not in range(grid_size): #guess not on the board
            print("Oops, that\'s not even in the ocean.")
        elif board[guess_row][guess_col] == "X": #have we guessed this already
            print("You guessed that one already.")
        else:
            print("You missed my battleship!") #incorrect guess
            board[guess_row][guess_col] = "X"
            print_board(board)

    #checks if user out of guesses
    if i == guesses - 1:
        #ship_location = "The answer is row " + str(ship_row) + ", column " + str(ship_col) 
        print("The answer is:")
        print(ships_list)
        print_board(board)
        print("Game Over")


'''You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

    Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
    IDEA - Add user input to determine the size of the board and the number of battleships??
    Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

    Make your game a two-player game.

    Use functions to allow your game to have more features like rematches, statistics and more!
'''