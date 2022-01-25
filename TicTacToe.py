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
        return "Soy un jugador adicto al juego de Tic Tac Toe"
    
    def __str__(self):
        return "Soy " + self.name + " y juego con las " + self.letter + "'s"
    
    def get_letter(self):
        while True:
            letter = input('''Seleccione una letra entre la "O" y la "X": ''').upper()
            if letter not in {"X", "O"}:
                print("\nDebe seleccionar una de las dos opciones, ya sea la X o la O")
                continue
            else:
                self.letter = letter
                break
    
    @staticmethod
    def checkboard(board):
        posible = list()
        for i in range(1,len(board)):
            if board[i] == " ":
                posible.append(i)
        return posible
    
    def make_move(self, board):
        while True:
            try:
                print("\nSeleccione una de las posibiles posiciones en el tablero:\n")
                posible = Player.checkboard(board)
                print("Posiciones disponibles: ", end = " ")
                for i in posible:
                    print(f"{i}", end = ", ")
                select = int(input("Posición: "))
                if select not in posible:
                    print("\nLa opción seleccionada no es válida")
                    continue
                else:
                    break
            except:
                print("\nLa respuesta dada no tiene sentido respecto a las posibles opciones... Escoja de nuevo")
        board[select] = self.letter
        
    def winning(self, board):
        if (board[1] == board[2] == board[3] == self.letter) or (board[4] == board[5] == board[6] == self.letter) or (board[7] == board[8] == board[9] == self.letter):
            return True
        if (board[1] == board[4] == board[7] == self.letter) or (board[2] == board[5] == board[8] == self.letter) or (board[3] == board[6] == board[9] == self.letter):
            return True
        if (board[1] == board[5] == board[9] == self.letter) or (board[3] == board[5] == board[7] == self.letter):
            return True
        return False
    
class Computer(Player):
    def __init__(self, name = "cpu", letter = None):
        self.name = name
        self.letter = letter
        

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
    
    