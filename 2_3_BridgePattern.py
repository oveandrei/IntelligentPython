
'''
Bridge Pattern
- The Bridge Pattern is a structural design pattern that decouples an abstraction from its implementation so that the two can vary independently.
- The Bridge Pattern is used when a class has multiple implementations and the client needs to switch between them at runtime.
'''


# Practical Example: File Storage Abstraction
from abc import ABC, abstractmethod

# Step 1: Define Abstraction (Abstract class)
class FileStorage(ABC):
    """Abstract class representing the file storage abstraction."""
    
    @abstractmethod
    def save_file(self, file_name):
        """Abstract method to save a file."""
        pass

# Step 2: Define Implementation (Abstract class)
class StorageImplementation(ABC):
    """Abstract class representing the storage implementation."""
    
    @abstractmethod
    def save(self, file_name):
        """Abstract method to save a file."""
        pass

# Step 3: Create Concrete Implementations
class LocalStorage(StorageImplementation):
    """Concrete implementation for local file storage."""
    
    def save(self, file_name):
        """Save a file locally."""
        return f"File '{file_name}' saved locally"

class CloudStorage(StorageImplementation):
    """Concrete implementation for cloud file storage."""
    
    def save(self, file_name):
        """Save a file to the cloud."""
        return f"File '{file_name}' saved to the cloud"
    
class NetworkStorage(StorageImplementation):
    """Concrete implementation for network file storage."""
    
    def save(self, file_name):
        """Save a file to a network location."""
        return f"File '{file_name}' saved to a network location"


# Step 4: Create Refined Abstraction
class AdvancedFileStorage(FileStorage):
    """Refined abstraction for advanced file storage."""
    
    def __init__(self, storage_impl):
        """Initialize with a specific storage implementation."""
        self._storage_impl = storage_impl
    
    def save_file(self, file_name):
        """Save a file using the specified storage implementation."""
        return self._storage_impl.save(file_name)
    
# Main section to showcase usage
if __name__ == "__main__":
    # Create concrete implementations
    local_storage = LocalStorage()
    cloud_storage = CloudStorage()
    network_storage = NetworkStorage()

    # Create refined abstractions and link them with concrete implementations
    advanced_local_storage = AdvancedFileStorage(local_storage)
    advanced_cloud_storage = AdvancedFileStorage(cloud_storage)
    advanced_network_storage = AdvancedFileStorage(network_storage)

    # Use refined abstractions to save files
    print(advanced_local_storage.save_file("example.txt"))    # Output: File 'example.txt' saved locally
    print(advanced_cloud_storage.save_file("example.txt"))    # Output: File 'example.txt' saved to the cloud
    print(advanced_network_storage.save_file("example.txt"))  # Output: File 'example.txt' saved to a network location




'''How It Works:

Abstraction and Implementation Separation:
The FileStorage abstraction is decoupled from the StorageImplementation implementations.
The AdvancedFileStorage abstraction delegates the file-saving operation to the implementation object (_storage_impl).

Concrete Implementations:
The LocalStorage, CloudStorage, and NetworkStorage classes provide different ways to save files.
These implementations are independent of the abstraction.

Dynamic Linking:
The client dynamically links the AdvancedFileStorage abstraction to a specific implementation (e.g., LocalStorage, CloudStorage, or NetworkStorage).

Client Interaction:
The client interacts with the AdvancedFileStorage abstraction to save files.
The abstraction internally delegates the operation to the linked implementation.'''
