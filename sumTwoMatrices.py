# Given Array A
arryA = [[7, 4, 5], 
         [2, 8, 3],
         [5, 2, 6]]

# Given Array B
arryB = [[6, 3, 9], 
         [1, 7, 5],
         [3, 9, 2]]

# Sum of Resultant Array
sum = [[0, 0 ,0],
       [0, 0, 0],
       [0, 0, 0]]

for i in range(len(arryA)): # Loop through rows of array A (arryA)
    for j in range(len(arryA[0])): # Loop through columns of array A [arryA]
        sum[i][j] = arryA[i][j] + arryB[i][j] # Sum the array elements  

for s in sum: # Print the results
    print(s) 
