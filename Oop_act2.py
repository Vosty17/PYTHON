
class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        pass  # This will be overridden by subclasses
        
class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🦅")
        
class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐠")
        
class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")
        
# Example usage
animals = [Bird("Eagle"), Fish("Nemo"), Snake("Viper")]

for animal in animals:
    animal.move()  # Each animal moves differently - polymorphism in action!
