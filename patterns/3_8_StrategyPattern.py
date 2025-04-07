
'''
Strategy Pattern
- The Strategy Pattern is implemented by defining a set of algorithms that can be swapped out at runtime.
- The Strategy Pattern is used when you want to define a family of algorithms, encapsulate each one, and make them interchangeable.'''

from typing import Protocol

# 2. Strategy Interface
class Strategy(Protocol):
    def execute(self, data: list[int]) -> list[int]:
        ...

# 3. Concrete Strategies
class AscendingSortStrategy:
    def execute(self, data: list[int]) -> list[int]:
        return sorted(data)

class DescendingSortStrategy:
    def execute(self, data: list[int]) -> list[int]:
        return sorted(data, reverse=True)

# 1. Context
class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, data: list[int]) -> list[int]:
        return self._strategy.execute(data)

# 4. Client
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    # Using AscendingSortStrategy
    context = Context(AscendingSortStrategy())
    print("Ascending:", context.execute_strategy(data))

    # Switching to DescendingSortStrategy
    context.set_strategy(DescendingSortStrategy())
    print("Descending:", context.execute_strategy(data))


'''How It Works:

Initialization:
The Context is initialized with the AscendingSortStrategy.
The execute_strategy method calls the execute method of the AscendingSortStrategy, which sorts the data in ascending order.

Switching Strategies:
The client switches the strategy to DescendingSortStrategy using the set_strategy method.
The execute_strategy method now calls the execute method of the DescendingSortStrategy, which sorts the data in descending order.

Output:
The client sees the sorted data based on the currently selected strategy.


Use Cases:
Sorting algorithms (as shown in this example).
Payment processing systems (e.g., credit card, PayPal, cryptocurrency).
Compression algorithms (e.g., ZIP, RAR, GZIP).
Pathfinding algorithms in games (e.g., A*, Dijkstra).
This implementation is a clean and flexible way to handle multiple interchangeable algorithms.
'''