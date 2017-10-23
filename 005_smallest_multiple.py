def main():
    result = 0

    while True:
        result += 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
        for each in range(1, 21):
            if result % each:
                break

        if each == 20:
            break

    print(result)

if __name__ == "__main__":
    main()
