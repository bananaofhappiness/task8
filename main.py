import player
import map
import random
from enemies import Witch, Bandit, Boss
from items import Potion, Shield, Sword, Boots, Book, Chest, Trap
from spells import Froze, Fatality, Swallow, Invulnerability, Distant_Attack, Chest_Open
from enum import Enum, auto


class GameState(Enum):
    RUNNING = auto()
    EXITING = auto()


class TurnState(Enum):
    EXPLORING_WORLD = auto()
    IN_BATTLE = auto()
    FOUND_ITEM = auto()
    FOUND_SPELL = auto()
    TALK_TO_NPC = auto()


class Game:
    items = [
            Potion("Зелье силы", "Увеличивает силу на 5", "strength", 5),
            Potion("Зелье интеллекта", "Увеличивает интеллект на 5", "iq", 5),
            Potion("Зелье маны", "Увеличивает ману на 5", "mana", 5),
            Potion("Зелье защиты", "Увеличивает защиту на 5", "defence", 5),
            Potion("Зелье уклонения", "Увеличивает уклонение на 5", "dodge", 5),
            Potion("Зелье здоровья", "Увеличивает здоровье на 25", "hp", 25),
            Potion("Большое зелье силы", "Увеличивает силу на 10", "strength", 10),
            # Potion("Большое зелье интеллекта", "Увеличивает интеллект на 10", "iq", 10),
            Potion("Большое зелье маны", "Увеличивает ману на 10", "mana", 10),
            Potion("Большое зелье защиты", "Увеличивает защиту на 10", "defence", 10),
            Potion("Большое зелье уклонения", "Увеличивает уклонение на 10", "dodge", 10),
            Potion("Большое зелье здоровья", "Увеличивает здоровье на 50", "hp", 50),
            Shield("Щит", "Дает бонус к защите (5)", 20, 5),
            Shield("Большой щит", "Дает бонус к защите (10)", 50, 10),
            Sword("Меч", "Дает бонус к атаке (5)", 5),
            Sword("Большой меч", "Дает бонус к атаке (10)", 10),
            Boots("Сапоги", "Дают бонус к уклонению (5)", 5),
            Boots("Кроссовки", "Дают бонус к уклонению (10)", 10),
            Book("Книга для малышей", "Повышает интеллект на 5", 10, 5),
            Book("Любовный роман", "Повышает интеллект на 10", 20, 10),
            Book("Учебник", "Повышает интеллект на 20", 50, 20),
            Chest("Старый сундук", "Полусломанный сундук, легко открывается", 15),
            Chest("Cундук", "Крепкий сундкук, чтобы сломать, нужно быть очень сильным", 20),
            Trap("Ловушка с колючей проволкой", "В ней тяжело и больно передвигаться", 15, 15),
            Trap("Капкан", "Он может легко оставить без ноги", 20, 20),
            Trap("Ловушка с растяжкой", "Совсем невидимая!", 20, 20)
            ]

    spells = [
            Froze('', '', 0),
            Fatality('', '', 0),
            Invulnerability("", "", 0),
            Chest_Open("", "", 0),
            Swallow("", "", 0),
            Distant_Attack("", "", 0),
            ]

    def __init__(self):
        self.state: GameState = GameState.RUNNING
        self.turn_state: TurnState = TurnState.EXPLORING_WORLD
        self.cleared_maps = 0
        self.after_fight = False
        self.boss_killed = False


