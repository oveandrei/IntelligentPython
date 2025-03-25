

'''
Definition: Decouples senders and receivers using a message broker.
Use case: Event-driven architectures, real-time messaging.
'''


class PubSub:
 def __init__(self):
    self.subscribers = {}
 
 def subscribe(self, event, handler):
    if event not in self.subscribers:
        self.subscribers[event] = []
    self.subscribers[event].append(handler)
 
 def publish(self, event, data):
    if event in self.subscribers:
        for handler in self.subscribers[event]:
            handler(data)


# Usage
def user_registered_handler(data):
 print(f"User registered: {data}")


pubsub = PubSub()
pubsub.subscribe("user_registered", user_registered_handler)
pubsub.publish("user_registered", {"id": 1, "name": "Alice"})