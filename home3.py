'''result = []
def divider(a, b):
 if a < b:
 raise ValueError
 if b > 100:
 raise IndexError
 return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
 res = divider(key, data[kem])
 result.append(res)

print(result)'''


result = []
def divider(a, b):
    if a < b:
        raise ValueError("Значення a менше за b")
    if b > 100:
        raise IndexError("Значення b більше за 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(int(key), data[key])  # Приведення до int для ключів типу str
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль для ключа {key} та значення {data[key]}")
    except ValueError as e:
        print(f"Помилка: {e} для ключа {key} та значення {data[key]}")
    except IndexError as e:
        print(f"Помилка: {e} для ключа {key} та значення {data[key]}")
    except Exception as e:
        print(f"Невідома помилка: {e} для ключа {key} та значення {data[key]}")

print(result)