# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:07:16 2020

@author: Aldair Hoyos
"""
import string

class Hanger():
    def __init__(self,name):
        self.name=name
    
    def hangerword(self):
        while True:
            word=list(input(f"{self.name}´s hidden word: "))
            val=True
            for i in range(len(word)):
                if word[i] not in string.ascii_letters:
                    val=False
            if val==False:
                print("\nPlease, choose a valid word of the english language")
            else:
                print("\nNice pick, my friend")
                break
        self.word=word
        
    
class HangedMan():
    def __init__(self,name,chances):
        self.name=name
        self.chances=chances
    
    def hangedguess(self):
        while True:
            while True:
                letter=input(f"{self.name}´s guess letter: ")
                if len(letter) > 1:
                    print("\nRemember that you should guess the word letter by letter and not the entire word at once")
                else:
                    break
            if letter not in string.ascii_letters:
                print("\nPlease, choose a valid letter of the english language")
            else:
                break
        return letter
                        
            
    
        
        