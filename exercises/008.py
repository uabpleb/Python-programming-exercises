#input_str = input("Provide comma-separated words: ")
#words = input_str.split(',')
words = [x for x in input("Provide comma-separated words: ").split(',')]
words.sort()

print(','.join(words))