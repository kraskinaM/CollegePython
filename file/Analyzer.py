filename = input("Введите имя файла (например, text.txt): ")
lines = None
try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("Файл не найден, попробуйте снова.")
except PermissionError:
    print("Нет прав на чтение файла.")
except UnicodeDecodeError:
    try:
        with open(filename, 'r', encoding='cp1251') as f:
            lines = f.readlines()
    except Exception as e:
        print("Ошибка при чтении файла:", e)
except Exception as e:
    print("Ошибка при открытии файла:", e)
if lines is not None:
    num_lines = len(lines)
    num_empty = sum(1 for l in lines if l.strip() == '')
    num_words = sum(len(l.split()) for l in lines)
    num_chars = sum(len(l) for l in lines)
    print("Результат анализа:")
    print("Количество строк:", num_lines)
    print("Количество слов:", num_words)
    print("Количество символов (включая пробелы и переводы строк):", num_chars)
    print("Количество пустых строк:", num_empty)