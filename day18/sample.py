# using a normal for loop in a not controlled manner over values that is printing:

for num in range(10 ** 100):
    if num == 10:
        break
    print(num)

# vs using the iter() and next() function which let's you have controled ove the values that your loopping
num_iterator = iter(range(10 ** 100))

# exmple that I want only five values from the num iterator
# so I can use the next funcition for five times, values printed are: 0-4 wchich equavalent to 5 number values
print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))

# but there's another secret for that which is to combine both of this functions into action
# which let's you have controlled over the values you want

name_list = ['bryan', 'kenneth', 'blando']
name_iterator = iter(name_list)

# storing it an new variable so we can controlled the values over
next_name = next(name_iterator)

for person_name in next_name:
    print(person_name)

# list comprehension
a = [1,2,3,4]
sort_even = [x for x in a if x % 2 == 0]
print(sort_even)

# dictionary comprehention
x = [1, 2, 3, 4]
mult = {i: i * 3 for i in x}

print(mult)