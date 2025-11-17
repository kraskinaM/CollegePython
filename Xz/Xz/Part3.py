text = input("Введите текст:").strip()
if not text:
    print("Текст не виден")
else:
    sentences = sum(1 for char in text if char in ".!?")
    if sentences == 0 and text:
        sentences = 1
    words = len(text.split())
    punctuation = sum(1 for char in text if char in '.,!?:;-"\'()')
    print(f"\nПредложений: {sentences}")
    print(f"Слов: {words}")
    print(f"Знаков препинания: {punctuation}")
