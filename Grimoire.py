class Grimoire(object):

    # Class attribute
    type = "type"

    # Instance attribute
    def __init__(self, name, type, hasEffect, effect_text, mana_cost):
        self.name = name
        self.type = type
        self.hasEffect = hasEffect
        self.effect_text = effect_text
        self.mana_cost = mana_cost

    # class method for Grimoire effect
    def effect(self):
        if self.hasEffect == True:
            answer = 'it has an effect'
        else:
            answer = 'it has no effect'
        print("This Grimoire is the {}, ".format(self.name) + answer)

# class to handle attack style grimoires
# it is a child class of the grimoire class


class BattleGrimoire(Grimoire):
    def __init__(self, name, type, hasEffect, effect_text, attack_points, healing_points, mana_cost):
        self.attack_points = attack_points
        self.healing_points = healing_points

        Grimoire.__init__(self, name, type, hasEffect, effect_text, mana_cost)

    def attack(self):
        print("This grimoire does {} damage points".format(self.attack_points))

# Structure grimoire class, this will be like a field spell of sorts


class FieldGrimoire(Grimoire):
    def __init__(self, name, type, hasEffect, effect_text, mana_cost):
        super().__init__(name, type, hasEffect, effect_text, mana_cost)
