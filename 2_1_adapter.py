
'''Definition: Allows objects with incompatible interfaces to work together.'''

class EuropeanPlug:
 def plug_in(self):
    return "220V"

class USPlug:
 def connect(self):
     return "110V"

class Adapter:
 def __init__(self, plug):
     self.plug = plug

 def plug_in(self):
     return self.plug.connect()


# Usage
us_plug = USPlug()
adapter = Adapter(us_plug)
print(adapter.plug_in()) # Output: 110V
