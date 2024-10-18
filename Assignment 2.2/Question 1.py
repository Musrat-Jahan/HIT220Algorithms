def sortByColours(numColour):
    low = 0
    mid = 0
    high = len(numColour) - 1
    
    while mid <= high:
        if numColour[mid] == 0:
            numColour[low], numColour[mid] = numColour[mid], numColour[low]
            low += 1
            mid += 1
        elif numColour[mid] == 1:
            mid += 1
        else:
            numColour[high], numColour[mid] = numColour[mid], numColour[high]
            high -= 1
    
    return numColour

# Get user input
user_input = input("Enter a list of numbers separated by spaces or commas: ")

# Convert the input string to a list of integers
numColour = list(map(int, user_input.replace(',', ' ').split()))

# Sort the colors
sorted_list = sortByColours(numColour)
print("Sorted list:", sorted_list)

# Count occurrences of each color
black_count = sorted_list.count(0)
red_count = sorted_list.count(1)
yellow_count = sorted_list.count(2)

# Print color counts
print(f"Count of black (0): {black_count}")
print(f"Count of red (1): {red_count}")
print(f"Count of yellow (2): {yellow_count}")
