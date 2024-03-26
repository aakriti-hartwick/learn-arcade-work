class Cat:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print("Meow!")


my_cat = Cat()

my_cat.name = "Fluffy"
my_cat.color = "Black"
my_cat.weight = 6


my_cat.meow()

print(my_cat.name + " says meow.")
print(my_cat.name + " is " + my_cat.color + " and " + " weighs " + str(my_cat.weight) + " lbs.")