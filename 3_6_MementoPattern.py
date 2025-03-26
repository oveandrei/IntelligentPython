
'''
Memento Pattern
- The Memento pattern is a behavioral design pattern that provides the ability to restore an object to its previous state (undo via rollback).
- The Memento pattern is implemented with three objects: the originator, a caretaker, and a memento.
- The originator is some object that has an internal state.'''


class Originator:
    def __init__(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

if __name__ == "__main__":
    # Instantiate classes
    originator = Originator("Initial state")
    caretaker = Caretaker()

    # Store object state
    caretaker.add_memento(originator.create_memento())

    # Modify object state
    originator.set_state("Modified state")

    # Restore object state
    originator.restore(caretaker.get_memento(0))



'''How It Works:

Initialization:
The Originator is initialized with the state "Initial state".
The Caretaker is initialized to manage the Memento objects.

Saving State:
The Originator creates a Memento object containing its current state ("Initial state") using create_memento.
The Caretaker stores this Memento using add_memento.

Modifying State:
The Originator's state is updated to "Modified state" using set_state.

Restoring State:
The Caretaker retrieves the saved Memento using get_memento(0).
The Originator restores its state to "Initial state" using restore.
'''