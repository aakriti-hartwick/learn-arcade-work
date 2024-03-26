class Monster2:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount

godzilla = Monster2("Godzilla", 100)
print(godzilla.name + " has health of " + str(godzilla.health))
godzilla.decrease_health(200)
print(godzilla.name + " has health of " + str(godzilla.health))