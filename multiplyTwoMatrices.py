# Multiply of Two Matrice using Nested Loop

# Given Array A
arryA = [[7, 4, 5], 
         [2, 8, 3],
         [5, 2, 6]]

# Given Array B
arryB = [[6, 3, 9, 5], 
         [1, 7, 5, 7],
         [3, 9, 2, 8]]

# Sum of Resultant Array
sum = [[0, 0 ,0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

for i in range(len(arryA)): # Loop through rows of array A (arryA)
    for j in range(len(arryB[0])): # Loop through columns of array B (arryB)
        for k in range(len(arryB)): # Loop through rows of array B (arryB)
            sum[i][j] = sum[i][j] + arryA[i][k] * arryB[k][j] # Multiply array A and array B and add with array sum

for s in sum: # Print results
    print(s)