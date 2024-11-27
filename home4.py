#1
class WordLengthIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return len(word)
        else:
            raise StopIteration

words = ["apple", "banana", "cherry", "date"]
iterator = WordLengthIterator(words)
for length in iterator:
    print(length)

#2

class PowersOfTwoIterator:
    def __init__(self):
        self.exponent = 0
    def __iter__(self):
        return self
    def __next__(self):
        result = 2 ** self.exponent
        self.exponent += 1
        return result
iterator = PowersOfTwoIterator()
for _ in range(10):
    print(next(iterator))