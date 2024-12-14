from main import handle_input
from items import Item, Sword, Boots, Shield
from spells import Spells, Invulnerability


class Player:
    def __init__(self, name):
        self.name: str = name
        self.hp: int = 100
        self.strength: int = 10
        self.mana: int = 10
        self.iq: int = 10
        self.defence: int = 10
        self.dodge: int = 10
        self.items: list[Item] = []
        self.spells: list[Spells] = []
        self.equiped_sword: Sword | None = None
        self.equiped_boots: Boots | None = None
        self.equiped_shield: Shield | None = None

    def use_item(self):
        if len(self.items) == 0:
            print("У Вас нет предметов")
            return

        print()
        print("Выберите предмет из списка цифрой:")
        print("0: Отмена")
        for i, item in enumerate(self.items):
            print(f"{i + 1}: {item.name}")

        choice = handle_input(len(self.items))

        if choice == 0:
            return
        if self.items[choice - 1].use(self):
            self.items.pop(choice - 1)

    def use_spell(self, enemy):
        if len(self.spells) == 0:
            print()
            print("У Вас нет заклинаний")
            return False

        print("Выберите заклинание из списка цифрой:")
        print("0: Отмена")
        for i, spell in enumerate(self.spells):
            print(f"{i + 1}: {spell.name}")

        choice = handle_input(len(self.items))

        if choice == 0:
            return False
        return self.spells[choice - 1].use(self, enemy)

    def equip_item(self):
        if len(self.items) == 0:
            print("У Вас нет предметов")
            return

        while True:
            print("Выберите предмет из списка цифрой:")
            print("0: Отмена")
            for i, item in enumerate(self.items):
                print(f"{i + 1}: {item.name}")

            choice = handle_input(len(self.items))

            if choice == 0:
                break

            item = self.items[choice - 1]
            match item:
                case Shield():
                    if self.equiped_shield:
                        self.equiped_shield.unequip(self)
                    print(item.equip(self))
                case Sword():
                    if self.equiped_sword:
                        self.equiped_sword.unequip(self)
                    print(item.equip(self))
                case Boots():
                    if self.equiped_boots:
                        self.equiped_boots.unequip(self)
                    print(item.equip(self))
                case _:
                    print("Вы не можете экипировать это, попробуйте еще раз")
                    continue
            break

    def delete_item(self):
        if len(self.items) == 0:
            print("У Вас нет предметов")
            return

        print()
        print("Выберите предмет из списка цифрой:")
        print("0: Отмена")
        for i, item in enumerate(self.items):
            print(f"{i + 1}: {item.name}")

        choice = handle_input(len(self.items))

        if choice == 0:
            return
        self.items.pop(choice - 1)

    def get_stats(self):
        print()
        print(f"Здоровье = {self.hp}")
        print(f"Сила = {self.strength}")
        print(f"Мана = {self.mana}")
        print(f"Интеллект = {self.iq}")
        print(f"Защита = {self.defence}")
        print(f"Уклонение = {self.dodge}")
        print(f"Меч = {self.equiped_sword}")
        print(f"Щит = {self.equiped_shield}")
        print(f"Обувь = {self.equiped_boots}")

    def attack(self, enemy) -> int:
        attack: int = self.strength
        enemy.hp -= attack
        return attack


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp: int = 80
        self.mana: int = 20
        self.iq: int = 15
        self.defence: int = 5
        self.dodge: int = 5
        self.spells: list[Spells] = [Invulnerability("", "", 0)]


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp: int = 120
        self.mana: int = 5
        self.iq: int = 5
        self.defence: int = 15
        self.dodge: int = 5

        sword = Sword("Меч", "Дает бонус к атаке (5)", 5)
        self.items.append(sword)
        sword.equip(self)
        self.equiped_sword = sword

class Rogue(Player):
    def __init__(self, name):
        super().__init__(name)
        self.iq = 12
        self.defence: int = 5
        self.dodge: int = 20

