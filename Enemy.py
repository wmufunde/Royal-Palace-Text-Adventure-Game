class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage # damage they inflict
        self.health = health # health points they have to begin with


dark_elf = Enemy("dark elf", 20, 30)
goblin = Enemy("goblin", 7, 15)
harpy = Enemy("harpy", 30, 60)
malignant_spirit = Enemy("malignant spirit", 15, 50)

