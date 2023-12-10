from Lesson_2.character import Character


class Berserk(Character):
    def __init__(self, name, health=100,
                 damage=3, defence=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = health

    def count_damage(self):
        return self.damage * (2 - self.health / self.max_health)

    def attack(self, target):
        return target.take_damage(self.count_damage())