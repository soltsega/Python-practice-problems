

class Planet:
    def __init__(self, name, planet_type, star):
        # 1. Type Checking (must be strings)
        if not (isinstance(name, str) and isinstance(planet_type, str) and isinstance(star, str)):
            raise TypeError("name, planet type, and star must be strings")
        
        # 2. Value Checking (must not be empty)
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")

        # 3. Assigning instance attributes
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # Custom method
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    # Official dunder method for string representation
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

# Creating three instances
planet_1 = Planet("Earth", "Terrestrial", "The Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "The Sun")
planet_3 = Planet("Proxima Centauri b", "Super Earth", "Proxima Centauri")

# Printing each planet (triggers __str__)
print(planet_1)
print(planet_2)
print(planet_3)

# Calling the orbit method on each
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())



