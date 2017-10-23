def palindrome_judge(result):
    a = []

    for each in range(6):
        a.append(result % 10)
        result //= 10

    if a[0]==a[5] and a[1]==a[4] and a[2]==a[3]:
        return 1
    else:
        return 0

def product_judge(result):
    for num1 in range(999, 0, -1):
        if not (result % num1):
            if 99 < result // num1 <= 999:
                return 1

    return 0

def main():
    result = 999 * 999

    while result > 10000:
        result -= 1
        flag = palindrome_judge(result)

        if flag:
            if product_judge(result):
                break

    print(result)

if __name__ == '__main__':
    main()
