class Monster1:

    def __init__(self):
        self.name = ""
        self.health = 0

    def decrease_health(self, amount):
        self.health -= amount


godzilla = Monster1()
godzilla.name = "Godzilla"
godzilla.health = 100
print(godzilla.name + " has health of " + str(godzilla.health))
godzilla.decrease_health(200)
print(godzilla.name + " has health of " + str(godzilla.health))
