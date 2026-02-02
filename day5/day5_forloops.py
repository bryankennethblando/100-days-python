# printing a box
for i in range(6):
    for j in range(6):
        print ("#", end = " ")
    print()

# printing a triangle
for i in range(6):
    for j in range(i):
        print ("#", end = " ")
    print()

# printing a inverted trianlge
for i in range(6):
    for j in range(6 - i):
        print ("#", end = " ")
    print()

# printing a triangle again
for i in range(6):
    for j in range(6 - i):
        print ("#", end = " ")
    print()