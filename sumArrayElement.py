# Sum of Array Element
def sumArrayElement(arry, n):
    s = 0 # Variable
    for i in range(0, n): # Loop for array summation
        s = s + arry[i] # Sum the current array element with right element
        print("%d " % s) # Print the results
        

arry = [9, 3, 5, 2, 6, 8] # Given Array
n = 6 # Given Frequency for Looping
sumArrayElement(arry, n) # Call Function