def main():
    numbers = {
        1: len("one"),
        2: len("two"),
        3: len("three"),
        4: len("four"),
        5: len("five"),
        6: len("six"),
        7: len("seven"),
        8: len("eight"),
        9: len("nine"),
        10: len("ten"),
        11: len("eleven"),
        12: len("twelve"),
        13: len("thirteen"),
        14: len("fourteen"),
        15: len("fifteen"),
        16: len("sixteen"),
        17: len("seventeen"),
        18: len("eighteen"),
        19: len("nineteen"),
        20: len("twenty"),
        30: len("thirty"),
        40: len("forty"),
        50: len("fifty"),
        60: len("sixty"),
        70: len("seventy"),
        80: len("eighty"),
        90: len("ninety"),
        100: len("hundred"),
        1000: len("thousand")}

    sum_1to9 = 0
    sum_10to19 = 0
    sum_20to99 = 0
    sum_100to999 = 0

    for i in range(1, 10):
        sum_1to9 += numbers[i]

    for i in  range(10, 20):
        sum_10to19 += numbers[i]

    for i in range(20, 100, 10):
        sum_20to99 += numbers[i]
    sum_20to99 = 10 * sum_20to99 + 8 * sum_1to9

    sum_100to999 = (999 - 99) * numbers[100] + (999 - 99 - 9) * len("and")  + 100 * sum_1to9 + 9 * (sum_1to9 + sum_10to19 + sum_20to99)

    count = sum_1to9 + sum_10to19 + sum_20to99 + sum_100to999 + numbers[1] + numbers[1000]

    print(count)

if __name__ == '__main__':
    main()
