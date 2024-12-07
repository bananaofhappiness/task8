import random


class Enemies():
    def __init__(self, name, hp=100, attacki=10):
        self.name = name
        self.hp = hp
        self.attacki = attacki

    def attack(self, character):
        probability = character.dodge * 10
        random_number = random.randint(0, 100)
        if random_number > probability:
            character.hp -= (self.attacki - self.attacki * character.defence // 10)
            return f'{self.name} ранит героя на {self.attacki} урона'
        return f'Персонаж успешно отразил атаку'


class Witch(Enemies):
    def __init__(self, name):
        super().__init__(name, hp=60, attacki=5)
        self.spell = 20

    def attack(self, character):
        if self.hp <= 40:
            character.hp -= self.spell
            return f'Ведьма атаковала огненным зарядом'
        return super().attack(character)


class Bandit(Enemies):
    def __init__(self, name):
        super().__init__(name, hp=20, attacki=20)

    def attack(self, character):
        return super().attack(character)


class Boss(Enemies):
    def __init__(self, name):
        super().__init__(name, hp=100, attacki=30)

    def attack(self, character):
        if self.hp <= 30:
            self.attacki += 5
            print(f'Босс переходит в следующую стадию и урон увеличивается')
        return super().attack(character)
