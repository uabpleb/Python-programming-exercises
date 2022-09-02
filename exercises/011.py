#input: 0100,0011,1010,1001
numbers = [int(x, 2) for x in input("Enter comma-separated, 4-digit bin nums: ").split(',')]
result = []
for n in numbers:
    if n % 5 == 0:
        result.append(n)

print(','.join([bin(x).removeprefix("0b") for x in result]))