"""
#Will give unexpected behavior, since we mutate the same list that is being iterated (remove an element -> next elements' index shited -> skip next element)
result = [str(2234), str(2486), str(1065), str(3333)]
for number in result:
    print("Inicio iteracion (number= " + number + ")")
    for digit in number:
        if int(digit) % 2 != 0:
            result.remove(number)
            print("breaking in "+number)
            break

print(result)
"""

result = [str(number) for number in range(1000, 3001) if all([int(digit) % 2 == 0 for digit in str(number)])]

print(result)