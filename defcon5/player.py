class Player:
    def __init__(self, player, symbol):
        self.player = player
        self.symbol = symbol

    def __str__(self):
        return "Player: " + str(self.player) + "\nSymbol: " + str(self.symbol)
