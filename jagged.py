# Assignment 3, Question 1
# Author: your name here
# McGill ID: your ID here

def make_jagged(data):
    return None # delete this line and write your code

def sort_jagged(data):
    return None # delete this line and write your code

# Please do not alter anything below this line.
if __name__ == '__main__':
    x = [[15,  2,  8,  5,  3],
         [ 3,  3,  7,  0,  0],
         [ 9,  1, 16,  3,  0],
         [ 0,  0,  0,  0,  0],
         [ 5,  0,  0,  0,  0]]

    make_jagged(x)
    print(x) # [[15, 2, 8, 5, 3], [3, 3, 7], [9, 1, 16, 3], [], [5]]
    
    sort_jagged(x)
    print(x) # [[], [5], [3, 3, 7], [9, 1, 16, 3], [15, 2, 8, 5, 3]]