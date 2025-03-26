
'''
Template Pattern
- The Template Pattern is a behavioral design pattern that defines the program skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
- The Template Pattern is implemented by creating an abstract base class that defines a template method, which calls a series of other methods that are either concrete or have default implementations.
- The Template Pattern is used when you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.'''


from abc import ABC, abstractmethod

# Step 1: Abstract Class (Template)
class AbstractTemplate(ABC):
    def template_method(self):
        """The template method orchestrating the steps."""
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        """Abstract method representing the first step."""
        pass

    @abstractmethod
    def step_two(self):
        """Abstract method representing the second step."""
        pass

    @abstractmethod
    def step_three(self):
        """Abstract method representing the third step."""
        pass

# Step 2: Concrete Class 1
class ConcreteTemplateA(AbstractTemplate):
    def step_one(self):
        """Concrete implementation for the first step in Template A."""
        print("Performing initialization for Template A.")

    def step_two(self):
        """Concrete implementation for the second step in Template A."""
        print("Executing core logic for Template A.")

    def step_three(self):
        """Concrete implementation for the third step in Template A."""
        print("Finalizing and cleaning up for Template A.")

# Step 3: Concrete Class 2
class ConcreteTemplateB(AbstractTemplate):
    def step_one(self):
        """Concrete implementation for the first step in Template B."""
        print("Setting up resources for Template B.")

    def step_two(self):
        """Concrete implementation for the second step in Template B."""
        print("Performing specialized processing for Template B.")

    def step_three(self):
        """Concrete implementation for the third step in Template B."""
        print("Cleaning up connections and resources for Template B.")

# Main Section
if __name__ == "__main__":
    # Creating instances of concrete classes
    template_a = ConcreteTemplateA()
    template_b = ConcreteTemplateB()

    # Using the template method to perform steps
    print("Executing Template A:")
    template_a.template_method()

    print("\nExecuting Template B:")
    template_b.template_method()


'''How It Works:

Abstract Template:
The AbstractTemplate defines the structure of the algorithm in the template_method.
The algorithm consists of three steps (step_one, step_two, step_three), which are abstract and must be implemented by subclasses.

Concrete Templates:
ConcreteTemplateA and ConcreteTemplateB provide specific implementations for the steps of the algorithm.
Each concrete class customizes the behavior of the algorithm while adhering to the structure defined in the template_method.

Client Execution:
The client calls the template_method on instances of the concrete classes.
The template_method executes the steps in the predefined order, invoking the concrete implementations of the steps.

Use Cases:
Workflow systems where the overall process is fixed, but individual steps vary (e.g., data processing pipelines).
Game development for defining game loops with customizable steps.
Report generation systems where the structure of the report is fixed, but the content varies.'''