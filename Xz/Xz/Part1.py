import string
punctuation = string.punctuation
text = input("Введите текст:")
chars = input("Введите запрещенное слово:")
hars = ""
for char in text.split():
    if char in chars:
        hars += "***"
    else:
        hars += "" +char
print(hars)