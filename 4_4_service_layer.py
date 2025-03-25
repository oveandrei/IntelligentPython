

'''
    Definition: Encapsulates business logic into separate service classes.
    Use case: Large applications with multiple use cases.
'''

class OrderService:
 def place_order(self, product, quantity):
    return f"Order placed for {quantity} of {product}"


# Usage
service = OrderService()
print(service.place_order("Laptop", 2)) # Output: Order placed for 2 of Laptop