import gameboard
import os
import ships
import time


def play_battleship():
    
    user_width = 0
    play_again = 0
    turns = 0

    while play_again != 2:

        if play_again == 0:

            os.system('cls')

            #prompt the user to play a game or exit.
            print("Would you like to play a game of Battleship?")
            print("Enter 1 to play")
            print("Enter 2 to exit")
            play_again = int(input("Make a selection: "))

        if play_again == 1:
            os.system('cls')
            #Checking to be sure the users board size is within the limit. IF it is we create a board object
            while user_width % 2 != 1 or user_width > 15:
                user_width = int(input("Please enter an odd numerical value for the width of the board between 1 and 15: "))
                while turns < 1 or turns > 10:

                    turns = int(input("How many turns would you like (no more than 10): "))

                if user_width % 2 == 1 and user_width < 16:
                    board = gameboard.Board(user_width)

                else:
                    print("That was not an odd numberical value between 1 and 15...")


            #Checking to make sure our board is within regulation. IF it is we create the board and print it to the screen.
            if user_width != len(board.board):

                # if this isn't here the program prints out the previous board as well as the new board.
                board.board = []
                board.create_board()
                #board.print_board()


            #initialize a ship object
            ship_1 = ships.Ship()
            ship_row = ship_1.row(board)
            ship_col = ship_1.col(board)


            #Turn counter and logic to take user guess and check if they are on the board, correct or wrong.
            for turn in range(turns):

                os.system('cls')
                board.print_board()

                #for debugging purposes
                print("The ship is in row: ", ship_row)
                print("The ship is in col: ", ship_col)

                #prints the turn number and prompts the user for their guess
                print("Turn: ", turn + 1, " out of ", turns)
                guess_row = int(input("Guess Row: ")) - 1
                guess_col = int(input("Guess Col: ")) - 1

                #checks to see if the users guess is correct
                if guess_row == ship_row and guess_col == ship_col:
                    print("Congratulations! You sank my battleship!")
                    play_again = 0
                    user_width = 0
                    turns = 0
                    time.sleep(2)
                    break

                else:
                    if guess_row not in range(user_width) or guess_col not in range(user_width):
                        print("Oops, That's not even in the ocean.")
                        time.sleep(1)

                        if turn == turns - 1:
                            os.system('cls')
                            print("Game Over!")
                            play_again = 0
                            user_width = 0
                            turns = 0
                            time.sleep(2)
                            break

                    elif board.board[guess_row][guess_col] == "X":
                        print("You guessed that one alread!")
                        time.sleep(1)

                        if turn == turns - 1:
                            os.system('cls')
                            print("Game Over!")
                            play_again = 0
                            user_width = 0
                            turns = 0
                            time.sleep(2)
                            break
                    else:
                        print("You missed my battleship!")
                        board.board[guess_row][guess_col] = "X"
                        time.sleep(1)

                        if turn == turns - 1:
                            os.system('cls')
                            print("Game Over!")
                            play_again = 0
                            user_width = 0
                            turns = 0
                            time.sleep(2)
                            break


