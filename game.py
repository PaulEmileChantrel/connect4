from player import HumanPlayer,RandomComputerPlayer
import time
class Connect4:
    def __init__(self):
        #6 by 7 board
        self.board = [' ' for _ in range(6*7)]
        self.board_position = [i for i in range(6*7)]
        self.current_winner = None

    def print_board(self):

        for i in range(6):
            row = self.board[7*i:7*i+7]
            print('|'+'|'.join(row)+'|')
    @classmethod
    def print_moves(cls):
        print('|0|1|2|3|4|5|6|')
    @classmethod
    def print_board_nums(cls):
        for i in range(6):
            row = [str(j) for j in range(7*i,7*i+7)]
            print('|'+'|'.join(row)+'|')
    def available_move(self):
        # should return a number from 0-6
        # giving the columns of availble moves
        availble = [i for i in range (7) if any([self.board[j]==' ' for j in range(i,42,7)])]
        return availble

    def can_play(self):
        return ' ' in self.board

    def make_move(self,col_move,letter):
        #col_move = input('Choose a column (0-6):')

        position = col_move
        for i in range(1,6):
            if self.board[i*7+col_move] == ' ':
                position = i*7+col_move
            else:
                break
        self.board[position] = letter

        return position
        #self.is_winning_move(position,letter)

    def is_winning_move(self,position,letter):

        #check in column
        col = position%7
        if position<21: #we can't pile 4 otherwise
            if all([self.board[position+j*7]==letter for j in range(4)]):
                return True
        
        #check in row
        row = position//7

        if any([all([self.board[i+j]==letter for j in range(4)] ) for i in range(position-3,position+1) if i//7==row and (i+3)//7==row]):
            return True

        #check in diagonal 1
        # diagonal 1 is [position -6, position , position+6] if row -1, row, row +1

        for i in range(position-6*4,position+1,6):
            print(i)
            if 3<=i<=20:#doesnt work for i outside
                rows = []
                result = []

                for j in range(0,4*6,6):
                    rows.append((i+j)//7)
                    result.append(self.board[i+j]==letter)
                rows_set = set(rows)
                if len(rows_set)==len(rows)and all(result):
                    return True


        #check in diagonal 2
        # diagonal 2 is [position -8, position , position+8] if row -1, row, row +1
        for i in range(position-8*4,position+1,8):
            if 0<=i<=41-3*8:#doesnt work for i outside
                rows = []
                result = []

                for j in range(0,4*8,8):
                    rows.append((i+j)//7)
                    result.append(self.board[i+j]==letter)
                rows_set = set(rows)
                if len(rows_set)==len(rows)and all(result):
                    return True

        return False


def play(game,x_player,o_player,print_game=True):
    if print_game:
        Connect4.print_board_nums()
        game.print_board()
    letter = 'X'
    current_player = x_player
    while game.can_play():
        move = current_player.get_move(game)
        position = game.make_move(move,letter)
        if game.is_winning_move(position,letter):
            game.print_board()
            print(f'Congrats! Player {letter} won the game!')
            return
        current_player = o_player if current_player == x_player else x_player
        letter = current_player.letter
        if print_game:
            Connect4.print_moves()
            game.print_board()
        time.sleep(1)

    print(f'It\'s a tie!')

if __name__ =='__main__':
    game = Connect4()
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    play(game,x_player,o_player,print_game=True)
