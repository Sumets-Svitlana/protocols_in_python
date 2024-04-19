from abc import ABC, abstractmethod


class Animal:
    def sound(self):
        print('...')

    def eat(self):
        print('...')


class Cat(Animal):
    def sound(self):
        print('Meow meow!')


class Dog(Animal):
    def sound(self):
        print('Woof woof!')

    def eat(self):
        print('Eats meat')


def make_sound(animal: Animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())
