'''
   author: Mansur Mansur
   
   description: This program implements a binary search algorithm.
   
   Algorithm for binary search: //assuming the array is sorted out.
                 1. Compare x with the middle number.
                 2. if X is equal to the middle number return the index of the middle number.
                 3. Else if x is greater than middle number, X can only lie in the right half subarray
                 4. else x is smaller
                 
                 
   date:  june 6th, 2020
'''
#import array for array creations
import array as arr

def binary_search(list, r, l, num):
  
    if l >= r:
       mid_index = l + (r-1)/2
       #compare mid element with the number
       if num == list[mid_index]:
          return mid_index
       elif list[mid_index] > num:
          binary_search(list, r, mid_index-1, num)
       elif list[mid_index] > num:
          binary_search(list,mid_index+1,l,num)
    else:
       return -1
def main():
    
    #array of sorted numbers
    a = arr.array('i',[2, 4, 9, 15, 24, 29, 45,59,70, 72, 84, 89, 90, 94])
    
   
    #get the middle index
    n = len(list)
    
    #binary search
    index = binary_search(a, 0, n-1, 84)
    
    if index == -1:
       print("The number does not exist in the array.")
    else:
       print("The number exist at index {} in the array.".format(index))
    
    

#invoke the main function
if __name__ == '__main__':
   main()
