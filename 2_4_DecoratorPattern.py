
'''
Decorator Pattern
- The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.'''



# Step 1: Component - The base game character
class Character():

    def get_description(self):
        pass

    def get_damage(self):
        pass

# Step 2: Concrete Component - Basic game character
class BasicCharacter(Character):
    def get_description(self):
        return "Basic Character"

    def get_damage(self):
        return 10

# Step 3: Decorator - Abstract decorator class
class CharacterDecorator(Character):
    def __init__(self, character):
        self._character = character

    
    def get_description(self):
        pass

    
    def get_damage(self):
        pass

# Step 4: Concrete Decorator
class DoubleDamageDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Double Damage"

    def get_damage(self):
        return self._character.get_damage() * 2
    
class FireballDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Fireball"

    def get_damage(self):
        return self._character.get_damage() + 20
    
class InvisibilityDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Invisibility"

    def get_damage(self):
        return self._character.get_damage()


 #Step 5: Client Code - Creating a character with abilities
if __name__ == "__main__":
    character = BasicCharacter()
    print(character.get_description())  # Output: "Basic Character"
    print(character.get_damage())       # Output: 10

    # Create different decorators
    double_damage_decorator = DoubleDamageDecorator(character)
    fireball_decorator = FireballDecorator(character)
    invisibility_decorator = InvisibilityDecorator(character)

    # Apply decorators individually
    print(double_damage_decorator.get_description())  # Output: "Basic Character with Double Damage"
    print(double_damage_decorator.get_damage())       # Output: 20

    print(fireball_decorator.get_description())  # Output: "Basic Character with Fireball"
    print(fireball_decorator.get_damage())       # Output: 30

    print(invisibility_decorator.get_description())  # Output: "Basic Character with Invisibility"
    print(invisibility_decorator.get_damage())       # Output: 10

    # Combine decorators
    double_fireball_character = DoubleDamageDecorator(FireballDecorator(character))
    print(double_fireball_character.get_description())  # Output: "Basic Character with Double Damage with Fireball"
    print(double_fireball_character.get_damage())       # Output: 60

    invisibility_double_fireball_character = InvisibilityDecorator(double_fireball_character)
    print(invisibility_double_fireball_character.get_description())  # Output: "Basic Character with Invisibility with Double Damage with Fireball"
    print(invisibility_double_fireball_character.get_damage())       # Output: 60





'''How It Works:

Base Character:
A BasicCharacter object is created with default behavior ("Basic Character", damage 10).

Adding Abilities:
Decorators are applied to the BasicCharacter to add abilities dynamically:
DoubleDamageDecorator doubles the damage.
FireballDecorator adds 20 to the damage.
InvisibilityDecorator adds the "Invisibility" description but does not modify the damage.

Combining Decorators:
Decorators can be combined to create more complex behaviors:
For example, DoubleDamageDecorator(FireballDecorator(character)) adds both "Double Damage" and "Fireball" abilities.

Dynamic Behavior:
The behavior of the character is modified dynamically without altering the original BasicCharacter class.'''