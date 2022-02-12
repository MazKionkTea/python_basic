#!/usr/bin/env python
# encoding: utf-8
"""
file_name.py

Created by Maz Q-yonk Tea on 13/02/22.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

###############################################################################

import sys
import os
import unittest

###############################################################################

# class
class Hero():
    '''new class with name class Hero'''

    # public class variable / class attributes
    all_heroes = 0
    '''Class attributes are the variables defined directly in the class that are shared by all objects of the class.
    - Defined directly inside a class.
    - Shared across all objects.
    - Accessed using class name as well as using object with dot notation, e.g.
        
        classname.class_attribute or object.class_attribute
    
    - Changing value by using
    
        classname.class_attribute = value
    
    - will be reflected to all the objects.
    '''

    # private class variable / class attributes
    __all_shadow_heroes = 0
    '''private variable writen with double underscore in front of variable name'''

    # constructor / initializer
    def __init__(self, name, health, power, armor) -> None:

        # instance public variable / instance attributes
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        '''Instance attributes are attributes or properties attached to an instance of a class.
        Instance attributes are defined in the constructor.
        - Defined inside a constructor using the self parameter.
        - Specific to object.
        - Accessed using object dot notation e.g.
        
            object.instance_attribute
        
        - Changing value of instance attribute will not be reflected to other objects.
        '''

        # instance private variable / instance attributes
        self.__commbo = 0
        self.__fatality = 0
        self.__bonus_commbo = 0

        # instance protected variable / instance attributes
        '''private variable writen with single underscore in front of variable name
        behavier just like instance public variable'''
        self._protected = 0

        Hero.all_heroes += 1
        '''increment when new hero created'''

        print(f"Hero {name}, Health {health}, Power {power} Armor {armor}")


    # method
    def attack(self, enemy):
        print(f"{self.name} menyerang {enemy.name}")
        enemy.defence(self)
    
    def defence(self, enemy):
        print(f"{self.name} siap bertahan dari serangan {enemy.name}")
        self.revenge(enemy)
    
    def revenge(self, enemy):
        print(f"{self.name} siap siap menyerang balik {enemy.name}")
        self.attack(enemy)
    
    
    
    # encapsulation
    '''make all variable private, to accsess it using geter and seter,'''
    

    # geter (standar)
    def get_instance_attribute(self):
        return self.__commbo, # self.__fatalty self.__bonus
    
    # seter (standar)
    def set_attribute(self, commbo):
        self.__bonus_commbo + commbo
    
    # decorator





###############################################################################


ucup = Hero("ucup", 100, 50, 50)
markonah = Hero("markonah", 100, 50, 50)


###############################################################################

if __name__ == '__main__':
	unittest.main()

def check_main():
	if __name__ == '__main__':
		print(__name__)

###############################################################################