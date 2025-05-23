class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name  # Name of the pet
        self.hunger = 15  # Hunger level (higher means hungrier)
        self.energy = 10  # Energy level
        self.happiness = 20  # Happiness level
        self.tricks = []  # List of tricks the pet knows

    def eat(self):
         #Reduces hunger by 3 points (but not below 0),and increases happiness by 1 (capped at 100).
        
        if self.hunger == 0:
            print(f"{self.name} is not hungry right now!")
        else:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(100, self.happiness + 1)
            print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy, but not above 10

    def play(self):
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
        print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def train(self, trick):
        self.tricks.append(trick)  # Add the new trick to the list of tricks
        print(f"{self.name} learned a new trick: {trick}!")  # Notify the user


    def show_tricks(self):
        if self.tricks:  # Check if the pet knows any tricks
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")  # List the tricks
        else:
            print(f"{self.name} knows zero tricks at the moment.")  # Notify if no tricks are known

    def get_status(self):
        print(f"{self.name}'s Status - Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

