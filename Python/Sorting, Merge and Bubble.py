#Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.


#importing the libraries
import random 

#Merge sort
def merge_sort(global_arr):
    # If the arr(python list) is empty or has only one element, there is nothing to sort. However, if the arr(python list) has more than 1 element, we continue with the sorting process.

    if len(global_arr) > 1:
        #setting the middle point of the list to divide the list into two parts
        mid = len(global_arr)//2

        #create two new lists, one for the left part and one for the right part.
        left = global_arr[:mid]
        right = global_arr[mid:]

        #call the merge_sort function on the left and right parts.
        merge_sort(left) 
        merge_sort(right)

        #setting variables to compare the left and right lists.
        i = j = k = 0 
        
        #comparing the left and right and iterating over the global_arr.

        while i < len(left) and j < len(right): 
            
            if left[i] < right[j]:
                global_arr[k] = left[i]
                i += 1
            else:
                global_arr[k] = right[j]
                j += 1
            k += 1
        
    print(global_arr)
    return global_arr

#Bubble sort
def bubble_sort(global_arr):
    n = len(global_arr)

    #iterate through the list and swapping the elements if they are in wrong order.
    for i in range(n):
        #subtracting i from the current iteration range because after each iteration, a previously compared element is now in the correct position.
        for j in range(n-i-1):
            if global_arr[j] > global_arr[j+1]:
                global_arr[j], global_arr[j+1] = global_arr[j+1], global_arr[j]

    print(global_arr)
    return global_arr



# A function to generate a list of numbers. Pass in the start and end values of the list. This list will be used by the sorting functions.
def generate_random_array(start, end):
    
    local_arr = [random.randint(start, end) for i in range(100)]
                        
    return local_arr





global_arr = generate_random_array(0, 1000)

bubble_sort(global_arr)
merge_sort(global_arr)