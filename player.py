from main import handle_input
from Items import Item
from Spells import Spell


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
        self.spells: list[Spell] = []
        # self.equiped: Item | None = None

    def use_item(self):
        if len(self.items) == 0:
            print("У Вас нет предметов")
            return

        while True:
            print("Выберите предмет из списка цифрой:")
            print("0: Отмена")
            for i, item in enumerate(self.items):
                print(f"{i + 1}: {item.name}")

            choice = handle_input()

            if choice == 0:
                break
            try:
                self.items[choice - 1].use()
            except IndexError:
                print("Нет такого предмета, попробуйте снова")

    def use_spell(self):
        if len(self.spells) == 0:
            print("У Вас нет заклинаний")
            return

        while True:
            print("Выберите заклинание из списка цифрой:")
            print("0: Отмена")
            for i, spell in enumerate(self.spells):
                print(f"{i + 1}: {spell.name}")

            choice = handle_input()

            if choice == 0:
                break
            try:
                self.spells[choice - 1].use()
            except IndexError:
                print("Нет такого заклинания, попробуйте снова")

    def get_stats(self):
        print("\n")
        print(f"Здоровье = {self.hp}")
        print(f"Сила = {self.strength}")
        print(f"Мана = {self.mana}")
        print(f"Интеллект = {self.iq}")
        print(f"Защита = {self.defence}")
        print(f"Уклонение = {self.dodge}")

    def attack(self, enemy) -> bool:
        enemy.hp -= self.strength  # + self.equiped.bonus

        if enemy.hp <= 0:
            print("Вы победили!")
            return True


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp: int = 80
        self.mana: int = 20
        self.iq: int = 15
        self.defence: int = 5
        self.dodge: int = 5


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp: int = 120
        self.mana: int = 5
        self.iq: int = 5
        self.defence: int = 15
        self.dodge: int = 5


class Rogue(Player):
    def __init__(self, name):
        super().__init__(name)
        self.iq = 12
        self.defence: int = 5
        self.dodge: int = 20
