text = input("Введите текст:")
chars = len(text)
words = text.split()
word_count = len(words)
vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
vowels_count = 0
consonants_count = 0
longest_word = max(words, key=len) if words else ""
longest = len(longest_word)
for letter in text.lower():
   if letter in vowels:
      vowels_count += 1
   elif letter in consonants:
      consonants_count += 1
print("Символов(включая пробелы):", chars)
print("Слов:", word_count)
print("Гласных:", vowels_count)
print("Согласных:", consonants_count)
print("Самое длинное слово:", longest_word , f"(длина: {longest})")
