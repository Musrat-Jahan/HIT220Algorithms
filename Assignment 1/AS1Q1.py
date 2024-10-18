def contains(stackName, search):
    # Temporary stack to help with processing
    tempStack = []
    
    # Initialize search tracking
    found = False
    searchIndex = 0
    
    # Process elements to find the search string
    while stackName:
        char = stackName.pop()  # Remove element from original stack
        tempStack.append(char)  # Save removed element in tempStack
        
        if char == search[searchIndex]:
            searchIndex += 1
            if searchIndex == len(search):
                found = True
                break
        else:
            searchIndex = 0
    
    # Restore the original stack order
    while tempStack:
        stackName.append(tempStack.pop())
    
    return found


stackName = [2, 0, 1, 3, 6]
search = "136"
print(contains(stackName, search)) 
print(stackName) 
