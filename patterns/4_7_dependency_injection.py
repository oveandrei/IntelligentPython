

'''
Definition: Injects dependencies instead of hardcoding them.
Use case: Large-scale enterprise applications.
'''



class Database:
 def connect(self):
    return "Connected to database"


class Service:
 def __init__(self, database):
    self.database = database
 
 def perform_action(self):
    return self.database.connect()
# Usage
db = Database()
service = Service(db)
print(service.perform_action()) # Output: Connected to database