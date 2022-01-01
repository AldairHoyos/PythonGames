# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:46:09 2022

@author: Aldair Hoyos
"""

class Naipe():
    """Clase para representar un posible naipe de la baraja española"""
    def __init__(self, tipo: int, numero: int):
        self._tipo = tipo
        self._numero = numero
        
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self,value):
        if value not in range(1,5):
            raise ValueError("\nDebe ingresar un tipo de carta con valores entre 1 y 4")
        else:
            self._tipo = value
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self,value):
        if value not in range(1,13):
            raise ValueError("\nDebe ingresar una carta con valores entre 1 y 12")
        else:
            self._numero = value
    
    def __repr__(self):
        return "Carta de la baraja española"
    
    def __str__(self):
        tipos = ("Espadas", "Bastos", "Oro", "Copas")
        return "{} de {}".format(self._numero, tipos[self._tipo-1])
    
    def __lt__(self,otro):
        if self._numero < otro._numero:
            return True
        else:
            return False
    
    def __le__(self,otro):
        if self._numero <= otro._numero:
            return True
        else:
            return False
    
    def __ge__(self,otro):
        if self._numero >= otro._numero:
            return True
        else:
            return False
    
    def __eq__(self,otro):
        if self._numero == otro._numero:
            return True
        else:
            return False
    
    def __ne__(self,otro):
        if self._numero != otro._numero:
            return True
        else:
            return False
