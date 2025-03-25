

'''Definition: Groups multiple database operations into a single transaction.
Use case: Transaction management in databases.'''



class UnitOfWork:
 def __init__(self):
    self.operations = []
 
 def register_operation(self, operation):
    self.operations.append(operation)
 
 def commit(self):
    for operation in self.operations:
        operation()


# Usage
def save_data():
 print("Data saved to database")

uow = UnitOfWork()
uow.register_operation(save_data)
uow.commit() # Output: Data saved to database
