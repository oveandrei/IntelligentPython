
'''
Command Pattern
- Command Pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request.
- This transformation lets you parameterize methods with different requests, delay or queue a request`s execution, and support undoable operations.
- The Command Pattern is based on the idea of encapsulating a request as an object.
'''

from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Receiver
class Light:
    def turn_on(self):
        print("The light is ON")

    def turn_off(self):
        print("The light is OFF")

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Client
if __name__ == "__main__":
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.set_command(light_on)
    remote.press_button()

    remote.set_command(light_off)
    remote.press_button()



'''
How It Works:

Initialization:
A Light object is created as the receiver.
Two command objects (LightOnCommand and LightOffCommand) are created, each linked to the Light object.

Setting and Executing Commands:
The RemoteControl object is used to set and execute commands.
When set_command(light_on) is called, the RemoteControl stores the LightOnCommand object.
When press_button() is called, the RemoteControl invokes the execute() method of the LightOnCommand, which calls light.turn_on().

Switching Commands:
The RemoteControl can switch to a different command by calling set_command(light_off).
When press_button() is called again, the LightOffCommand's execute() method is invoked, which calls light.turn_off().
'''