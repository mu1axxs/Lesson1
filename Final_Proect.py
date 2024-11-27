import requests
class CurrencyConverter:
    def get_exchange_rates(self):
        response = requests.get(self.url)
        data = response.json()
        if response.status_code == 200:
            return data['rates']
        else:
            return {}

    def get_rate(self, currency):
        """Получаем курс для конкретной валюты относительно гривни (UAH)."""
        return self.rates.get(currency.upper(), None)

    def convert(self, amount, from_currency, to_currency):
        """Конвертирует сумму из одной валюты в другую."""
        from_rate = self.get_rate(from_currency)
        to_rate = self.get_rate(to_currency)

        if from_rate is None or to_rate is None:
            return "Неверная валюта"

        # Переводим сумму в базовую валюту (гривню) и потом в целевую валюту
        amount_in_base = amount / from_rate
        converted_amount = amount_in_base * to_rate
        return round(converted_amount, 2)

# Создание объекта конвертера
converter = CurrencyConverter()

# Пользователь вводит количество своей валюты
amount = float(input("Введите количество вашей валюты (например, 100): "))
from_currency = input("Введите код вашей валюты (UAH, USD, EUR и т.д.): ").upper()

# Конвертируем в доллары США
to_currency = 'USD'
converted = converter.convert(amount, from_currency, to_currency)

if isinstance(converted, float):
    print(f"{amount} {from_currency} = {converted} {to_currency}")
else:
    print(converted)  # Выводим ошибку, если валюта не найдена
