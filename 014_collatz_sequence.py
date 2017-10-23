def main():
    record = [0, 1, 2]
    max_length = 0

    for num in range(3, 1000000):
        a = num
        length = 0

        while(a != 1):
            if a < num:
                length += record[a]
                break

            if(a % 2):
                a = 3 * a + 1
            else:
                a //= 2

            length += 1

        record.append(length)

        if length > max_length:
            max_length = length
            result = num

    print("%d-->%d" % (result, max_length))

if __name__ == "__main__":
    main()
