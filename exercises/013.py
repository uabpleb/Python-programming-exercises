sentence = input("Enter a sentence: ")

letters=0
digits=0
for character in sentence:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        letters += 1

print("Letters: " + str(letters))
print("Digits: " + str(digits))
        