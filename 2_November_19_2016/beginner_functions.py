# Your first function is a simple one: a function called multiply that will return the product of two numbers
def multiply(num1, num2):
    # replace 'None' with your code for multiplication
    product = None
    return product

# Now create a function called division - but remember that you can't divide by 0!
def division(dividend, divisor):
    if divisor == 0:
        print "You can't divide by zero!"
        return None
    else:
        # Replace 'None' with your code for division
        quotient = None
        return quotient

""" Before moving on, make sure that you understand or ask questions about the
'if' and 'else' statements that you encounter.  These are logical "gates", so you can
read the `if diviosr == 0` as "if the divisor (the bottom number) is equal to zero, then...".
Notice that if/else statements can be super useful for handling different cases and behaviors.
"""

# All right, now let's get a little trickier - write a function that returns the remainder of a division problem
def remainder(dividend, divisor):
    # Replace 'None' with your code for finding the remainder
    # Hint: Google the function 'modulo', which in python is represented by `%`
    remainder = None
    return remainder

# Lastly, define a function that returns whether or not a number is prime.  
# Remember that a number is prime if and only if its only factors are 1 and itself
def is_prime(number):
    prime = None
    pass

if __name__ == '__main__':
    print "testing multiply: (3,4) should return 12, did return {}".format(multiply(3,4))
    print "testing division: (10,2) should return 5, did return {}".format(division(10,2))
    print "testing division: (10,0) should print warning and return None, did return {}".format(division(10,0))
    print "testing remainder: (10,3) should return 1, did return {}".format(remainder(10,3))
    print "testing remainder: (9,3) should return 0, did return {}".format(remainder(9,3))
    print "testing is_prime: 1 should return False, did return {}".format(is_prime(1))
    print "testing is_prime: 9 should return False, did return {}".format(is_prime(9))
    print "testing is_prime: 7 should return True, did return {}".format(is_prime(7))



