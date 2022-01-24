# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 06:08:15 2022

@author: Uso Personal
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 04:39:07 2022

@author: Aldair Hoyos
"""

class Player:
    def __init__(self, name: str, letter = None):
        self.name = name
        self.letter = None
    
    def __repr__(self):
        return "I'm an addicted player of Tic Tac Toe"
    
    def __str__(self):
        return "Soy" + self.name + "y juego con las" + self.letter + "'s"
    
    def get_letter(self):
        while True:
            letter = input('''Seleccione una letra entre la "O" y la "X": ''').upper()
            if letter not in {"X", "O"}:
                print("\nDebe seleccionar una de las dos opciones, ya sea la X o la O")
                continue
            else:
                self.letter = letter
                break

class Computer(Player):
    def __init__(self, name = "cpu", letter = None):
        super().__init__(name, letter)
        

class TicTacToe:
    board = [" "]*10
    
    def __init__(self, player: Player, cpu: Computer):
        self.player = player
        self.cpu = cpu
    
    @classmethod
    def show_board(cls):
        print("|   {}   |   {}   |   {}   |".format(cls.board[1],cls.board[2],cls.board[3]))
        print("*       *       *       *")
        print("|   {}   |   {}   |   {}   |".format(cls.board[4],cls.board[5],cls.board[6]))
        print("*       *       *       *")
        print("|   {}   |   {}   |   {}   |".format(cls.board[7],cls.board[8],cls.board[9]))
    
    def who_plays_first(self):
        from random import randint
        plays = randint(0, 1)
        if plays == 0:
            return self.cpu.name
        else:
            return self.player.name