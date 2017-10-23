import math

def is_prime(num):
    for i in range(3, int(math.sqrt(num)) + 1 ):
        if not (num % i):
            return 0

    return 1

def main():
    num = 3
    count = 2

    while count < 10001:
        num += 2

        if is_prime(num):
            count += 1

    print("The 10001st prime is:", num)

if __name__ == "__main__":
    main()
