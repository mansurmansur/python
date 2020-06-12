# Assignment 3, Question 1
# Author: your name here
# McGill ID: your ID here

def make_jagged(data):
    #check if the lists contain integer only if not throw exception
    for i in data:
        for j in i:
            try:
               # convert to integer
               int(j)
            except ValueError:
                print("Error, The lists should only contain integer")
                exit()
                
    #iterate through the data
    for i in data:
        j = 0
        a = len(i)
        while 0 in i and j< a:
            i.remove(0)
            j = j+1

def sort_jagged(data):
    #bubble sort
    length = len(data)
    #traverse through the list
    for i in range(length):
        for j in range(0, length - i -1):
            #traverse the list from 0 to n-i-1
            #swap if the length element at j is greater than lenght of element at j+1
            #then go to next
            if len(data[j]) > len(data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]

# Please do not alter anything below this line.
if __name__ == '__main__':
    x = [[15,  2,  8,  5,  3],
         [ 3,  3,  7,  0,  0],
         [ 9,  1, 16,  3,  0],
         [ 0,  0,  0,  0,  0],
         [ 5,  0,  0,  0,  0]]

    make_jagged(x)
    print(x) # [[15, 2, 8, 5, 3], [3, 3, 7], [9, 1, 16, 3], [], [5]]
    
