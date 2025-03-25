

'''
    Definition: Uses events to trigger actions asynchronously.
    Use case: Microservices, real-time applications.
'''


class EventDispatcher:
 def __init__(self):
    self.handlers = {}
 
 def register(self, event, handler):
    if event not in self.handlers:
        self.handlers[event] = []
    self.handlers[event].append(handler)
 
 def dispatch(self, event, data):
    if event in self.handlers:
        for handler in self.handlers[event]:
            handler(data)


# Usage
def order_created_handler(data):
 print(f"Order created: {data}")


dispatcher = EventDispatcher()
dispatcher.register("order_created", order_created_handler)
dispatcher.dispatch("order_created", {"id": 1, "product": "Laptop"})