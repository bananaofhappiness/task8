import main
import threading
import time


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
        print("Вы победили!")
        game.turn_state = TurnState.FOUND_ITEM

class Swallow(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Ласточка'
        self.desc = 'Здоровье персонажа увеличивается на 20 ХП на 1 атаку'
        self.value = 1

    def use(self, character):
        super().use(character)
        character.hp += 20
        print(f"Здоровье увеличено до {character.hp}")
        threading.Thread(target=self.reset_health).start()

    def reset_health(self, character):
        time.sleep(60)
        character.hp -= 20


class Invulnerability(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Неуязвимость'
        self.desc = 'Персонаж с большей вероятностью увернется от атаки'
        self.value = 1

    def use(self, character):
        super().use(character)
        character.dodge += 10
        print(f"Уклонение увеличено до {character.dodge}")
        threading.Thread(target=self.reset_dodge).start()

    def reset_dodge(self, character):
        time.sleep(60)
        character.dodge -= 10


class Distant_Attack(Spells):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = 'Огненный заряд'
        self.desc = 'Персонаж кастует огненный заряд, наносящий урон противнику'
        self.value = 2

    def use(self, character, enemy):
        super().use(character)
        enemy.hp -= 20
