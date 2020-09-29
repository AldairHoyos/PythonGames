# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 07:48:51 2020

@author: Aldair Hoyos
"""

import random
import time


class Player:
    def __init__(self,name,tries,bet):
        self.name=name
        self.tries=tries
        self.bet=bet
        self.options=list()
  
    
def WelcomeMessage():
    print("Welcome to our humble place of amusement")
    time.sleep(2)
    print("\nWe want to offer you a simple game but fun and profitable")
    time.sleep(3)
    print("\nThe game consists on guessing a number between 1 and 20 and you will have six tries to guess it")
    time.sleep(3)
    print("\nIf you guess the number you'll win twice the money you bet but on the other hand, if you loose, you loose the money you bet")
    time.sleep(4)
    print("\nDo you want to enter and play?")
    print("\n1. Yes, it would be a placer to do so")
    print("\n2. No, I'm okey but thanks a lot!")
    while True:
        resp=int(input("Answer from stranger: "))
        if resp not in set([1,2]):
            print("\nSorry but you have to give us a right answer for this, thre's no middle ground")
        else:
            break
    if resp==2:
        print("\nIt's such a shame that you've decided that, I hope you change your mind any time soon")
    else:
        print("\nPerfect! You have taken a great choice, my friend")
    return resp
    
def GuessTheNumber():
    resp=WelcomeMessage()
    if resp==1:
        name=input("Tell us your name, please: ")
        while True:
            bet=float(input("Tell us how much do you want to bet on this game: "))
            if bet <= 0:
                print("\nYou cannot bet with magic money, my friend. Give us a real amount")
            else:
                break
        player=Player(name,6,bet)
        hiddennumber=random.randint(1, 21)
        while player.tries > 0:
            print("\nYou have",player.tries,"tries to guess the number")
            while True:
                guess=int(input("Choose a number between 1 and  20: "))
                if guess < 1 or guess > 20:
                    print("\nSelect a number between the valid range")
                else:
                    player.options.append(guess)
                    break
            if hiddennumber == guess:
                print("\nWe have a winner! You have guessed the right number")
                print("\nYou have won",player.bet,"dollars")
                break
            else:
                player.tries=player.tries-1
                time.sleep(1)
                print("\nSorry but you have made a wrong guess")
                if player.tries > 0:
                    if hiddennumber < guess:
                        time.sleep(1)
                        print("\nThe real number is lower than you might think")
                    else:
                        time.sleep(1)
                        print("\nThe real number is higher than you might think")
                else:
                    time.sleep(1)
                    print("\nYou have run out of guesses, my friend")
                    time.sleep(1)
                    print("\nThe number that we chose for you was: ",hiddennumber)
                    time.sleep(1)
                    print("\nYou have lost",player.bet,"dollars")                    
            
        
    
      