from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        ...


class Cat(Animal):
    def sound(self):
        print('Meow meow!')


class Dog:
    def sound(self):
        print('Woof woof!')


def make_sound(animal: Animal):
    animal.sound()


make_sound(Cat())
make_sound(Dog())
