

'''Definition: Defines a dependency between objects.'''

class Subject:
 def __init__(self):
     self._observers = []
 def attach(self, observer):
    self._observers.append(observer)
 def notify(self, message):
    for observer in self._observers:
        observer.update(message)


class Observer:
 def update(self, message):
     print(f"Received: {message}")


# Usage
subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify("Event occurred!")