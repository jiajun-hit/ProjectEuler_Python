import math
import time

MAX = 2000000

def main():
    global MAX
    prime = [0]
    prime = prime * (MAX + 1)
    num = 3
    result = 2

    prime[2] = 1
    for num in range(3, MAX + 1, 2):
        prime[num] = 1;

    for num in range(3, int(math.sqrt(MAX) + 1), 2):
        if prime[num]:
            for j in range(num + num, MAX + 1, num):
                prime[j] = 0

    for num in range(3, MAX + 1, 2):
        if prime[num]:
            result += num

    print(result)

if __name__ == "__main__":
    start = time.clock()
    main()
    end = time.clock()
    print("%fs" %(end - start))
