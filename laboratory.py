#!/usr/bin/python
# Hèctor Martínez
# 05/04/2019

import os

# Variables


# Funtions
def requirments():
    '''show/install the requirments to use this laboratory'''
    os.system("clear")
    print('\n')
    print('REQUIRMENTS:') 
    input("Press ENTER to continue...") 

def welcome():
    '''text of welcome'''
    os.system("clear")
    print('\n')
    print ('Welcome to security laboratory!')
    print ('With this program you can learn and practice penetration tests.\n')
    print ('ENVIRONMENT: ')
    print()
    print(' -------------------------------------')
    print('|                                     |')
    print('|   ---------             ---------   |')
    print('|  |         |           |         |  |')
    print('|  | Server  | <-------> | Client  |  |')
    print('|  |         |           |         |  |')
    print('|   ---------             ---------   |')
    print('|              ---------              |')
    print('|             |         |             |')
    print('|             |  Tester |             |')
    print('|             |  (You)  |             |')
    print('|              ---------              |')
    print('|                                     |')
    print(' -------------------------------------') 
    print()
    print('In this laboratory you will work as if you were a malicious employee of a company. You work with the Virutal machine "Tester".')
    print('Inside the MV tester you have a little tutorials and instructions to practice. This type of pentesting is called "gray box", since you have part of the system information.\n') 
    print('After the installation to acces the MV tester you need type "vagrant ssh" in the console shell.\n')   
    input("Press ENTER to continue...")

def environment():
    '''Select the environment'''
    print("\n")
    print('You can select the environment (defualt or personalized).')
    print('If you select "Defualt" this program create a environment with the services and configurations by default.')
    print('If you select "Personalized" you can chose all server services you want.\n')
    y = bool(0)
    option = int(0)
    print("Choose the environment:")
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
        print('Please type 1 or 2')
def generate_environment():
    '''Generate the environment with Vagrant'''

# Estructure

requirments()  # show/install the requirments to use this laboratory
welcome()  # Welcome to learning
environment()  # Select the environment
generate_environment() 

