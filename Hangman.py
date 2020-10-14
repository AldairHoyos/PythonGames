# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 08:07:16 2020

@author: Aldair Hoyos
"""
import string
import time

class Hanger():
    def __init__(self):
        self.name="The Hanger"
    
    def hangerword(self):
        while True:
            word=input(f"{self.name}'s hidden word: ")
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
    def __init__(self):
        self.name="Player"
        self.chances=5
        self.lista=list()
    
    def fillblanks(self,word):
        for i in range(len(word)):
            self.lista.append("_")
    
    
    def hangedguess(self):
        while True:
            while True:
                letter=input(f"{self.name}'s guess letter: ")
                if len(letter) > 1:
                    print("\nRemember that you should guess the word letter by letter and not the entire word at once")
                else:
                    break
            if letter not in string.ascii_letters:
                print("\nPlease, choose a valid letter of the english language")
            else:
                break
        return letter
    
def CheckingResult(hanger,hanged,letter):
    while True:
        if letter in hanger.word:
            print("\nYou have guessed  a letter successfully")
            hanged.lista.append(letter)
        else:
            print("\nThe letter you chose is not part of the hidden word")
            hanged.chances=hanged.chances-1

def WelcomingMessage():
    print('\nWelcome to "The Hangman Game".')
    time.sleep(2)
    print("\nIn this game someone will radonmly indicate a word for you to guess.")
    time.sleep(3)
    print("\nConsequently, you will try to guess the entire word by indicating a letter for such word.")
    time.sleep(4)
    print("\nIf the indicated letter appears in the word, it will be displayed for you.")
    time.sleep(4)
    print("\nNevertheless, if you don't guess any letter in the word, you loose a point.")
    time.sleep(3)
    print("\nYou have a total of 5 points with you to try to guess the entire word.")
    time.sleep(3)
    print("\nIf you loose all your points, you loose the game, but if you guess the word, you win!")
    time.sleep(3)
    while True:
        print("\nDo you want to play the game?")
        print("\n1. Yes, I definetely want to play!")
        print("\n2. No, I have better things to do with my life.")
        answ=int(input("Answer from player: "))
        if answ not in set([1,2]):
            print("\nPlease, select one of the possible options.")
            return False
        else:
            break
    return answ
