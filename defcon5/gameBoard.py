class Board:
    def __init__(self, boardSize=3):
        self.boardSize = boardSize
        self.numberTurns = boardSize*boardSize
        self.gameBoard = [[" "]*boardSize for n in range(boardSize)]

    def __str__(self):
        board = ""
        for i in range(self.boardSize):
            row = self.printBoard(i)
            for content in self.printBoard(i):
                board += "|" +  content + "|"
            board += "\n"
        return board

    def printBoard(self, row):
        return self.gameBoard[row]

    def insertBoard(self, row, col, symbol):
        if self. gameBoard[row][col] == " ":
            self.gameBoard[row][col] = symbol
        else:
            raise ValueError

    def checkHorizontal(self, row, symbol):
        for i in range(self.boardSize):
            if symbol != self.gameBoard[row][i]:
                return False
        return True

    def checkVertical(self, col, symbol):
        for i in range(self.boardSize):
            if symbol != self.gameBoard[i][col]:
                return False
        return True

    def checkDiagonal(self, row, col, symbol):
        validPosition = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
        if [row, col] in validPosition:
            if self.diagonalLeft(row, col, symbol) == True or self.diagonalRight(row, col, symbol) == True:
                return True
        return False

    def diagonalLeft(self, row, col, symbol):
        for i in range(self.boardSize):
            if symbol != self.gameBoard[i][i]:
                return False
        return True

    def diagonalRight(self, row, col, symbol):
        x = 0
        y = 2

        for i in range(self.boardSize):
            if self.gameBoard[x][y] == symbol:
                x+1
                y-1
            else:
                return False
        return True

