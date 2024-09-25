class Character:
    def __init__(self, name, health, magicPoints):
        # Initialize the character's basic attributes
        self.name = name
        self.health = health
        self.magicPoints = magicPoints

    def showCharacter(self):
        # Display character's basic attributes in a formatted way
        print("\n---------------------")
        print(f"Name: {self.name:>15}")
        print("---------------------")
        print(f"Health: {self.health:>13}")
        print(f"Magic points: {self.magicPoints:>7}")


class Player(Character):
    def __init__(self, name, health, magicPoints, numLives):
        # Initialize base character attributes using the parent class constructor
        super().__init__(name, health, magicPoints)
        # Additional attribute specific to Player
        self.numLives = numLives

    def showCharacter(self):
        # Display character's and player's attributes
        super().showCharacter()
        print(f"Lives: {self.numLives:>14}")

    def amIalive(self):
        # Check if player is alive based on the number of lives
        if self.numLives <= 0:
            print("No")
        else:
            print("Yes")


class Enemy(Character):
    def __init__(self, name, health, magicPoints, type, strength):
        # Initialize base character attributes using the parent class constructor
        super().__init__(name, health, magicPoints)
        # Additional attributes specific to Enemy
        self.type = type
        self.strength = strength

    def showCharacter(self):
        # Display character's and enemy's attributes in a formatted way
        super().showCharacter()
        print(f"Type: {self.type:>15}")
        print(f"Strength: {self.strength:>11}")


class Orc(Enemy):
    def __init__(self, name, health, magicPoints, strength, speed):
        # Initialize base enemy attributes using the parent class constructor and set type to 'Orc'
        super().__init__(name, health, magicPoints, "Orc", strength)
        # Additional attribute specific to Orc
        self.speed = speed

    def showCharacter(self):
        # Display character's, enemy's, and orc's attributes
        super().showCharacter()
        print(f"Speed: {self.speed:>14}")


class Vampire(Enemy):
    def __init__(self, name, health, magicPoints, strength, dayNight):
        # Initialize base enemy attributes using the parent class constructor and set type to 'Vampire'
        super().__init__(name, health, magicPoints, "Vampire", strength)
        # Additional attribute specific to Vampire
        self.dayNight = dayNight

    def showCharacter(self):
        # Display character's, enemy's, and vampire's attributes
        super().showCharacter()
        print(f"Day/Night: {self.dayNight:>10}")


# Create a player instance
p1 = Player("GenP", 100, 100, 5)

# Create enemy instances (Using provided five enemies setup)
e1 = Orc("Thrag", 80, 60, 7, 3)
e2 = Orc("Gorbag", 95, 75, 6, 2)
e3 = Orc("Ugluk", 120, 50, 8, 5)
e4 = Vampire("Dracula", 110, 100, 9, "Night")
e5 = Vampire("Vlad", 85, 95, 7, "Day")

# Show player's attributes
p1.showCharacter()
p1.amIalive()

# Show enemies' attributes
e1.showCharacter()
e2.showCharacter()
e3.showCharacter()
e4.showCharacter()
e5.showCharacter()
