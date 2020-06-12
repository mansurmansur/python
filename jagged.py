'''
  author: Mansur Mansur
  
  Description: This program makes jagged list. a jagged list is list of lists in python that contains lists of different sizes.
  
  functions: 2 functions
        1. make_jagged(data)
        2. sort_jagged(data)
        
  date: june 11th, 2020
'''

def make_jagged(data):
    '''
       This function removes all zeros from each inner lists and all inner lists should contain only integer values. the function do not return any value.
       
       algorithms:
              I.Traverse through the list of lists and convert all elements in each list to integer if there is error throw an exception and exit the program.
              II. Traverse through the Lists of lists, J equals to 0, a = length of each list
              III. Traverse through each list and remove zeros, J++
       
    '''
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
    '''
       The function sorts the list of lists such that the one with list length comes first by using bubble sort.
       
       Algorithms of bubble sort:
                      I. Traverse through the list of lists
                      II. Traverse the list of lists from 0 to length - i -1
                      III. swap if length of list at j is greater  length of list at j+1
    '''
    #bubble sort
    length = len(data)
    #traverse through the list
    for i in range(length):
        for j in range(0, length - i -1):
            #traverse the list from 0 to length-i-1
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
    sort_jagged(x)
    print(x) # [[], [5], [3, 3, 7], [9, 1, 16, 3], 15, 2, 8, 5, 3]]
    
