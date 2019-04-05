#!/usr/bin/python
# Hèctor Martínez1
# 05/04/2019

import os

# Variables


# Funtions

def welcome():
    '''text of welcome'''
    print ('Welcome to security laboratory!')
    print ('With this program you can learn and practice penetration tests.')
    print ('Enjoi it!')


def environment():
    '''Can select the environment (defualt or personalized)'''
    y = bool(0)
    option = int(0)
    print("You can choose the environment you want")
    print("1. Default")
    print("2. Personalized")  
    while y == 0:
        option = input("select an option (1|2) \n>")
        if option == '1':
            return 1
            y = 1
        elif option == '2':
            return 2
            y = 1


# Estructure

welcome()
environment()

