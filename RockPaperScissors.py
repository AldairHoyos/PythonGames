# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:47:03 2021

@author: Uso Personal
"""

class Person():
    def __init__(self, prenom: str, argent : float):
        self.user = prenom
        self.money = argent
    
class Game():
    def __init__(self, jouer1: Person):
        self.player = jouer1
        self.win = 0
        self.lose = 0
    
    @staticmethod
    def choise():
        print("\nSeleccione una opción:")
        while True:
            print("\n1. Piedra")
            print("\n2. Papel")
            print("\n3. Tijera")
            try:
                resp = int(input("Respuesta: "))
                if resp not in {1,2,3}:
                    print("\nDebe seleccionar una opción valida, por favor.")
                else:
                    break
            except:
                print("\nLa respuesta dada no se encuantra entre las posibles propuestas, seleccione un valor numérico, por favor.")
        return resp
    
    @staticmethod
    def menu():
        print("Indiquenos la versión del juego que desea jugar:")
        print("\n1. El mejor a un solo intento")
        print("\n2. El mejor a tres intentos")
        print("\n3.El mejor a cinco intentos")
        while True:
            try:
                resp = int(input("Respuesta del juegador: "))
                if resp not in {1,2,3}:
                    print("\nSeleccione una opción válida, por favor.")
                else:
                    break
            except:
                print("\nLa respuesta dada no tiene sentido, seleccione uno de los valores mostrados, por favor.")
        return resp
    
    def comparar(self, x, y):
        if (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
            self.win += 1
        elif (y == 1 and x == 3) or (y == 2 and x == 1) or (y == 3 and x == 2):
            self.lose += 1
        else:
            pass
    
    @staticmethod
    def show_results(x,y):
        import time
        result = ("Piedra", "Papel", "Tijeras")
        print(f"\n\n{result[x-1]} Vs ", end = "")
        time.sleep(1)
        print(f"{result[y-1]}")
        time.sleep(1)
        if x == 1:
            if y == 1:
                print("\n¡Empate!")
            elif y == 2:
                print("\n¡Derrota!")
            else:
                print("\n¡Victoria!")
        elif x == 2:
            if y == 1:
                print("\n¡Victoria!")
            elif y == 2:
                print("\n¡Empate!")
            else:
                print("\n¡Derrota!")
        else:
            if y == 1:
                print("\n¡Derrota!")
            elif y == 2:
                print("\n¡Victoria!")
            else:
                print("\n¡Empate!")
                
    def rock_paper_scissors(self):
        import random
        import time
        print(f"Bienvenido {self.player.user} al juego de piedra, papel o tijeras")
        opcion = Game.menu()
        while self.win != opcion and self.lose != opcion:
            self.player.hand = Game.choise()
            cpu = random.randint(1,3)
            print("\nPiedra, ",end="")
            time.sleep(1)
            print("papel o ",end="")
            time.sleep(1)
            print("tijeras",end="")
            Game.comparar(self, self.player.hand, cpu)
            Game.show_results(self.player.hand, cpu)
        if self.win > self.lose:
            print(f"\nVictoria para {self.player.user}")
        else:
            print(f"\nDerrota para {self.player.user}")
            