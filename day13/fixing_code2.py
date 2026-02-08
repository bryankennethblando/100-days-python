# finding and fixing code part two: the prime loop problem

def is_prime(number):
    # Check for numbers 2 up to the number itself
    # for i in range(2, number): -- since 2 is a prime number the loop should start at 3
    for i in range(3, number):
        if number % i == 0:
            # If it divides evenly, it's NOT prime.
            return False
        else:
            # If it doesn't divide by 'i', it MUST be prime... right?
            return True

# 🚨 Test Code 
# Should print False, but it prints True. Why?
print(f"Is 9 prime? {is_prime(9)}")
