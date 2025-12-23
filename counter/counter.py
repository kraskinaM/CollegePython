def call_counter(func):
    func.count = 0
    def wrapper(*args, **kwargs):
        func.count += 1
        print(f"Функция {func.__name__} вызвана {func.count} раз")
        print(f"Аргументы: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper
@call_counter
def add(a, b):
    return a + b
@call_counter
def repeat(text, n):
    return text * n
result1 = add(2, 3)
print(result1)
result2 = add(10, 5)
print(result2)
result3 = repeat("Hi", 3)
print(result3)