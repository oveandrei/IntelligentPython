

'''
Definition: Combines data access and business logic in a single object.
Use case: ORM frameworks like Django ORM.
'''



class User:
 _database = {}
 
 def __init__(self, user_id, name):
    self.user_id = user_id
    self.name = name
 
 def save(self):
    User._database[self.user_id] = self.name
 
 @classmethod
 def get(cls, user_id):
    return cls._database.get(user_id, "User not found")


# Usage
user = User(1, "Alice")
user.save()
print(User.get(1)) # Output: Alice
