
class Player:
    def __init__(self,letter):
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(self,letter)

    def make_move(self):


class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(self,letter)
