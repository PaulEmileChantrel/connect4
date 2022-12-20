import random
class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        col_move = input('Choose a column (0-6):')
        incorrect_move = True
        while incorrect_move:
            try:
                col_move = int(col_move)
                if col_move not in game.available_move():
                    raise ValueError
            except ValueError:
                print('The move was incorrect!')
                col_move = input('Choose a column (0-6):')
            else:
                incorrect_move = False
        return col_move

        game.make_move(col_move)

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        col_move = random.choice(game.available_move())
        return col_move
