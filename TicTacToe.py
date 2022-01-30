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
    
    def other_letter(self, cpu_letter):
        if cpu_letter == "X":
            self.letter = "O"
        else:
            self.letter = "X"
    
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
                posible = Player.checkboard(board)
                if posible == []:
                    return "Ya no hay posiciones disponibles en el tablero"
                print("\nSeleccione una de las posibiles posiciones en el tablero:\n")
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
    
class Computer:
    def __init__(self, name = "cpu", letter = None):
        self.name = name
        self.letter = letter
    
    def get_letter(self):
        while True:
            letter = input('''Seleccione una letra entre la "O" y la "X": ''').upper()
            if letter not in {"X", "O"}:
                print("\nDebe seleccionar una de las dos opciones, ya sea la X o la O")
                continue
            else:
                self.letter = letter
                break    
    
    def other_letter(self, player_letter):
        if player_letter == "X":
            self.letter = "O"
        else:
            self.letter = "X"
    
    #Developping the strategic for making the best move
    
    def win_horizontal(self,board):
        for j in [1,4,7]:
            count, val = 0, True
            for i in [0,1,2]:
                if board[j+i] == " ":
                    position = j+i
                    continue
                elif board[j+i] != " " and board[j+i] != self.letter:
                    val = False
                    break
                else:
                    count +=1
            if count == 2 and val == True:
                board[position] = self.letter
                return True
        return False
    
    def win_vertical(self,board):
        for j in [1,2,3]:
            count, val = 0, True
            for i in [0,3,6]:
                if board[j+i] == " ":
                    position = j+i
                    continue
                elif board[j+i] != " " and board[j+i] != self.letter:
                    val = False
                    break
                else:
                    count +=1
            if count == 2 and val == True:
                board[position] = self.letter
                return True
        return False
    
    def win_diagonal(self,board):
        count , val = 0, True
        for i in [1,5,9]:
            if board[i] == " ":
                position = i
            elif board[i] != " " and board[i] != self.letter:
                val = False
                break
            else:
                count += 1
        if count == 2 and val == True:
            board[position] = self.letter
            return True
        return False
        
        count , val = 0, True
        for i in [3,5,7]:
            if board[i] == " ":
                position = i
            elif board[i] != " " and board[i] != self.letter:
                val = False
                break
            else:
                count += 1
        if count == 2 and val == True:
            board[position] = self.letter
            return True
        return False
    
    def block_horizontal(self, board, player_letter):
        for i in [1,4,7]:
            count, val = 0, True
            for j in [0,1,2]:
                if board[i+j] == " ":
                    position = i+j
                elif board[i+j] != " " and board[i+j] != player_letter:
                    val = False
                    break
                else:
                    count += 1
            if count == 2 and val == True:
                board[position] = self.letter
                return True
        return False
    
    def block_vertical(self, board, player_letter):
        for i in [1,2,3]:
            count, val = 0, True
            for j in [0,3,6]:
                if board[i+j] == " ":
                    position = i+j
                elif board[i+j] != " " and board[i+j] != player_letter:
                    val = False
                    break
                else:
                    count += 1
            if count == 2 and val == True:
                board[position] = self.letter
                return True
        return False
    
    def block_diagonal(self, board, player_letter):
        count, val = 0, True
        for i in [1,5,9]:
            if board[i] == " ":
                position = i
            elif board[i] != " " and board[i] != player_letter:
                val = False
                break
            else:
                count += 1
        if count == 2 and val == True:
            board[position] = self.letter
            return True
        
        count, val = 0, True
        for i in [3,5,7]:
            if board[i] == " ":
                position = i
            elif board[i] != " " and board[i] != player_letter:
                val = False
                break
            else:
                count += 1
        if count == 2 and val == True:
            board[position] = self.letter
            return True
        return False
    
    @staticmethod
    def posible_options(board):
        posible = list()
        for i in range(1,10):
            if board[i] == " ":
                posible.append(i)
        return posible
    
    def pick_position(self,board, posible):
        import random
        position = random.choice(posible)
        board[position] = self.letter

class TicTacToe:
    board = [" "]*10
    def __init__(self, player: Player, cpu: Computer):
        self.player = player
        self.cpu = cpu
    
    @staticmethod
    def show_board(board):
        copy = board.copy()
        copy.reverse()
        for i in [1,4,7]:
            print("|   {}   |   {}   |   {}   |\n".format(copy[i], copy[i+1], copy[i+2]))
            
    @classmethod
    def board_restart(cls):
        cls.board = [" "]*10
    
    @classmethod
    def draw(cls):
        val = True
        for i in range(1,10):
            if cls.board[i] == " ":
                val = False
                break
        return val
    
    def who_plays_first(self):
        from random import randint
        plays = randint(0, 1)
        if plays == 0:
            return self.cpu
        else:
            return self.player
    
    def change_turn(self,turn):
        if turn == self.cpu:
            return self.player
        else:
            return self.player
    
    @classmethod
    def play_the_game(cls):
        game = cls(Player("player"), Computer())
        turn = game.who_plays_first()
        print("\nJuega primero {}".format(turn.name))
        if turn == game.cpu:
            turn.get_letter()
            game.player.other_letter(game.cpu.letter)
        else:
            turn.get_letter()
            game.cpu.other_letter(game.cpu.letter)
        while True:
            if turn == game.cpu:
                wincpu = turn.win_horizontal(cls.board)
                if wincpu == False:
                    wincpu = turn.win_vertical(cls.board)
                    if wincpu == False:
                        wincpu = turn.win_diagonal(cls.board)
                        if wincpu == False: #Verificar que tengo que bloquear al oponente
                            val = turn.block_horizontal(cls.board,game.player.letter)
                            if val == False:
                                val = turn.block_vertical(cls.board,game.player.letter)
                                if val == False:
                                    val = turn.block_diagonal(cls.board,game.player.letter)
                                    if val == False: #Jugamos aleatorimente
                                        turn.pick_position(cls.board, game.cpu.posible_options(cls.board))
                if wincpu == True:
                    print("\nHa ganado la computadora")
                    break
                elif wincpu == False and cls.draw() == True:
                    print("\nHay un empate entre los oponentes")
                    break
                else:
                    turn = game.player
            else:
                turn.make_move(cls.board)
                if turn.winning(cls.board) == True:
                    print("\nHa ganado el jugador")
                    break
                elif turn.winning(cls.board) == False and cls.draw() == True:
                    print("\nHay un empate entre los oponentes")
                    break
                else:
                    turn = game.cpu
        cls.board_restart()

#Hay que resolver el despliegue del tablero en pantalla.
                
        
        
        
        
        
        
        