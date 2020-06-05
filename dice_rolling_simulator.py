'''
   Author: Mansur Mansur
   
   Description: This program simulates rolling dice. When the program runs, it randomly choose a number between 1 and 6. It will print out the number which turns when a die is rolled. The program allows the user to roll the dice a many times a possible.
   
   date: June 4th, 2020.
   
'''
import random

# -------------------------------------------------------------------------------- #
# function name: generate_random_number()
# description: generates random number
# parameter: void
# -------------------------------------------------------------------------------- #
def generate_random_number():
    #set the minimum and maximum variable
    mininmum = 1
    maximum  = 6
    
    #generate the random number
    die = randrange(mininmum, maximum)
    
    #return the generated number
    return die


# -------------------------------------------------------------------------------- #
# function name: main()
# description: it is the main function. where the execution starts. it asks user
#               play or exit the game. when user chooses play it will invoke the
#               generate_random_number. and then it prints out the number
# parameter: void
# -------------------------------------------------------------------------------- #
def main():
   #variables
    a = "1"
    b = "2"

    
    #infinite loop
    while True:
      print("Welcom to Die rolling simulator")
      print("This programs allows you to roll die and check the number you got")
      print("What would like to do ? \n 1) Roll the die. \n 2) End the simultor")
      user_input = input()
      
      #validating the user input
      while True :
          if user_input == a or user_input == b :
             break
             
          print("INVALID INPUT")
          print("What would like to do ? \n 1) Roll the die. \n 2) End the simultor")
          user_input = input()
        
              
      #choice
      if user_input == a :
         value = generate_random_number()
         print("The number on the die is: {}".format(value))
      elif user_input == b:
         print("See ya \n End of th Program")
         break



#invoke the main function
if __name__ == '__main__':
   main()
         
            
    
