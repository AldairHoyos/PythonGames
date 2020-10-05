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

class Wonderer:
    def __init__(self,name,age,warriortype):
        self.name=name
        self.age=age
        self.warriortype=warriortype
    
    def defensemode(self):
        if self.warriortype == "Swordman":
            return "Protecting Shield"
        if self.warriortype == "Bowman":
            return "Avoiding Jump"
        if self.warriortype == "Wizard":
            return "Magic Shield"
        
    def attackmode(self):
        if self.warriortype == "Swordman":
            return "Sword Attack!"
        if self.warriortype == "Bowman":
            return "Arrow Attack!"
        if self.warriortype == "Wizard":
            return "Magic Attack!"

def WarningMessage():
    print("- Wizard: Hello and welcome, you lost traveler! You have entered to a dangerous land.")
    time.sleep(3)
    print("\nYou are in Dragons Land. In front of you, you see two caves.",end="")
    time.sleep(3)
    print(" In one cave there are endless treasures that will make you rich instantly.",end="")
    time.sleep(4)
    print(" Nevertheless, inside the other cave, there is a greedy and hungry dragon that can eat you alive without hesitation if it sees you.")
    time.sleep(3)
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

def WonderersData():
    warriors=["Swordman", "Bowman", "Magician"]
    print("\n- Wizard: What is your name, Wonderer? ")
    name=input("- Wonderer : ")
    print(f"\n- Wizard: How old are you, {name}? ")
    age=int(input(f"- {name} : "))
    while True:
        print("\n- Wizard: What kind of warrior are you? ")
        print("\n1. Swordman")
        print("\n2. Bowman")
        print("\n3. Magician")
        answ=int(input(f"- {name} : "))
        if answ not in set([1,2,3]):
            print("\n- Wizard: you have to be one of the above types of warrior, there are no others")
        else:
            break
    return Wonderer(name, age, warriors[answ-1])

def Battle(warrior,dragon):
    Wlife=2
    Dlife=1
    while Dlife > 0 and Wlife > 0:
        print(f"\n{dragon.name}'s life = {Dlife}")
        print(f"{warrior.name}'s life = {Wlife}")
        dnumber=random.randint(1,3)
        wnumber=random.randint(1,3)
        time.sleep(2)
        if wnumber==dnumber:
            print(f"\n- {dragon.name}: "+dragon.attacks())
            time.sleep(2)
            print(f"\n- {warrior.name}: "+warrior.defensemode())
            time.sleep(2)
            print(f"\n- {warrior.name}: "+warrior.attackmode())
            Dlife=Dlife-1
        else:
            time.sleep(2)
            print(f"\n- {dragon.name}: "+dragon.attacks())
            Wlife=Wlife-1
        time.sleep(1)
    if Dlife == 0:
        print(f"\n- Wizard: You have defeated almighty {dragon.name}, you have been rewarded with treasures beyond your wildest dreams and recognition from all warriors in Dragon's land")
    elif Wlife == 0:
        print("\nLuck was not by your side! You have lost your life in exchage of greed!")

def DragonRealm():
    answ=WarningMessage()
    if answ == 1:
        warrior=WonderersData()  
        print(f"\n - Wizard: Alright {warrior.name}, you have to decide which cave you want to enter to")
        while True:
            print("\nChoose a cave from the followings:")
            print("\n1. Left cave")
            print("\n2. Right cave")
            answ=int(input(f"{warrior.name}'s Decision: "))
            if answ not in set([1,2]):
                print("\n- Wizard: There is not middle ground on this one, my friend.")
            else:
                break
        cave=random.randint(1,2)
        if answ==cave:
            dragon=Dragon()
            dragon.presentation()
            time.sleep(4)
            Battle(warrior,dragon)
        else:
            print("\nYou lucky wonderer! You have made yourself rich!\nYou have found the the most valuable treasure of all time!")
    else:
        print("\nIn that case, you have nothing to do in here, go back where you came from and come back only when you remeber where your guts were!")