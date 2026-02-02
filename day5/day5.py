# for loops: recreating the max functions using for loops

test_scores = [46, 45, 62, 13, 54, 34, 24, 25]

maximum_score = 0
for score in test_scores:
    if score > maximum_score:
        maximum_score = score
print (maximum_score)

# solving the Gauss challenge using range() fucntion
total_number = 0
for number in range (1, 101, 1):
    total_number += number

print (total_number)