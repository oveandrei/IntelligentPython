

'''Definition: Separates object construction from its representation.'''


class Burger:
 def __init__(self):
     self.ingredients = []
 def add_ingredient(self, ingredient):
    self.ingredients.append(ingredient)
 def show(self):
    print(f"Burger with {', '.join(self.ingredients)}")


class BurgerBuilder:
 def __init__(self):
    self.burger = Burger()

 def add_cheese(self):
    self.burger.add_ingredient("Cheese")
    return self

 def add_lettuce(self):
     self.burger.add_ingredient("Lettuce")
     return self
 
 def build(self):
    return self.burger



# Usage
builder = BurgerBuilder()
burger = builder.add_cheese().add_lettuce().build()
burger.show() # Output: Burger with Cheese, Lettuce
