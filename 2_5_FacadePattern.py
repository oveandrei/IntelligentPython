
'''
Facade Pattern
- Provides a simplified interface to a complex system of classes, library or framework.
- It provides a single class that represents an entire subsystem.
- It wraps a complicated subsystem with a simpler interface.
'''



class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!"

class Subsystem2:
    def operation2(self):
        return "Subsystem2: Ready!"

class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        result = []
        result.append(self._subsystem1.operation1())
        result.append(self._subsystem2.operation2())
        return '\n'.join(result)
    
def client_code(facade):
    print(facade.operation())

# Usage
if __name__ == "__main__":
    facade = Facade()
    client_code(facade)


'''How It Works:

Subsystem Initialization:
The Facade class initializes instances of Subsystem1 and Subsystem2.

Client Interaction:
The client calls the operation method of the Facade class.
The Facade internally calls the operation1 method of Subsystem1 and the operation2 method of Subsystem2.

Result Combination:
The Facade combines the results of the subsystem operations into a single output and returns it to the client.

Simplified Interface:
The client does not need to know about the existence or complexity of the subsystems. It interacts only with the Facade.
'''