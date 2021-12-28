# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 10:47:03 2021

@author: Aldair Hoyos
"""

class Person():
    def __init__(self, prenom: str, argent : float):
        self.user = prenom
        self.money = argent
    
    #Una representación alternativa para crear una clase persona que este adaptada al juego per se.
    @classmethod
    def fromPerson(cls):
        print("\nEn lo siguiente nos indicará sus datos, por favor")
        name = input("Nombre completo o alias: ")
        while True:
            try:
                money = float(input("Dinero a apostar: "))
                if money <= 0:
                    print("\nIngrese una cantidad válida para jugar")
                else:
                    break
            except:
                print("\nLa cantidad debe expresarla numéricamente, por favor")
        return cls(name,money)
    
class Game():
    win = 0
    lose = 0
    
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
        print("\nAhora, indiquenos la versión del juego que desea jugar:")
        print("\n1. El mejor a un solo intento")
        print("\n2. El mejor a tres intentos")
        print("\n3.El mejor a cinco intentos")
        while True:
            try:
                resp = int(input("Respuesta del jugador: "))
                if resp not in {1,2,3}:
                    print("\nSeleccione una opción válida, por favor.")
                else:
                    break
            except:
                print("\nLa respuesta dada no tiene sentido, seleccione uno de los opciones mostrados, por favor.")
        return resp
    
    @classmethod
    def repeat_menu(cls):
        print("\n¿Desea volver a jugar?")
        print("\n1. Si, quiero jugar de nuevo")
        print("\n2. No, ya fue suficiente")
        while True:
            try:
                resp = int(input("Respuesta del jugador: "))
                if resp not in {1,2}:
                    print("\nSeleccione una opción válida, por favor.")
                else:
                    cls.win, cls.lose = 0, 0
                    break
            except:
                print("\nLa respuesta dada no tiene sentido, seleccione uno de las opciones mostrados, por favor.")
        return resp
    
    @classmethod
    def comparar(cls, opcion, x, y):
        #Realizamos las comparaciones entre las manos de los jugadores y contabilizamos las victorias o derrotas
        if (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
            cls.win += 1
        elif (y == 1 and x == 3) or (y == 2 and x == 1) or (y == 3 and x == 2):
            cls.lose += 1
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
        print("¡Bienvenido al juego de piedra, papel o tijeras!")
        self.player = Person.fromPerson()
        while True:
            opcion = Game.menu()
            while Game.win != opcion and Game.lose != opcion:
                self.player.hand = Game.choise()
                cpu = random.randint(1,3)
                print("\nPiedra, ",end="")
                time.sleep(1)
                print("papel o ",end="")
                time.sleep(1)
                print("tijeras",end="")
                Game.comparar(opcion, self.player.hand, cpu)
                Game.show_results(self.player.hand, cpu)
                time.sleep(1)
            if Game.win > Game.lose:
                time.sleep(1)
                self.player.money*=(2*opcion)
                print(f"\nVictoria para {self.player.user}")
                print(f"\nAhora usted posee la cantidad de {self.player.money} dólares")
                time.sleep(1)
            else:
                time.sleep(1)
                self.player.money = 0
                print(f"\nDerrota para {self.player.user}")
                print("\nAhora usted se quedó sin dinero...")
                time.sleep(1)
            replay = Game.repeat_menu()
            if replay == 1:
                print("\nVolvamos a jugar")
                if self.player.money == 0:
                    try:
                        self.player.money = float(input("Ingrese un nuevo monto a apostar: "))
                        if self.player.money <= 0:
                            print("\nIngrese una cantidad válida para jugar")
                    except:
                        print("\nLa cantidad debe expresarla numéricamente, por favor")
            else:
                break
        print("\nGame over...")
            
            