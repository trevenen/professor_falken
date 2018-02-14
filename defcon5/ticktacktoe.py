from player import Player
from gameBoard import Board

def insertBoard():
    while(True):
        row = int(input("Enter row: "))
        if row < 1 or row > 3:
            raise ValueError
        break
    while(True):
        col = int(input("Enter column: "))
        if col < 1 or col > 3:
            raise ValueError
        break
    return row-1, col-1


if __name__ == ("__main__"):
    game1 = Board()
    player1 = Player("1", "X")
    player2 = Player("2", "O")
    turns = 0

    while(True):
        while (turns < game1.numberTurns):
            turns += 1
            try:
                print(game1)
                if turns%2 != 0:
                    print("Turn: " + str(turns) + "\t\tPlayer: " + player1.player + "\tSymbol: " + player1.symbol)
                    row, col = insertBoard()
                    game1.insertBoard(row, col, player1.symbol)
                    if game1.checkHorizontal(row, player1.symbol) == True or game1.checkVertical(col, player1.symbol) == True or game1.checkDiagonal(row, col, player1.symbol) == True:
                        print("Player " + player1.player + " wins!")
                        break

                else:
                    print("Turn: " + str(turns) + "\t\tPlayer: " + player2.player + "\tSymbol: " + player2.symbol)
                    row, col = insertBoard()
                    game1.insertBoard(row, col, player2.symbol)
                    if game1.checkHorizontal(col, player2.symbol) == True or game1.checkHorizontal(col, player2.symbol) == True or game1.checkDiagonal(row, col, player2.symbol) == True:
                        print("Player " + player2.player + " wins!")
                        break

            except ValueError:
                turns -= 1
                print("\nValueError: Please enter a valid value!\n1. Value cannot be smaller or larger than the grid.\n2. The space cannot be occupied.\n\n")
            except TypeError:
                turns -= 1
                print("\nTypeError: Please enter an integer!\n\n")
