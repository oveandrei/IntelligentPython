
'''
Prototype Pattern
- The Prototype Pattern is a creational design pattern that is used when the type of objects to create is determined by a prototypical instance, which is cloned to produce new objects.
- The Prototype Pattern is used to create a new object by copying an existing object, known as the prototype.
'''


import copy

class Prototype:
    def __init__(self):
        self.data = []

    def clone(self):
        return copy.deepcopy(self)

# Create a prototype
prototype_instance = Prototype()

# Clone the prototype
clone_instance = prototype_instance.clone()

# Check if the prototype and the clone are the same
print(prototype_instance == clone_instance)  # False
# Check if the prototype and the clone have the same data
print(prototype_instance.data == clone_instance.data)  # True
# Check if the prototype and the clone are the same type
print(type(prototype_instance) == type(clone_instance))  # True



'''How It Works:

Prototype Initialization:
A Prototype object (prototype_instance) is created and initialized with an empty data list.

Cloning:
The clone method is called on the prototype, creating a deep copy of the object (clone_instance).
The clone_instance is independent of the prototype_instance.

Verification:
The checks confirm that:
    The prototype and the clone are different objects (False for equality check).
    The prototype and the clone have identical data (True for data equality check).
    The prototype and the clone are of the same type (True for type check).'''