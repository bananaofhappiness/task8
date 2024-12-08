import main
from spells import Chest_Open



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

    def use(self, character, game):
        if self.name == "Капкан":
            if character.strength < self.diff:
                character.hp -= self.inj
                return f'Персонаж не смог выбраться из ловушки невредимым и ему пришлось ампутировать конечность. Показатель hp уменьшен на {self.inj}'
            else:
                return "Вы были достаточны сильные и смогли разжать капкан и выбраться!"

        if character.dodge > self.diff:
            return "Вы были достаточно ловки и смогли избежать ловушки!"
        print("Вы не смогли избежать ловушки!")
        character.hp -= self.inj
        game.killed_enemies -= 1
        game.turn_state = main.TurnState.IN_BATTLE
        return 'Неожиданно кто-то напал из кустов!'


class Chest(Item):
    def __init__(self, name, description, difficulty):
        super().__init__(name, description)
        self.diff = difficulty

    def use(self, character, game):
        if character.strength < self.diff:
            if character.mana >= 2:
                if any(isinstance(spell, Chest_Open) for spell in character.spells):
                    game.turn_state = main.TurnState.FOUND_SPELL
                    return f'Сундук открыт заклинанием. В сундуке оказалось заклинание!'
                character.mana -= 2
            game.turn_state = main.TurnState.EXPLORING_WORLD
            return f'Сундук не удалось открыть. Попробуйте увеличить показатель силы, маны или получите заклинание для открытия сундука'
        game.turn_state = main.TurnState.FOUND_SPELL
        return f'Сундук открыт. В сундуке оказалось заклинание!'


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
