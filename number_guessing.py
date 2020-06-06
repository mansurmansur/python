'''
   author: Mansur Mansur
   
   date: June 6, 2020
   
   description: This program randomly chooses a number to guess and then user will have a few chances to guess the number correctly. In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed.
   
   
'''
import random

# -------------------------------------------------------------------------------- #
# function name: generate_number()
# parameters : void
# return: number generated
# -------------------------------------------------------------------------------- #
def generate_number():
    minimum = 1
    maximum = 50
    
    return randrange(minimum,maximum)


# -------------------------------------------------------------------------------- #
# function name: check_number_guessed()
# parameters : user guess and number generated
# return: string
# -------------------------------------------------------------------------------- #
def check_number_guessed():

# -------------------------------------------------------------------------------- #
# function name: user_input()
# parameters : void
# return: none
# -------------------------------------------------------------------------------- #
def user_input():
    a = "1"
    b = "2"
    #infinite loop
    while True:
       print("Welcome to Number Guessing program")
       print("The program generatest numeber which you are given 3 chances to guess")
       print("What would you like to do? \n 1) Play the game \n 2) End the game")
       choice = input()
       
       #validate input
       while True:
          if choice == a or choice == b:
             break
          
          print("INVALID INPUT")
          print("What would you like to do? \n 1) Play the game \n 2) End the game")
          choice = input()
          
       if choice == a:
       
          numeber = generate_number()
          
          #ask user to guess a number
          print("Guess the number choosen by the computer between 1 and 50")
          guess = input()
          
          #check if user got it right
          value = check_number_guessed(numeber, guess)
          
          #
       elif choice == b:
          break
