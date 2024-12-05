import main


class Spells():
    def __init__(self, name, description, value):
        self.name = name
        self.desc = description
        self.value = value

    def __repr__(self):
        return f'{self.name}'
    
    def __str__(self):
        return f'{self.name}. {self.desc}'
    
    def use(self, character):
        print(f'Заклинание {self.name}. {self.desc}')
        if character.mana < self.value:
            return f'Пополните ману до {self.value}'
        character.mana -= self.value


class Froze(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Заморозка'
        self.desc = 'Персонаж атакует врага без ответной атаки'
        self.value = 2

    def use(self, character, enemy):
        super().use(character)
        character.attack(enemy)


class Fatality(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Фаталити'
        self.desc = 'Персонаж добивает врага'
        self.value = 7

    def use(self, character, enemy):
        super().use(character)
        enemy.hp = 0

class Escape(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Побег'
        self.desc = 'Персонаж благополучно избегает драки'
        self.value = 5

    def use(self, character, enemy):
        super().use(character)
        game.state == TurnState.NOT_IN_BATTLE


class Invulnerability(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Неуязвимость'
        self.desc = 'Персонаж с большей вероятностью увернется от атаки'
        self.value = 4

    def use(self, character, enemy):
        super().use(character)
        character.dodge += 3
        character.attack(enemy)
        enemy.attack(character)
        character.dodge -= 3


class Distant_Attack(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Огненный заряд'
        self.desc = 'Персонаж кастует огненный заряд, наносящий урон противнику'
        self.value = 2

    def use(self, character, enemy):
        super().use(character)
        enemy.hp -= 20
