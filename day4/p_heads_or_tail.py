# # creating a head or tail random generator

import random as r

coin_flip = r.randint(1, 2)

if coin_flip == 1:
    print ("heads")
else:
    print ("tails")

# randomization in list
list_names = ["bryan", "kenneth", "blando"]
print (list_names[r.randint(0, 2)])