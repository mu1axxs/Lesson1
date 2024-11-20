class Animal:
    def __init__(self, name, age, species): #Базовий клас для всіх тварин
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self): #Метод для відтворення звуку тварини. Повинен бути перевизначений у підкласах
        raise NotImplementedError("Цей метод має бути перевизначений у підкласі!")

    def __str__(self):
        return f"{self.species} на ім'я {self.name}, вік: {self.age} років."


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака")
        self.breed = breed

    def make_sound(self):
        return "Гав-гав!"

    def fetch(self, item): #Метод, характерний для собак
        return f"{self.name} приносить {item}!"

    def __str__(self):
        return super().__str__() + f" Порода: {self.breed}."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Кіт")
        self.color = color

    def make_sound(self):
        return "Мяу!"

    def climb(self): #Метод, характерний для котів
        return f"{self.name} залазить на дерево!"

    def __str__(self):
        return super().__str__() + f" Колір: {self.color}."
