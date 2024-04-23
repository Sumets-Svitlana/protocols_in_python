class Fibonacci:
    def __init__(self, max_number):
        self.max_number = max_number
        self.first, self.second = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.first > self.max_number:
            raise StopIteration
        current = self.first
        self.first, self.second = self.second, self.first + self.second
        return current


fib_sequence = Fibonacci(10)
for number in fib_sequence:
    print(number)
