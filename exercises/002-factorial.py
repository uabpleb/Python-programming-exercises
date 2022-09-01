number = input("Number to calculate factorial: ")

result = 1

for i in range(int(number), 0, -1):
    result *= i

print(result)