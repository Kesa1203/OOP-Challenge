class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name  # Name of the pet
        self.hunger = 15  # Hunger level (higher means hungrier)
        self.energy = 10  # Energy level
        self.happiness = 20  # Happiness level
        self.tricks = []  # List of tricks the pet knows

    def eat(self):
        pass

    def sleep(self):
        pass

    def play(self):
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
        print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def train(self, trick):
        pass

    def show_tricks(self):
        pass

    def get_status(self):
        pass

