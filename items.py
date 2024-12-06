import random
import main



class Item:
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def __repr__(self):
        return f'{self.name}'
    
    def __str__(self):
        return f'{self.name}. {self.desc}'


class Potion(Item):
    def __init__(self, name, description, type, value):
        super().__init__(name, description)
        self.type = type
        self.value = value

    def use(self, character):
        value = getattr(character, self.type)
        value += self.value
        setattr(character, self.type, value)
        if self.value > 0:
            return f'Выпито {self.name}. Показатель "{self.type}" увеличен на {self.value}'
        return f'Выпито {self.name}. Показатель "{self.type}" уменьшен на {self.value}'
        

class Book(Item):
    def __init__(self, name, description, difficulty, reward):
        super().__init__(name, description)
        self.diff = difficulty
        self.reward = reward

    def use(self, character):
        if character.iq < self.diff:
            difference = self.diff - character.iq
            return f'Эта книга слишком сложная. Увеличьте показатель iq на {difference}'
        character.iq += self.reward
        return f'Интересная и полезная книга. Показатель iq увеличен на {self.reward}'
        

class Trap(Item):
    def __init__(self, name, description, difficulty, injury):
        super().__init__(name, description)
        self.diff = difficulty
        self.inj = injury

    def use(self, character):
        if character.strength < self.diff:
            character.hp -= self.inj
            return f'Персонаж не смог выбраться из капкана и ему пришлось ампутировать конечность. Показатель hp уменьшен на {self.inj}'
        print(f'Неожиданно кто-то напал из кустов!')
        game.turn_state = TurnState.IN_BATTLE


class Chest(Item):
    def __init__(self, name, description, difficulty):
        super().__init__(name, description)
        self.diff = difficulty
        self.item = random.choice(main.Game.spells)

    def use(self, character):
        if character.strength < self.diff:
            if character.mana >= 2:
                if 'chest_open' in character.spells:
                    return f'Сундук открыт заклинанием. В сундуке оказалось заклинание!'
            return f'Сундук не удалось открыть. Попробуйте увеличить показатель силы, маны или получите заклинание для открытия сундука'
        return f'Сундук открыт. В сундуке оказалось заклинание!'
        game.state = TurnState.FOUND_SPELL

    

class Shield(Item):
    def __init__(self, name, description, weight, power):
        super().__init__(name, description)
        self.weight = weight
        self.power = power

    def equip(self, character):
        if character.strength < self.weight:
            return f'Щит слишком тяжелый. Улучшите показатель силы'
        character.defence += self.power
        character.equiped.append(self)
        return f'Щит используется. Показатель защиты увеличен на {self.power}'

    def deequip(self, character):
        character.defence -= self.power
        character.equiped.remove(self)
    

class Boots(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power

    def equip(self, character):
        character.dodge += self.power
        character.equiped.append(self)
        return f'Ботинки используются. Показатель уклонения увеличен на {self.power}'

    def deequip(self, character):
        character.dodge -= self.power
        character.equiped.remove(self)

class Sword(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power

    def equip(self, character):
        character.strength += self.power
        character.equiped.append(self)
        return f'Меч используется. Показатель силы увеличен на {self.power}'

    def deequip(self, character):
        character.strength -= self.power
        character.equiped.remove(self)
