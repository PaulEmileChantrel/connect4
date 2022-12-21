import random
import math

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

class SmartComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if game.num_of_empty()==42:
            col_move = random.choice(game.available_move())
        else:
            col_move = self.minimax(game,self.letter,6)
            col_move = col_move['position']

        return col_move

    def minimax(self,state,player,n):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        #base case
        if state.current_winner == other_player :
            return {'position':None,'score':1*(state.num_of_empty()+1) if other_player==max_player else -1*(state.num_of_empty()+1)}
        elif state.num_of_empty()==0 :#no move left
            return {'position':None,'score':0}
        elif n == 0:
            return {'position':None,'score':0.5*(state.num_of_empty()+1) if other_player==max_player else -0.5*(state.num_of_empty()+1)}


        if player==max_player:
            best = {'position':None,'score':-math.inf}#we want to maximize the score
        else:
            best = {'position':None,'score':math.inf}#we want to minimize the score
        moves = state.available_move()
        random.shuffle(moves)
        for possible_move in moves: #We suffle the array to avoid aving 0 as a fist move all the time
            #step 1 -> play a move
            position = state.make_move(possible_move,player)

            #step 2 -> recursively play every other move
            sim_score = self.minimax(state,other_player,n-1)

            #step 3 -> cancel the moves
            state.board[position] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            #step 4 -> update score
            if player == max_player:
                if sim_score['score']>best['score']:
                    best = sim_score
            else:
                if sim_score['score']<best['score']:
                    best = sim_score

        return best
