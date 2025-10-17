# Define a function called 'calculator' that takes an 'operation' 
# (like 'add', 'subtract', etc.) and any number of numbers using *args
def calculator(operation, *args):
    
    # If no numbers are provided, print a warning message
    if not args:
        print('No digits provided')
    
    # Check if the operation is 'add'
    if operation == 'add':
        # The built-in sum() adds up all numbers in args
        result = sum(args)
    
    # Check if the operation is 'subtract'
    elif operation == 'subtract':
        # Start with the first number in args
        result = args[0]
        # Loop through the remaining numbers and subtract each one
        for number in args[1:]:
            result -= number
    
    # Check if the operation is 'multiply'
    elif operation == 'multiply':
        # Start with 1 (neutral element for multiplication)
        result = 1
        # Multiply each number in args by result
        for number in args:
            result *= number
    
    # Check if the operation is 'divide'
    elif operation == 'divide':
        # Start with the first number
        result = args[0]
        # Divide result by each of the remaining numbers
        for number in args[1:]:
            result /= number
    
    # Return the final computed result
    return result


# Test cases to show how the function works
print(calculator('subtract', 2, 4, 4))  # => 2 - 4 - 4 = -6
print(calculator('multiply', 2, 4, 4))  # => 2 * 4 * 4 = 32
print(calculator('divide', 2, 4, 4))    # => 2 / 4 / 4 = 0.125