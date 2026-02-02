# using random module
import random

# calling my own module on this file
import my_own_module

# using randint function
random_integer = random.randint(1, 10) # parameters condition: a <= num >= b: basically random num from 1-10
print (random_integer)

# now using the random function to generate floating numbers stating from zero
random_float = random.random() * 10 # using the mutiply by 10: it indicates the scope of random nums it can generate
print (round(random_float, 2))

# now using the uniform function that is the same on the first example
random_float_numbers = random.uniform(1, 10) 
print (round(random_float_numbers, 2))

# process of calling my own function inside the module I make
print (my_own_module.sum_of_two_numbers(1, 10))
