# Program to Calculate Factorial of a Number

# Take input from the user
num = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Check if number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate factorial using loop
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
