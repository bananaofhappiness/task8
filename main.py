import player
import map
import random
from enemies import Witch, Bandit, Boss
from items import Potion
from enum import Enum, auto


class GameState(Enum):
    RUNNING = auto()
    EXITING = auto()


class TurnState(Enum):
    EXPLORING_WORLD = auto()
    IN_BATTLE = auto()
    FOUND_ITEM = auto()


class Game:
    enemies = [
            Witch("a"),
            Bandit("a"),
            Boss("a"),
            ]
    items = [
            Potion("А", "a", "strength", 10)
            ]

    def __init__(self):
        self.state: GameState = GameState.RUNNING
        self.turn_state: TurnState = TurnState.EXPLORING_WORLD


def handle_input(n):
    while True:
        try:
            user_input: str = int(input())
        except ValueError:
            print("Вы ввели не цифру, попробуйте снова")
            continue

        if user_input > n or user_input < 0:
            print("Такого выбора нет, попробуйсте снова")

        return user_input


if __name__ == "__main__":
    game = Game()
    print("Приветствуем в Dungeons and Pythons!")
    print("Введите ваше имя:")

    name: str = input()

    print("Выберите класс персонажа цифрой:")
    print("0: Без класса")
    print("1: Маг")
    print("2: Воин")
    print("3: Плут")
    while True:
        user_input: int = handle_input(3)
        match user_input:
            case 0:
                character = player.Player(name)
                break
            case 1:
                character = player.Wizard(name)
                break
            case 2:
                character = player.Warrior(name)
                break
            case 3:
                character = player.Rogue(name)
                break

    game_map = map.Map()
    game_map.generation(20, 20)
    while game.state == GameState.RUNNING:
        match game.turn_state:
            case TurnState.EXPLORING_WORLD:
                print()
                print("Выберите опцию цифрой:")
                print("0: Выйти")
                print("1: Продвинуться дальше")
                print("2: Использовать предмет")
                print("3: Экипировать предмет")
                print("4: Посмотреть характеристики")
                print("5: Показать карту")
                user_input: int = handle_input(4)
                match user_input:
                    case 0:
                        game.state = GameState.EXITING
                    case 1:
                        print()
                        print("Выберите направление:")
                        print("1: Вверх")
                        print("2: Вниз")
                        print("3: Влево")
                        print("4: Вправо")
                        direction = handle_input(3)
                        while True:
                            match direction - 1:
                                case map.Dirs.RIGHT.value:
                                    tile = game_map.move(map.Dirs.RIGHT)

                                case map.Dirs.LEFT.value:
                                    tile = game_map.move(map.Dirs.LEFT)

                                case map.Dirs.UP.value:
                                    tile = game_map.move(map.Dirs.UP)

                                case map.Dirs.DOWN.value:
                                    tile = game_map.move(map.Dirs.DOWN)

                                case _:
                                    print("Такого направления нет, попробуйте снова")
                                    continue

                            if tile == 3:  # враг
                                game.turn_state = TurnState.IN_BATTLE

                            if tile == 4:  # предмет
                                game.turn_state = TurnState.FOUND_ITEM
                            break

                    case 2:
                        character.use_item()
                    case 3:
                        character.equip_item()
                    case 4:
                        character.get_stats()
                    case 5:
                        game_map.show_map()

            case TurnState.IN_BATTLE:
                enemy = random.choice(Game.enemies)

                while True:
                    print()
                    print(f"Вы встретили врага {enemy.name}")
                    print("Выберите цифрой вариант:")
                    print("0: Сбежать")
                    print("1: Атаковать")
                    print("2: Использовать заклинание")
                    choice = handle_input(2)
                    match choice:
                        case 0:
                            print("Вы сбежали и ничего не получаете!")
                            game.turn_state = TurnState.EXPLORING_WORLD
                            break
                        case 1:
                            attack, is_dead = character.attack(enemy)
                            print(f"Вы ударили врага на {attack} ОЗ, у врага осталось {enemy.hp} ОЗ")

                            if is_dead:
                                print("Вы победили!")
                                game.turn_state = TurnState.FOUND_ITEM
                                break

                            print(enemy.attack(character))
                            print(f"У вас осталось {character.hp}")
                            if character.hp <= 0:
                                print("Вы умерли! Конец игры!")
                                game.state = GameState.EXITING
                                break
                            continue
                        case 2:
                            character.use_spell()
                            continue

            case TurnState.FOUND_ITEM:
                item = random.choice(Game.items)
                print(f"Вы нашли предмет {item}")
                print("Выберите опцию:")
                print("0: Не брать")
                print("1: Взять предмет")

                choice = handle_input(1)
                match choice:
                    case 0:
                        game.turn_state = TurnState.EXPLORING_WORLD
                    case 1:
                        if len(character.items) >= 10:
                            print("Вы не можете таскать более 10 предметов!")
                            game.turn_state = TurnState.EXPLORING_WORLD
                        character.items.append(item)
                        game.turn_state = TurnState.EXPLORING_WORLD
