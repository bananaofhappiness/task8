import player
# import Map
import random
from enum import Enum, auto


class GameState(Enum):
    RUNNING = auto()
    EXITING = auto()


class TurnState(Enum):
    EXPLORING_WORLD = auto()
    IN_BATTLE = auto()


class Game:
    enemies = []

    def __init__(self):
        self.state: GameState = GameState.RUNNING
        self.turn_state: TurnState = TurnState.EXPLORING_WORLD


def handle_input(n):
    while True:
        try:
            user_input: str = int(input())
            return user_input
        except ValueError:
            print("Вы ввели не цифру, попробуйте снова")

        if user_input > n or user_input < 0:
            print("Такого выбора нет, попробуйсте снова")


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

    while game.state == GameState.RUNNING:
        match game.turn_state:
            case TurnState.EXPLORING_WORLD:
                print()
                print("Выберите опцию цифрой:")
                print("0: Выйти")
                print("1: Продвинуться дальше")
                print("2: Использовать предмет")
                print("3: Посмотреть характеристики")
                user_input: int = handle_input(3)
                match user_input:
                    case 0:
                        game.state = GameState.EXITING
                    case 1:
                        print("Выберите направление:")
                        direction = handle_input(3)
                        while True:
                            match direction:
                                case Map.Directions.RIGHT.value:
                                    tile = Map.move(Directions.RIGHT)
                                    break

                                case Map.Directions.LEFT.value:
                                    tile = Map.move(Directions.LEFT)
                                    break

                                case Map.Directions.UP.value:
                                    tile = Map.move(Directions.UP)
                                    break

                                case Map.Directions.DOWN.value:
                                    tile = Map.move(Directions.DOWN)
                                    break

                                case _:
                                    print("Такого направления нет, попробуйте снова")

                            if tile == _: # враг
                                game.turn_state = TurnState.IN_BATTLE

                    case 2:
                        character.use_item()
                    case 3:
                        character.get_stats()

            case TurnState.IN_BATTLE:
                enemy = random.choice(Game.enemies)
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
                        game.turn_state.EXPLORING_WORLD
                    case 1:
                        attack, is_dead = character.attack(enemy)
