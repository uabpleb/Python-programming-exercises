sent = input("Enter a sentence: ")

upper=0
lower=0
for letter in sent:
    if letter.isalpha():
        if letter.isupper():
            upper+=1
        else:
            lower+=1

print("Upper: " + str(upper))
print("Lower: " + str(lower))