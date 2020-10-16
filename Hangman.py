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
                print("\nPlease, choose a valid word of the english language.")
            else:
                print("\nNice pick, my friend.")
                break
        self.word=word
        
class HangedMan():
    def __init__(self):
        self.name="Player"
        self.chances=5
        self.lista=list()
    
    def fillblanks(self,word):
        self.lista=list()
        for i in range(len(word)):
            self.lista.append("_")
    
    def hangedguess(self):
        while True:
            while True:
                letter=input(f"{self.name}'s guess letter: ")
                if len(letter) > 1:
                    print("\nRemember that you should guess the word letter by letter and not the entire word at once.")
                else:
                    break
            if letter not in string.ascii_letters:
                print("\nPlease, choose a valid letter of the english language.")
            else:
                break
        return letter
    
def LookInWord(hanged,letter,word):
    for i in range(len(word)):
        if letter == word[i]:
            hanged.lista[i]=letter
        else:
            pass

def ShowResult(hanged):
    print(f"\n{hanged.name}'s chances: {hanged.chances}.")
    print(f"\n{hanged.name}'s result: ",end="")
    for i in range(len(hanged.lista)):
        print(hanged.lista[i],end=" ")
    
def CheckingResult(hanger,hanged):
    picks=list()
    ShowResult(hanged)
    while True:
        print("\n")
        letter=hanged.hangedguess()
        if letter in picks:
            print("\nYou have already said this letter before, choose another one.")
        elif letter in hanger.word:
            print("\nYou have guessed a letter successfully.")
            picks.append(letter)
            LookInWord(hanged,letter,hanger.word)
            ShowResult(hanged)
        else:
            print("\nThe letter you chose is not part of the hidden word.")
            picks.append(letter)
            hanged.chances=hanged.chances-1
            ShowResult(hanged)
        if hanged.chances==0 or hanged.lista==list(hanger.word):
            break
        
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

def Playagain():
    while True:
        print("\nDo you want to play again?")
        print("\n1. Yes, I definetely want to play again!")
        print("\n2. No, enough is enough.")
        answ=int(input("Answer from player: "))
        if answ not in set([1,2]):
            print("\nPlease, select one of the possible options.")
        else:
            break
    return answ

def TheHangmanGame():
    play = WelcomingMessage()
    if play == 2:
        print("\nAlright, my friend! come back whenever you want to play.")
    else:
        print("\nGreat! I knew that you wanted to play.")
        hanger=Hanger()
        player=HangedMan()
        while True: 
            hanger.hangerword()
            player.fillblanks(hanger.word)
            CheckingResult(hanger,player)
            if player.chances==0:
                print("\n\nYou could not guessed the word. You have lost the game, my friend.")
            else:
                print(f"\n\nCongratulations, {player.name}! You have won the game!")
            answ=Playagain()
            if answ == 1:
                print("\nThat's the kind of people I like the most! Keep on playing!")
                hanger.word=""
            else:
                print("\nGoodbye, My friend. See you next time!")
                break