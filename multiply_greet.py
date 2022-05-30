# Write a function that accepts any number of integers as positional arguments 
# and any number of a student's attributes as keyword arguments
#  and prints the result of multiplying all of the integers with 
#  a customized greeting based on the keyword arguments. 
# Name the function multiply_and_greet.

def multiply_and_greet(*args,**kwargs):
    result = 1
    for num in args:
        result*=num
    print(f"Hello {kwargs['name']} from {kwargs['country']} and ID number { kwargs['ID']}. The result is {result}.")


    