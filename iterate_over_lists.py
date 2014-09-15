#List/Array are synonyms.
"""
list is a array.

list = ["India","USA","England"]
list = [1,2,3]
For loops iterate over lists
prints:
    India is a country
    USA is a country
    England is a country

"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))


sample_list = [1,2,3,3,4,4,5,5,5,5,5,5,5,5,5]
for i in sample_list:
	 	print("{} is a number".format(i))


#for loop
#iteration over elements in list and printing :) its a simple job
#Iterating over elements,passing to a variable,and printing the value of variable.
another_list = [2,3,4,5,6,7]
for another_variable in another_list:
			print("{} more numbers printing".format(another_variable))