import player
from enum import Enum, auto


class GameState(Enum):
    RUNNING = auto()
    EXITING = auto()


class TurnState(Enum):
    EXPLORING_WORLD = auto()
    IN_BATTLE = auto()


class Game:
    def __init__(self):
        self.state: GameState = GameState.RUNNING
        self.turn_state: TurnState = TurnState.EXPLORING_WORLD


def handle_input():
    while True:
        try:
            user_input: str = int(input())
            return user_input
        except ValueError:
            print("Вы ввели не цифру, попробуйте снова")


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
        user_input: int = handle_input()
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
            case _:
                print("Такого класса нет, попробуйте снова")

    while game.state == GameState.RUNNING:
        match game.turn_state:
            case EXPLORING_WORLD:
                print()
                print("Выберите опцию цифрой:")
                print("0: Выйти")
                print("1: Продвинуться дальше")
                print("2: Использовать предмет")
                print("3: Посмотреть характеристики")
                user_input: int = handle_input()
                match user_input:
                    case 0:
                        game.state = GameState.EXITING
                    case 1:
                        ...
                    case 2:
                        character.use_item()
                    case 3:
                        character.get_stats()



