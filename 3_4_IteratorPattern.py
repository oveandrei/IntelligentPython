
'''
Iterator Pattern
- The Iterator Pattern provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
'''

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # Returns itself as an iterator

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration  # Raises StopIteration when iteration is complete
        value = self.data[self.index]
        self.index += 1
        return value

# Usage Example
my_list = [1, 2, 3, 4, 5]
iter_obj = MyIterator(my_list)

# Using the for loop to iterate through the object
for element in iter_obj:
    print(element)



'''
How It Works:
When the for loop starts, it calls iter_obj.__iter__(), which returns the iterator object itself.
The loop then repeatedly calls iter_obj.__next__() to get the next element.
Each call to __next__ retrieves the current element, increments the index, and returns the element.
When the index exceeds the length of the list, StopIteration is raised, and the loop terminates.
'''