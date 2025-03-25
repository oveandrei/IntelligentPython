

'''Definition: Represents part-whole hierarchies'''


class Component:
 def operation(self):
    pass


class Leaf(Component):
 def operation(self):
     return "Leaf"


class Composite(Component):
 def __init__(self):
     self.children = []
 def add(self, component):
     self.children.append(component)
 def operation(self):
    return " + ".join(child.operation() for child in self.children)


# Usage
tree = Composite()
tree.add(Leaf())
tree.add(Leaf())
print(tree.operation()) # Output: Leaf + Leaf