def handle_input(n):
    while True:
        try:
            user_input: str = int(input())
        except ValueError:
            print("Вы ввели не цифру, попробуйте снова")
            continue

        if user_input > n or user_input < 0:
            print("Такого выбора нет, попробуйте снова")
            continue

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
                s = Invulnerability("", "", 0)
                Game.spells = [spell for spell in Game.spells if not isinstance(spell, s.__class__)]
                break
            case 2:
                character = player.Warrior(name)
                break
            case 3:
                character = player.Rogue(name)
                break

    game_map = map.Map()
    game_map.generation(20, 20, 5)
    while game.state == GameState.RUNNING:
        if game.boss_killed:
            game_map = map.Map()
            game_map.generation(20, 20, 5)
            game.cleared_maps += 1
            game.boss_killed = False

        if game.cleared_maps == 3:
            print("Вы прошли игру!")
            game.state = GameState.EXITING

        match game.turn_state:
            case TurnState.EXPLORING_WORLD:
                print()
                game_map.show_map()
                print("Выберите опцию цифрой:")
                print("0: Выйти")
                print("1: Продвинуться дальше")
                print("2: Использовать предмет")
                print("3: Экипировать предмет")
                print("4: Выбросить предмет")
                print("5: Посмотреть характеристики")
                user_input: int = handle_input(5)
                match user_input:
                    case 0:
                        game.state = GameState.EXITING
                        break
                    case 1:
                        print()
                        print("Выберите направление:")
                        print("1: Вверх")
                        print("2: Вниз")
                        print("3: Влево")
                        print("4: Вправо")

                        while True:
                            direction = handle_input(4)
                            match direction:
                                case 4:
                                    tile = game_map.move(map.Dirs.RIGHT)

                                case 3:
                                    tile = game_map.move(map.Dirs.LEFT)

                                case 1:
                                    tile = game_map.move(map.Dirs.UP)

                                case 2:
                                    tile = game_map.move(map.Dirs.DOWN)

                                case _:
                                    print("Такого направления нет, попробуйте снова")
                                    continue

                            if tile == 3:  # враг
                                game.turn_state = TurnState.IN_BATTLE

                            if tile == 4:  # предмет
                                game.turn_state = TurnState.FOUND_ITEM

                            if tile == 5:  # нпц
                                game.turn_state = TurnState.TALK_TO_NPC

                            break

                    case 2:
                        character.use_item()
                    case 3:
                        character.equip_item()
                    case 4:
                        character.delete_item()
                    case 5:
                        character.get_stats()

            case TurnState.IN_BATTLE:
                if map.get_enemy_count() == 0:
                    enemy = Boss("Босс")
                elif random.randint(0, 1) == 0:
                    enemy = Witch("Ведьма")
                else:
                    enemy = Bandit("Бандит")

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
                            if isinstance(enemy, Boss):
                                print("Вы не можете сбежать от босса!")
                                continue

                            character.hp -= 5
                            if character.hp <= 0:
                                print("Вы умерли при побеге! Конец игры!")
                                game.state = GameState.EXITING
                                break

                            print("Вы сбежали, получили 5 урона при побеге и не получили предмет!")
                            game.turn_state = TurnState.EXPLORING_WORLD
                            break
                        case 1:
                            attack = character.attack(enemy)
                            print(f"Вы ударили врага на {attack} ОЗ, у врага осталось {enemy.hp} ОЗ")

                            if enemy.hp <= 0:
                                print("Вы победили!")
                                game.turn_state = TurnState.FOUND_ITEM
                                game.after_fight = True
                                break

                            print(enemy.attack(character))
                            print(f"У вас осталось {character.hp}")

                            if character.hp <= 0:
                                print("Вы умерли! Конец игры!")
                                game.state = GameState.EXITING
                                break
                            continue
                        case 2:
                            if character.use_spell(enemy):
                                if enemy.hp <= 0:
                                    print("Вы победили!")
                                    game.turn_state = TurnState.FOUND_ITEM
                                    game.after_fight = True
                                    break

                                print(enemy.attack(character))
                                print(f"У вас осталось {character.hp}")

                                if character.hp <= 0:
                                    print("Вы умерли! Конец игры!")
                                    game.state = GameState.EXITING
                                    break
                            continue

            case TurnState.FOUND_ITEM:
                item = random.choice(Game.items)

                if game.after_fight:
                    game.after_fight = False
                    while isinstance(item, Trap):
                        item = random.choice(Game.items)

                if isinstance(item, Chest):
                    print(f"Вы нашли {item}")
                    if item.use(character):
                        game.turn_state = TurnState.FOUND_SPELL
                        continue
                    game.turn_state = TurnState.EXPLORING_WORLD
                    continue

                if isinstance(item, Trap):
                    print(f"Вы понимаете, что попали в ловушку {item}")
                    if not item.use(character):
                        if character.hp <= 0:
                            print("Вы умерли! Конец игры!")
                            game.state = GameState.EXITING
                            break

                        game.turn_state = TurnState.IN_BATTLE
                        continue
                    game.turn_state = TurnState.EXPLORING_WORLD
                    continue

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

            case TurnState.FOUND_SPELL:
                if len(Game.spells) == 0:
                    print("Вы уже выучили все заклинания")
                    game.turn_state = TurnState.EXPLORING_WORLD
                    continue

                spell = random.choice(Game.spells)

                print(f"Вы нашли заклинание {spell}")
                character.spells.append(spell)
                Game.spells = [s for s in Game.spells if not isinstance(s, spell.__class__)]
                game.turn_state = TurnState.EXPLORING_WORLD

            case TurnState.TALK_TO_NPC:
                print(f"Маг: Здравствуй, {character.name}!")
                if character.iq < 20:
                    print(f"Маг: {character.name}, ты слишком мало знаешь, мне не о чем с тобой говорить")
                    game.turn_state = TurnState.EXPLORING_WORLD
                elif character.iq >= 20 and character.iq <= 25:
                    print(f"Маг: {character.name}, ты хороший собеседник. Если ты еще немного обучишься, то я смогу обучить тебя заклинанию")
                    game.turn_state = TurnState.EXPLORING_WORLD
                else:
                    print("Маг: {character.name}, ты прирожденный волшебник! Я обучу тебя всему, что знаю сам!")
                    game.turn_state = TurnState.FOUND_SPELL
