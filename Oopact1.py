
class Superhero:
    def __init__(self, name, secret_identity, powers, weakness):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.weakness = weakness
        self.energy_level = 100
        
    def use_power(self):
        if self.energy_level > 20:
            print(f"{self.name} uses {self.powers[0]}!")
            self.energy_level -= 20
        else:
            print(f"{self.name} is too tired to use powers!")
            
    def rest(self):
        print(f"{self.name} is resting to regain energy.")
        self.energy_level = min(100, self.energy_level + 30)
        
    def reveal_identity(self):
        print(f"My real name is {self.secret_identity}.")
        
    def __str__(self):
        return f"{self.name} - Powers: {', '.join(self.powers)} | Weakness: {self.weakness}"

# Example usage
spiderman = Superhero("Spider-Man", "Peter Parker", 
                     ["web-slinging", "spider-sense", "wall-crawling"], 
                     "ethics and responsibility")
print(spiderman)
spiderman.use_power()
spiderman.reveal_identity()
