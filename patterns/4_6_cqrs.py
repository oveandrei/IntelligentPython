

''' 4.6. CQRS (Command Query Responsibility
Segregation)
 Definition: Separates read operations (queries) from write operations (commands).
    Use case: High-performance applications (e.g., banking systems).
'''

class OrderCommand:
 def __init__(self):
    self.orders = {}
 
 def create_order(self, order_id, product):
    self.orders[order_id] = product


class OrderQuery:
 def __init__(self, order_command):
    self.order_command = order_command
 
 def get_order(self, order_id):
    return self.order_command.orders.get(order_id, "Order not found")


# Usage
command = OrderCommand()
query = OrderQuery(command)
command.create_order(1, "Laptop")
print(query.get_order(1)) # Output: Laptop