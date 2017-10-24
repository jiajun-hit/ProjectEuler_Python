import math
''' indeed it is more efficiency than the other method in math, but there are more operations about memory
def all_prime(n):
    primes = [2, 3]
    primes.extend([num for num in range(7, n + 1, 6)])
    primes.extend([num for num in range(5, n + 1, 6)])
    primes.sort()

    for i in primes:
        if i > int(math.sqrt(n)) :
            break

        for j in primes:
            if j >= i and i * j in primes:
                primes.remove(i * j)

    return primes
'''

def all_prime(n):
    primes = [0] * (n+1)
    primes[2] = 1
    primes[3] = 1
    primes[5] = 1

    result = [2]

    for num in range(1, n + 1, 6):
        primes[num] = 1;

    for num in range(5, n + 1, 6):
        primes[num] = 1;

    for num in range(3, int(math.sqrt(n) + 1), 2):
        if primes[num]:
            for j in range(num + num, n + 1, num):
                primes[j] = 0

    for num in range(3, n + 1, 2):
        if primes[num]:
            result.append(num);

    return result


def largest_divisible(p, q, n) :
    num = p * q
    if num > n:
        return 0
    elif num == n:
        return n

    if n % p == 0 and n % q == 0:
        return n

    goal = n // num

    if (q >= math.sqrt(n)):
        temp = int(math.log(goal, p))

        return num * (p ** temp)

    temp = 1
    diff_min = goal
    result = 1

    for i in range(int(math.log(goal, p)) + 1):
        temp = p ** i

        for j in range(int(math.log(goal, q)) + 1):
            temp *= q ** j
            if temp * p < goal:
                continue

            if temp > goal:
                break
            elif temp == goal:
                return temp * num
            else:
                diff_temp = goal - temp
                if diff_temp < diff_min:
                    result = temp
                    diff_min = diff_temp
    return num * result


def main():
    n = int(input("please input a number:"))
    result = 0

    primes = all_prime(n)

    for p in primes:
        if p > math.sqrt(n):
            break

        for q in primes:
            if q > p:
                #break
                result += largest_divisible(p, q, n)

    print(result)


if __name__ == "__main__":
    main()
