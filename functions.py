####################################################
## 4. Functions
####################################################

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y    # Return values with a return statement


# Calling functions with parameters
add(5, 6)   # => prints out "x is 5 and y is 6" and returns 

# Another way to call functions is with keyword arguments
add(y=6, x=5)   # Keyword arguments can arrive in any order.




# Use "def" to create new functions
#substraction funtion
def sub(a, b):
    print("a is {} and b is {}".format(a, b))
    sample = a - b    # Return values with a return statement
    print(sample)

# Another wab to call functions is with keyword arguments
sub(b=6, a=5)   # Keyword arguments can arrive in any order.

#multiply functions
def mul(x,y):
    print("x is {} , y is {}".format(x,y))
    mul_var = x * y
    print(mul_var)
mul(x=50,y=60)

#division function
def div(x,y):
	  print("x is {},y is {}".format(x,y))
	  division_value = x / y ;
	  print(division_value)
div(625,25)



