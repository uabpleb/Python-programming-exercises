# input: hello world and practice makes perfect and hello world again
input_str = input("Whitespace separated words: ")

result = set()
for word in input_str.split(' '):
    result.add(word)

print(' '.join(sorted(result)))