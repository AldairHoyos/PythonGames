# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:33:42 2020

@author: Aldair Hoyos
"""

import random
import time

class Dragon:
    def __init__(self):
        self.name="Smaug"
        self.color="Green"
        self.age="Two centuries"
    
    def presentation(self):
        print(f"\nWho dares to awake me from my everlasting dream? I am {self.name}, Dragon of all Dragons! You interrupted my dream and for that, you must pay with your life!")
    
    def attacks(self):
        attack=random.randint(1,3)
        if attack == 1:
            return "Breath of fire!"
        elif attack == 2:
            return "Claws!"
        if attack == 3:
            return "Tail!"

def WarningMessage():
    print("Wizard: Hello and welcome, you lost traveler! You have entered to a dangerous land.")
    print("\nYou are in Dragons Land. In front of you, you see two caves.",end="")
    time.sleep(3)
    print(" In one cave there are endless treasures that will make you rich instantly.",end="")
    time.sleep(4)
    print(" Nevertheless, inside the other cave, there is a greedy and hungry dragon that can eat you alive without hesitation if it sees you.")
    while True:
        print("\nDo you want to take a chance and enter to one of the caves and see if you're lucky one way or the other?")
        print("\n1. Yes, fortune rewards risky people! I have nothing to fear.")
        print("\n2. No, I love my life! There are more things in life than money or treasure.")
        answ=int(input("Answer from traveler: "))
        if answ not in set([1,2]):
            print("\nI understand that you're afraid but try to give me an answer that has sense.")
        else:
            break
    return answ

def DragonRealm():
    answ=WarningMessage()
    if answ == 1:
        print("\nAlright wonderer, you have to decide which cave you want to enter to")
        while True:
            print("\nChoose a cave from the followings:")
            print("\n1. Left cave")
            print("\n2. Right cave")
            answ=int(input("Decision: "))
            if answ not in set([1,2]):
                print("\nThere is not middle ground on this one, my friend.")
            else:
                break
        cave=1
        if answ==cave:
            dragon=Dragon()
            dragon.presentation()
            time.sleep(4)
            print(f"\n{dragon.name} attack: " + dragon.attacks())
            time.sleep(2)
            print("\nLuck was not with you! You have lost your life in exchage of greed!")
        else:
            print("\nYou lucky wonderer! You have made yourself rich!\nYou have found the the most valuable treasure of all time!")
    else:
        print("\nIn that case, you have nothing to do in here, go back where you came from and come back only when you remeber where your guts were!")