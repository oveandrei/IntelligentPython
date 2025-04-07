
'''Definition: Defines an interface for creating objects, but lets subclasses alter the
type.'''

class Animal:
 def speak(self):
    pass
 
class Dog(Animal):
 def speak(self):
    return "Woof!"

class Cat(Animal):
 def speak(self):
    return "Meow!"

def animal_factory(animal_type):
 animals = {"dog": Dog, "cat": Cat}
 return animals.get(animal_type, Animal)()


# Usage
animal = animal_factory("dog")
print(animal.speak()) # Output: Woof!
