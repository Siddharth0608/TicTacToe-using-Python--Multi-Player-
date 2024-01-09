# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:46:17 2022

@author: sid
"""

class TictacToe::
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3 for i in range(3)]]:
            print('|' + '|'.join(row) + '|')
            
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')
            
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, square, letter):
        if self.board == ' ':
            self.board[square] = letter
            if(self.winner(square, letter)):
                self.current_winner = letter
            return True
        return False
        
    
    def empty_squares(self):
        return ' ' in self.board
    
    def empty_squares_num(self):
        return len(self.available_moves())
    
    def winner(self):
        row_ind = square//3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square%3 
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square%2 == 0:
            dia1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in dia1]):
                return True
            dia2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in dia2]):
                return True
            
        return False
    
def play(main, x_player, o_player, print_game = True):
    if print_game:
        main.print_board_nums()
        
    letter = 'X'
    
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
            
        else:
            square = x_player.get_move(game)
            
        if main.make_move(square, letter):
            if print_game:
                print(letter +f'makes a move to {square}')
                main.print_board()
                print(' ')
                
            if main.current_winner:
                if print_game:
                    print(letter + ' wins!')
                
            letter = 'O' if letter == 'X' else 'X' 
            
        time.sleep(1)
            
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTaeToe()
    play(t, x_player, o_player, print_game = True)
    