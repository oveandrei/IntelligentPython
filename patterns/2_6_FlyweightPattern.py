
'''
Flyweight Pattern
- A space optimization technique that lets us use less memory by storing externally the data associated with similar objects.
- It is used to minimize memory usage or computational expenses by sharing as much as possible with related objects.
'''

class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Flyweight: Shared ({self.shared_state}) and Unique ({unique_state}) state.")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        key = tuple(shared_state)
        if key not in self._flyweights:
            print(f"Creating new flyweight for shared state: {shared_state}")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f"Reusing existing flyweight for shared state: {shared_state}")
        return self._flyweights[key]

    def list_flyweights(self):
        print(f"FlyweightFactory: {len(self._flyweights)} flyweights:")
        for key in self._flyweights.keys():
            print(f"  {key}")


# Example usage
if __name__ == "__main__":
    factory = FlyweightFactory()

    flyweight1 = factory.get_flyweight(["state1", "state2"])
    flyweight1.operation("unique1")

    flyweight2 = factory.get_flyweight(["state1", "state2"])
    flyweight2.operation("unique2")

    flyweight3 = factory.get_flyweight(["state3", "state4"])
    flyweight3.operation("unique3")

    factory.list_flyweights()


'''How It Works:

Flyweight Creation:
The client requests a Flyweight with the shared state ["state1", "state2"].
Since no Flyweight with this shared state exists, the factory creates a new Flyweight and stores it in the _flyweights dictionary.

Flyweight Reuse:
The client requests another Flyweight with the same shared state ["state1", "state2"].
The factory finds an existing Flyweight with this shared state and reuses it instead of creating a new one.

New Flyweight:
The client requests a Flyweight with a new shared state ["state3", "state4"].
Since no Flyweight with this shared state exists, the factory creates a new Flyweight.

Flyweight Operations:
The client calls the operation method on each Flyweight, passing a unique state ("unique1", "unique2", "unique3").
The Flyweight combines its shared state with the unique state and performs the operation.

Listing Flyweights:
The factory lists all the Flyweight objects it manages, showing the shared states.'''