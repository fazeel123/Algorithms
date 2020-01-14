# Insertion Sort Function with Single Parameter
def insertionSort(arry):
    # Loop through the given Array (arry)
    for j in range(1, len(arry)):
        key = arry[j] # Store the array key for every iteration
        i = j - 1 # Sort the array sequence for arry[1...i-1]
        # Compare the key with array sequence arry[j]
        while i >= 0 and key < arry[i]:
            arry[i + 1] = arry[i] # Move one postion for array values to right  
            i -= 1 # Sort the array sequence for arry[1...i-1]
        arry[i + 1] = key # Sort key position in descending order i.e. A = [aa' <= ab' <= ac' .... <= an']

# Given Array
arry = [23, 45, 90, 12, 6, 3, 11]

# Function Call
insertionSort(arry)

# Loop through the given array
for i in range(len(arry)):
    print("% d " % arry[i]) # Print the results