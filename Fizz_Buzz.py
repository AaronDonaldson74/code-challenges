"""
So we're going to write a program that prints the numbers from 1 to 100 but for multiples of 3 it prints Fizz. So it prints a string of fizz instead of the number and for the multiples of five it prints Buzz for the numbers which are multiples of both 5 and 3 then you're going to print out fizz buzz. And so just to give an idea of what this is going to look like you're going to print out something that is 1, 2, 3, 4, and 5. But instead of where we have a number 3 right here, this instead is going to be the string Fizz and instead of the number 5 this is going to be Buzz.
"""

"""Psuedo

1.Print 1-100 -use a loop function for x in numbers etc.
2.set condition if number / 3 is modulous 0 then return fizz
3.set condition if number / 5 is modulous 0 then return buzz
4.set condition elif number / 3 AND number / 5 is modulous 0 then FizzBuzz.
5.set maximum at a variable input by user. 
"""


# def fizz_buzz():
#     max_value = input("Enter Maximum Count Value:")

#     max_value = int(max_value)

#     numbers = range(1, (max_value + 1))

#     for num in numbers:
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")
#         else:    
#             print(num)

# fizz_buzz()

def fizz_buzz(max):

    numbers = range(1, (max+1))
    
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:    
            print(num)

fizz_buzz(100)