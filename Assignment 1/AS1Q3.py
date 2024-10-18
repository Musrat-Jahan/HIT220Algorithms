def product_of_sequence(sequence):
    product = 1 
    
    for number in sequence:  
        product *= number  
    
    return product  


sequence = [2, 3, 4, 5]  
print('Product :', product_of_sequence(sequence))  
