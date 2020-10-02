# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:33:42 2020

@author: Aldair Hoyos
"""

import random
import time

class Dragon:
    self.name="Smaug"
    self.color="Green"
    self.age="Two centuries"
    
    def presentation(self):
        return "\nWho dares to awake me from my everlasting dream?\n I am",self.name,"Dragon of all Dragons!\n You interrupted my dream!"
    
    def attacks(self):
        attack=random.randint(1,3)
        if attack == 1:
            return "Breath of fire!"
        elif attack == 2:
            return "Claws!"
        if attack == 3:
            return "Tail!"
        

def WarningMessage():
    print("You are in a land full of dragons. In front of you, you see two caves.",end="")
    time.sleep(3)
    print(" In one cave there is endless treasure that will make you rich instantly.",end="")
    time.sleep(4)
    print(" Nevertheless, inside the other cave, there is a greedy and hungry dragon that can eat you alive without hesitation if it sees you.",end="")
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
    
    