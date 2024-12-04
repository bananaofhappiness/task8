from Items import Item
from Spells import Spell


class Player:
    def __init__(self, name):
        self.name: str = name
        self.hp: int = 100
        self.strength: int = 10
        self.mana: int = 10
        self.iq: int = 10
        self.items: list[Item] = []
        self.spells: list[Spell] = []

    def use_item(self):
        if len(self.items) == 0:
            print("У Вас нет предметов")
            return

        while True:
            print("Выберите предмет из списка цифрой:")
            print("0: Отмена")
            for i, item in enumerate(self.items):
                print(f"{i + 1}: {item}")

            try:
                choice = int(input())
            except ValueError:
                print("Вы ввели не число, попробуйсте снова")

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
                print(f"{i + 1}: {spell}")

            try:
                choice = int(input())
            except ValueError:
                print("Вы ввели не число, попробуйсте снова")

            if choice == 0:
                break
            try:
                self.spells[choice - 1].use()
            except IndexError:
                print("Нет такого заклинания, попробуйте снова")


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp: int = 80
        self.mana = 20
        self.iq: int = 15
