Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

SyntaxError: multiple statements found while compiling a single statement
num1= 1.5
num2= 6.3
sum = num1+num2
print('the sum of {0} and {1} is {2}'.format(num1, num2, sum))
the sum of 1.5 and 6.3 is 7.8
