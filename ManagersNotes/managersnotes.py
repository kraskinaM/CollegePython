import os
filename = 'notes.txt'
if not os.path.exists(filename):
    open(filename, 'w', encoding='utf-8').close()
notes = []
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            cat, text = line.split('|', 1)
            notes.append((cat.strip(), text.strip()))
        else:
            notes.append(('без категории', line))
while True:
    print()
    print('Меню:')
    print('1. Добавить заметку')
    print('2. Показать все заметки')
    print('3. Найти по категории')
    print('4. Поиск по слову')
    print('5. Выход')
    choice = input('Выберите пункт (1-5): ').strip()
    if choice == '1':
        category = input('Категория: ').strip()
        text = input('Текст заметки: ').strip()
        if not category:
            category = 'без категории'
        if text:
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f'{category} | {text}\n')
            notes.append((category, text))
            print('Заметка добавлена.')
        else:
            print('Пустая заметка не добавлена.')
    elif choice == '2':
        if not notes:
            print('Нет заметок.')
        else:
            unique_cats = sorted({c for c, _ in notes}, key=str.lower)
            print('Категории:', ', '.join(unique_cats))
            print('Все заметки:')
            for i, (c, t) in enumerate(notes, 1):
                print(f'{i}. [{c}] {t}')
    elif choice == '3':
        cat_search = input('Введите категорию для поиска: ').strip().lower()
        if not cat_search:
            print('Пустая категория.')
        else:
            results = [n for n in notes if n[0].lower() == cat_search]
            if not results:
                print('Заметок в этой категории не найдено.')
            else:
                for i, (c, t) in enumerate(results, 1):
                    print(f'{i}. [{c}] {t}')
    elif choice == '4':
        word = input('Введите слово для поиска: ').strip().lower()
        if not word:
            print('Пустой запрос.')
        else:
            results = [n for n in notes if word in n[1].lower() or word in n[0].lower()]
            if not results:
                print('Ничего не найдено.')
            else:
                for i, (c, t) in enumerate(results, 1):
                    print(f'{i}. [{c}] {t}')
    elif choice == '5':
        print('Выход.')
        break
    else:
        print('Неверный выбор, введите число от 1 до 5.')
