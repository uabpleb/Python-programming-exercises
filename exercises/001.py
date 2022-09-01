result = []
for n in range(2000, 3201):
    if n % 7 == 0 and n % 5 != 0:
        result.append(n)

print(result)

"""
l = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join())
"""