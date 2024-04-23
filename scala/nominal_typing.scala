object main1 extends App {
  abstract class Animal {
    def sound(): Unit
  }


  class Cat extends Animal {
    def sound(): Unit = {
      println("Meow meow!")
    }
  }


  class Dog {
    def sound(): Unit = {
      println("Woof woof!")
    }
  }


  def makeSound(animal: Animal): Unit = {
    animal.sound()
  }

  makeSound(new Cat())
  makeSound(new Dog())
}