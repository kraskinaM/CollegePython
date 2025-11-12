text = input()
words = input().split()
for word in words:
    text = text.replace(word, word.upper())
print(text)