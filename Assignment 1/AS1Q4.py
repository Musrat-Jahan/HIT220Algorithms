def fibonacci(n):
    # Base 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive 
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
print('Fibonacci:',fibonacci(n)) 