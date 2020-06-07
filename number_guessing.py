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
    
    num = random.randint(minimum,maximum)
    return num


# -------------------------------------------------------------------------------- #
# function name: userinput_validator()
# parameters : userinput
# return: True or False
# -------------------------------------------------------------------------------- #
def userinput_validator(num):
    try:
      val = int(num)
      return True
    except ValueError:
         return False
         
# -------------------------------------------------------------------------------- #
# function name: check_number_guessed()
# parameters : user guess and number generated
# return: True or False
# -------------------------------------------------------------------------------- #
def check_number_guessed(number, guess):
    #check if user guessed correctly
    if number == guess:
       return True
    elif number > guess:
       print("Number you entered is smaller")
       return False
    elif number < guess:
       print("Number you entered is larger")
       return False

# -------------------------------------------------------------------------------- #
# function name: play()
# parameters : void
# return: none
# -------------------------------------------------------------------------------- #
def play():

  #this terminates the infinite loop when the attemp is 3 times
  number_of_guess = 0
 
  
  #generate the number
  number = generate_number()
  
  while True:
     #terminate the loop if the number of trial is 3
     if number_of_guess == 3:
        print("You  lost the game after 3 trials")
        print("The correct numebr is: {}".format(number))
        break
        
     
     #print out * for the number randomly generated
     if number > 10:
        print("The number to be guessed is: **")
     else:
        print("The number to be guessed is: *")
        
    
     #user input
     print("The number is between 1 and 50")
     print("You have {} attempts to guess the number".format(3-number_of_guess))
     guess = input("Enter the number: ")
     number_of_guess += 1
     
     #invoke the validator function
     while True:
        if userinput_validator(guess) is True:
           try:
             val = int(guess)
           except ValueError:
             val = float(gues)
             
           if val >= 1 or val <= 50:
              break
        
        print("INVALID INPUT")
        guess = input("Enter valid number : ")
     
     #check if the guess is correct
     if check_number_guessed(number, val) is False and number_of_guess != 3:
        print("Please Try again")
        print("You only have {} more try".format(3-number_of_guess))
     elif check_number_guessed(number, val) is True:
        print("You have guessed the correct number which is : {}".format(number))
        print("After {} try".format(number_of_guess))
        break
     


# -------------------------------------------------------------------------------- #
# function name: main()
# -------------------------------------------------------------------------------- #
def main():
    #varibles
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
          #play
          play()
          
       elif choice == b:
          print("See ya !!!")
          print("End of the game")
          break


# ---- invoke the main function ----------#
if __name__ == '__main__':
   main()
