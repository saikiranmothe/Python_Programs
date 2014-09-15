# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) #=> range(1,10). This is an object that implements our Iterable interface

# We can loop over it.
for i in our_iterable:
    print(i)    # Prints one, two, three

# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object by calling the __next__ function.
our_iterator.__next__()  #=> "one"

# It maintains state as we call __next__.
our_iterator.__next__()  #=> "two"
our_iterator.__next__()  #=> "three"

# After the iterator has returned all of its data, it gives you a StopIterator Exception
our_iterator.__next__() # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it.
list(filled_dict.keys())  #=> Returns ["one", "two", "three"]