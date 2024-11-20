#2
class Product:
    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def is_available(self, quantity):  #Перевіряє, чи достатньо товару в наявності
        return quantity <= self.quantity_in_stock

    def reduce_stock(self, quantity): #Зменшує кількість товару в наявності
        if self.is_available(quantity):
            self.quantity_in_stock -= quantity
        else:
            raise ValueError(f"Недостатньо товару {self.name} в наявності!")
    def __str__(self):
        return f"{self.name} - {self.price} грн (В наявності: {self.quantity_in_stock})"


class CartItem: #Допоміжний клас для зберігання інформації про товар у кошику
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self): #Розраховує загальну вартість товару у кошику
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x{self.quantity} = {self.get_total_price()} грн"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity): #Додає товар до кошика
        if product.is_available(quantity): #Перевіряємо, чи товар вже у кошику
            for item in self.items:
                if item.product == product:
                    item.quantity += quantity
                    product.reduce_stock(quantity)
                    return #Додаємо новий товар
            self.items.append(CartItem(product, quantity))
            product.reduce_stock(quantity)

    def remove_product(self, product_name): #Видаляє товар з кошика
        for item in self.items:
            if item.product.name == product_name:
                item.product.quantity_in_stock += item.quantity  #Повертаємо товар у склад
                self.items.remove(item)

    def calculate_total(self): #Розраховує загальну вартість кошика
        return sum(item.get_total_price() for item in self.items)

    def list_items(self): #Виводить список товарів у кошику
        if not self.items:
            print("Кошик порожній.")
        else:
            print("Ваш кошик:")
            for item in self.items:
                print(item)
            print(f"Загальна вартість: {self.calculate_total()} грн")

    def clear_cart(self): #Очищає кошик, повертаючи товари на склад
        for item in self.items:
            item.product.quantity_in_stock += item.quantity
        self.items = []

if __name__ == "__main__":
    #Створення товарів
    product1 = Product("Телефон", 12000, 10)
    product2 = Product("Ноутбук", 30000, 5)
    product3 = Product("Навушники", 2500, 20)
    #Створення кошика
    cart = Cart()
    #Додавання товарів
    cart.add_product(product1, 2)
    cart.add_product(product3, 3)
    cart.list_items()
    #Видалення товару
    cart.remove_product("Телефон")
    cart.list_items()
    #Додавання більше товарів
    cart.add_product(product2, 1)
    cart.list_items()
    #Очищення кошика
    cart.clear_cart()
    cart.list_items()