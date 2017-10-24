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

# get the list of all the primes that smaller than n
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
    num = p * q  # the answer must contain both p and q
    if num > n:
        return 0
    elif num == n:
        return n

    goal = n // num  # what we want is to approach the "goal" as much as possible

    # if q >= sqrt(n), then n contains q just once
    if (q >= math.sqrt(n)):
        temp = int(math.log(goal, p))

        return num * (p ** temp)

    diff_min = goal  # minimize the diff and approach the goal
    result = 1

    for i in range(int(math.log(goal, p)) + 1):
        temp_p = p ** i

        for j in range(int(math.log(goal, q)) + 1):
            temp_q = q ** j
            temp = temp_p * temp_q

            if temp * p < goal:  # too small
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

    primes = all_prime(n // 2)  # get the list of all the primes not larger than n // 2

    # p is the smaller prime, so it shoule be smaller than sqrt(n)
    for p in primes:
        if p > math.sqrt(n):
            break

        for q in primes:
            if q > p:  # q is the larger prime
                result += largest_divisible(p, q, n)

    print(result)


if __name__ == "__main__":
    main()
