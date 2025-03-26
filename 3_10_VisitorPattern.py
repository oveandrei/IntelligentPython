
'''
Visitor Pattern
- The Visitor Pattern is a behavioral design pattern that allows adding new behaviors to existing class hierarchies without altering any existing code.
- The Visitor Pattern is used when we have to perform an operation on a group of similar objects.
- The Visitor Pattern is implemented by defining a visitor class that implements the operations to be performed on the elements of an object structure.
'''


from abc import ABC, abstractmethod

# Step 1: Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element_a):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element_b):
        pass


# Concrete Visitor A
class ConcreteVisitorA(Visitor):
    def visit_concrete_element_a(self, element_a):
        print(f"Visitor A visiting {element_a}")

    def visit_concrete_element_b(self, element_b):
        print(f"Visitor A visiting {element_b}")


# Concrete Visitor B
class ConcreteVisitorB(Visitor):
    def visit_concrete_element_a(self, element_a):
        print(f"Visitor B visiting {element_a}")

    def visit_concrete_element_b(self, element_b):
        print(f"Visitor B visiting {element_b}")

# Step 3: Element Interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Step 4: Concrete Elements
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def operation_a(self):
        return "Operation A"


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def operation_b(self):
        return "Operation B"


# Client Code
if __name__ == "__main__":
    # Creating concrete elements
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()

    # Creating concrete visitors
    visitor_a = ConcreteVisitorA()
    visitor_b = ConcreteVisitorB()

    # Accepting visitors
    element_a.accept(visitor_a)
    element_b.accept(visitor_a)

    element_a.accept(visitor_b)
    element_b.accept(visitor_b)


'''
    How It Works:

Element Accepts Visitor:
Each element (ConcreteElementA or ConcreteElementB) has an accept method that takes a visitor as an argument.
The element calls the appropriate method on the visitor (visit_concrete_element_a or visit_concrete_element_b), passing itself as an argument.

Visitor Performs Operation:
The visitor performs the operation specific to the element type.
For example, ConcreteVisitorA might print a message indicating it is visiting ConcreteElementA.

Client Interaction:
The client creates elements and visitors and uses the accept method to apply the visitors to the elements.
This allows the client to perform different operations on the elements without modifying their classes.

    Use Cases:
    
Compilers (e.g., traversing and processing abstract syntax trees).
Object structures where new operations need to be added frequently.
Reporting systems (e.g., generating different types of reports for the same data structure).
This implementation provides a clean way to add new operations to existing object structures without modifying their classes.'''