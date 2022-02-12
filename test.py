#!/usr/bin/env python
# encoding: utf-8
"""
file_name.py

Created by Maz Q-yonk Tea on 9/19/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

########################################################################


import sys
import os
import unittest

# class
class Hero():
    
    # public class variabel
    all_heroes = 0
    
    # private class variable
    _all_heroes_priv = 0
    
    # constructor
    def __init__(self, name, health, power, armor):
        
        # instance public variable
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        
        Hero.all_heroes += 1
		
        # instance private variabel
        '''private variable writen with double underscore in front of variable name'''
        self.__rahasia = "private"
        self.__combo = 0
        self.__fatality = 0
        self.__bonus = 0

        # instance protected variable
        '''private variable writen with single underscore in front of variable name
        behavier just like instance public variable'''
        self._protected = 0
		
        print(f"Hero {name}, Health {health}, Power {power} Armor {armor}")

print(Hero.__dict__)
###############################################################################

















if __name__ == '__main__':
	unittest.main()
########################################################################




def check_main():
	if __name__ == '__main__':
		print(__name__)