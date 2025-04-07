
'''
Chain of Responsibility
- Behavioral design pattern
- Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request
- Chain the receiving objects and pass the request along the chain until an object handles it
'''

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            return self.successor.handle_request(request)
        return None


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            return "Handled by ConcreteHandlerA"
        return super().handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            return "Handled by ConcreteHandlerB"
        return super().handle_request(request)


class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == "C":
            return "Handled by ConcreteHandlerC"
        return super().handle_request(request)


# Create the chain of responsibility
handler_chain = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))

# Test the chain
requests = ["A", "B", "C", "D"]
for req in requests:
    result = handler_chain.handle_request(req)
    print(f"Request {req}: {result if result else 'Not handled'}")
# Output:
# Request A: Handled by ConcreteHandlerA
# Request B: Handled by ConcreteHandlerB
# Request C: Handled by ConcreteHandlerC
# Request D: Not handled



'''How It Works:

Request "A":
ConcreteHandlerA handles the request and returns "Handled by ConcreteHandlerA".
The chain stops here.

Request "B":
ConcreteHandlerA does not handle the request and passes it to ConcreteHandlerB.
ConcreteHandlerB handles the request and returns "Handled by ConcreteHandlerB".
The chain stops here.

Request "C":
ConcreteHandlerA and ConcreteHandlerB do not handle the request and pass it to ConcreteHandlerC.
ConcreteHandlerC handles the request and returns "Handled by ConcreteHandlerC".
The chain stops here.

Request "D":
None of the handlers (ConcreteHandlerA, ConcreteHandlerB, or ConcreteHandlerC) handle the request.
The chain ends, and None is returned.'''