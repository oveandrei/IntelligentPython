

'''
    Definition: Centralizes data access logic, providing an abstraction over data storage.
    Use case: Database access layer in large applications.
'''

class Repository:
 def __init__(self):
    self.data = {}
 def add(self, key, value):
    self.data[key] = value
 def get(self, key):
    return self.data.get(key, None)


# Usage
repo = Repository()
repo.add("user1", "John Doe")
print(repo.get("user1")) # Output: John Doe