# Player class and 'Player' relevant code
class Player(object):

    # class attribute
    decklist = []
    inventory = []
    xp = 0

    def __init__(self, name, hp, speed, strength):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.strength = strength

    def attack():
        return "ATTACK!"
