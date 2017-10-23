def main():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    results = []
    answer = 0

    for a in range(1, 100):
        for b in range(100, 4096):
            product = a * b
            flag = True

            if len(str(a)) + len(str(b)) + len(str(product)) == 9:
                for each in digits:
                    if str(each) not in (str(a) + str(b) + str(product)):
                        flag = False
                        break

                if flag:
                    if product not in results:
                        results.append(product)
                        answer += product
                        print("%d * %d = %d" %(a, b, product))

    print(answer)

    return

if __name__ == '__main__':
    main()

