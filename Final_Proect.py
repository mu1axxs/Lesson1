# Фіксовані курси валют
exchange_rates = {
    "UAH": 1,    # 1 гривня = 1 гривня
    "USD": 41,  # 1 долар = 41 гривень
    "EUR": 43,  # 1 євро = 43 гривень
}

# Функція для конвертації валюти в гривні
def convert_to_uah(amount, currency):
    if currency in exchange_rates:  # Перевірка, чи є валюта в словнику
        rate = exchange_rates[currency]  # Отримуємо курс валюти
        converted_amount = amount * rate  # Перераховуємо в гривні
        return round(converted_amount, 2)  # Повертаємо результат, округлений до 2 знаків
    else:
        return "Невірна валюта"  # Якщо валюта не знайдена

# Основна функція програми
def main():
    # Запитуємо користувача на введення
    try:
        amount = float(input("Введіть кількість вашої валюти: "))  # Введення кількості валюти
        currency = input("Введіть код вашої валюти (UAH, USD, EUR): ").upper()  # Введення коду валюти

        # Конвертуємо та виводимо результат
        converted = convert_to_uah(amount, currency)

        # Виводимо результат
        if isinstance(converted, float):
            print(f"{amount} {currency} = {converted} UAH")
        else:
            print(converted)  # Вивести помилку, якщо валюта неправильна
    except ValueError:
        print("Будь ласка, введіть коректне число для кількості валюти.")

# Викликаємо основну функцію
if __name__ == "__main__":
    main()