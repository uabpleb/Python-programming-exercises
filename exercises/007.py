args = input("x, y: ")
args = args.split(sep=',')
x = int(args[0])
y = int(args[1])

result = []
for i in range(x):
    result.append([])
    for j in range(y):
        result[i].append(i*j)

print(result)