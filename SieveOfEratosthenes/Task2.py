import random
def shuffle_words(text):
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)
text = input()
shuffled_text = shuffle_words(text)
print(shuffled_text)