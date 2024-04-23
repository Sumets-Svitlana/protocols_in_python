object main2 extends App {
  private type Animal = {
    def sound(): Unit
    def eat(): Unit
  }

  class Cat extends Animal{
    def sound(): Unit = {
      println("Meow meow!")
    }
  }

  class Dog extends Animal{
    def sound(): Unit = {
      println("Woof woof!")
    }
    def eat(): Unit = {
      println("Eats meat")
    }
  }

  def makeSound(animal: Animal): Unit = {
    animal.sound()
  }

  makeSound(new Cat())
  makeSound(new Dog())
}
