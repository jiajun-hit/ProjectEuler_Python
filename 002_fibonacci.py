result = 0

num1 = 1
num2 = 1

while num2 < 4000000:
    num3 = num1 + num2
    num1 = num2
    num2 = num3

    if num2 % 2 == 0:
        result += num2

print(result)
