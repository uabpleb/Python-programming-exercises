#lines = input().splitlines(False)
f = open("../data/009.txt", "r")
lines = f.readlines()

for line in lines:
    line.upper()

print(lines)

