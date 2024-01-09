# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:47:08 2022

@author: sid
"""

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self):
        pass
    
class HumanPlayer:
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        
        while not valid_square:
            square = input('Enter a valid input')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input')
                
                
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, main):
        square = random.choice(main.available_moves())