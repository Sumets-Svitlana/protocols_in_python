from typing import Protocol, runtime_checkable


@runtime_checkable
class Animal(Protocol):
    def sound(self):
        ...


class Dog:
    def sound(self):
        print('Woof woof!')


print(isinstance(Dog(), Animal))


@runtime_checkable
class HasLength(Protocol):
    def __len__(self) -> int:
        ...


print(isinstance('Duck', HasLength))
print(isinstance([1, 2, 3], HasLength))
