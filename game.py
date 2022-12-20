class Connect4:
    def __init__(self):
        #6 by 7 board
        self.board = [' ' for _ in range(6*7)]
        self.board_position = [i for i in range(6*7)]

    def print_board(self):
        for i in range(6):
            row = self.board[6*i:6*i+7]
            print('|'+'|'.join(row)+'|')

    def available_move(self):
        # should return a number from 0-6
        # giving the columns of availble moves
        availble = [i for i in range (7) if any([self.board[j]==' ' for j in range(i,42,7)])]
        return availble

    def can_play(self):
        return ' ' in self.board

    def make_move(self,letter):
        col_move = input('Choose a column (0-6):')
        incorrect_move = True
        while incorrect_move:
            try:
                int(col_move)
                if col_move in self.available_move():
                    incorrect_move = False
            except:
                print('The move was incorrect!')
                col_move = input('Choose a column (0-6):')

        position = col_move
        for i in range(1,6):
            if self.board[i*7+col_move] == ' ':
                position = i*7+col_move
            else:
                break
        self.board[position] = letter

        self.is_winning_move(position,letter)

    def is_winning_move(self,position,letter):

        #check in column
        col = position%7
        if position<=14: #we can't pile 4 otherwise
            if all([self.board[position+j*7]==letter for j in range(4)]):
                return True

        #check in row
        row = postion//6
        if any([all([self.board[i+j]==letter for j in range(4) if (i+j)//6==row]) for i in range(position-3,position+1) if i//6 == row]):
            return True

        #check in diagonal 1
        # diagonal 1 is [position -6, position , position+6] if row -1, row, row +1

        for i in range(position-6*3,position,6):
            if 0<=i<=41-4*6:
                rows = []
                result = []

                for j in range(0,4*6,6):
                    rows.append((i+j)//6)
                    result.append(self.board[i+j]==letter)
                rows_set = set(rows)
                if len(rows_set)==len(row)and all(result):
                    return True


        #check in diagonal 2
        # diagonal 2 is [position -8, position , position+8] if row -1, row, row +1




game = Connect4()
game.print_board()
print(game.available_move())
