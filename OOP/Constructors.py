class Character:
    def __init__(self, name, hp, mp, atk, type):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.type = type
        print("Created")


character_one = Character("Bugoy", 100, 50, 25, "Assassin")
character_Two = Character("Lalay", 100, 50, 25, "Mage")
character_Three = Character("Alieya", 100, 50, 25, "Ranger")
