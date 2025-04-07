
'''
Proxy Pattern
- A structural design pattern that lets you provide a substitute or placeholder for another object.
- A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.
- The proxy and the original object implement the same interface.
'''


class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self._check_access():
            result = self._real_subject.request()
            self._log_access()
            return result
        return "Proxy: Access denied."

    def _check_access(self):
        print("Proxy: Checking access prior to forwarding the request.")
        # Simulate access control logic
        return True

    def _log_access(self):
        print("Proxy: Logging the time of request.")

# Client code
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print(proxy.request())
    # Proxy: Checking access prior to forwarding the request.
    # Proxy: Logging the time of request.
    # RealSubject: Handling request.



'''How It Works:

Initialization:
A RealSubject object is created.
A Proxy object is created, which holds a reference to the RealSubject.

Client Request:
The client calls the request method on the Proxy object.

Proxy Behavior:
The Proxy first calls _check_access to simulate access control.
If access is granted (True), the proxy forwards the request to the RealSubject by calling its request method.
After the RealSubject processes the request, the proxy calls _log_access to log the request.
If access is denied (False), the proxy returns "Proxy: Access denied." without forwarding the request.

RealSubject Execution:
If access is granted, the RealSubject processes the request and returns the result ("RealSubject: Handling request.").'''