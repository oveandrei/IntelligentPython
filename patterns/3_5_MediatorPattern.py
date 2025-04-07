
'''
Mediator Pattern
- Defines an object that encapsulates how a set of objects interact.
- Promotes loose coupling by keeping objects from referring to each other explicitly.
- Allows for varying interactions between objects.
- Centralizes communication between objects.
'''



from abc import ABC, abstractmethod


class Component:
    """
    Represents a component with business logic.
    """
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, message):
        """
        Sends a message to the mediator.
        """
        self._mediator.notify(message)

    def receive(self, message):
        """
        Receives and processes messages from the mediator.
        """
        print(f"Component received message: {message}")


class Mediator(ABC):
    """
    Mediator interface declares communication methods.
    """
    @abstractmethod
    def notify(self, message):
        """
        Notify method for sending messages to components.
        """
        pass


class ConcreteMediator(Mediator):
    """
    Concrete Mediator manages communication between components.
    """
    def __init__(self):
        self._components = []

    def add_component(self, component):
        """
        Adds a component to the mediator.
        """
        self._components.append(component)

    def notify(self, message):
        """
        Notifies all components with the message.
        """
        for component in self._components:
            component.receive(message)

if __name__ == "__main__":
    # Create mediator
    mediator = ConcreteMediator()

    # Create components and link them to the mediator
    component1 = Component(mediator)
    component2 = Component(mediator)

    # Add components to the mediator
    mediator.add_component(component1)
    mediator.add_component(component2)

    # Send messages through components
    component1.send("Hello from Component 1")
    component2.send("Hi from Component 2")

# Output:
# Component received message: Hello from Component 1
# Component received message: Hello from Component 1
# Component received message: Hi from Component 2
# Component received message: Hi from Component 2

'''
Mediator Pattern:

The ConcreteMediator class manages communication between components.
Each Component sends a message to the mediator, and the mediator forwards the message to all registered components.

Execution Flow:
Two Component instances (component1 and component2) are created and linked to the same ConcreteMediator instance.
Both components are added to the mediator's _components list.
When component1.send("Hello from Component 1") is called:
The mediator's notify method is invoked.
The mediator iterates over its _components list and calls the receive method of each component.
Both component1 and component2 receive the message and print it.
Similarly, when component2.send("Hi from Component 2") is called, the same process occurs.

Output:
For the first message, "Hello from Component 1", both components print the message once.
For the second message, "Hi from Component 2", both components print the message once.
'''