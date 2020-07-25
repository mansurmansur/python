'''
   Author: Mansur Mansur                          date: 25th July, 2020
   
   Name of program: password generator
   
   Description: This program generates a unique password every time, to help users have a very strong password. Programs ask the user to enter how long the password should be, how many characters, should it be both uppercase and lowercase letter, and should it include numbers nad special symbols.
   
'''

#import random module to make use of random.choice() function
import random


#variables
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_-#!&*" #characters that can be used for password only
password = "";            #password that will be generated
lengthOfPassword = 0;     #int length of desired password


def password_generator(size):
    '''
        this function generates characters from and stores them in the password variable
    '''
    for i in range(1,size):
        password = password + random.choice(char)
        

#main function
if __name__ == "__main__":
   #Prompt user to input how long the password should be
   lengthOfPassword = input("Enter the length of the password: ")
   lengthOfPassword = int(lengthOfPassword)
   
   while(1):
       if isinstance(lengthOfPassword, int):
           break
       else:
           lengthOfPassword=input("Error, Enter an integer number between 1 and 10: ")
   
   #invoke the password generator function
   password_generator(lengthOfPassword)
   
   #print the password generated
   print("Password generated is: {}".format(password))
   
   print("End of the program \U0001f600 !!!")
