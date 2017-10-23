import math

# number = 13195
number = 600851475143

factor = 2
largest = int(math.sqrt(number))

while factor <= largest:
    if not (number % factor):
        number /= factor
        print(factor, end = ' ')

        factor = 1
        largest = int(math.sqrt(number))

    factor += 1

print("\nThe largest prime factor is:", int(number))
