
'''Definition: Ensures a class has only one instance and provides a global access point'''

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
# Usage

s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # True
    