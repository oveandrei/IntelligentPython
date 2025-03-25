

''' Definition: Provides an interface for creating families of related objects.'''


class Dog:
 def speak(self):
    return "Woof!"

class Cat:
 def speak(self):
     return "Meow!"

class AnimalFactory:
 def create_animal(self):
     pass

class DogFactory(AnimalFactory):
 def create_animal(self):
     return Dog()

class CatFactory(AnimalFactory):
 def create_animal(self):
     return Cat()



# Usage
factory = DogFactory()
animal = factory.create_animal()
print(animal.speak()) # Output: Woof!