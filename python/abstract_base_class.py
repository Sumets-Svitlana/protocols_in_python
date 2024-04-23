from abc import ABC, abstractmethod


class Animal(ABC):
    category: str

    @abstractmethod
    def sound(self) -> str:
        ...

    def eat(self, food: str) -> str:
        return 'Eat default'


class Dog(Animal):
    category = 'pet'

    def sound(self) -> str:
        return f'Dog with category {self.category} sound like Woof woof!'

    def eat(self, food: str) -> str:
        return f'Dog with category {self.category} eat {food}'


def make_sound(animal: Animal):
    return animal.sound()


print(make_sound(Dog()))
print(isinstance(Dog(), Animal))
