import player
from enum import Enum, auto


class GameState(Enum):
    RUNNING = auto()
    EXITING = auto()

class TurnState(Enum):
    IN_BATTLE = auto()


class Game:
    def __init__(self):
        self.state: GameState = GameState.RUNNING


if __name__ == "__main__":
    game = Game()
    while game.state == GameState.RUNNING:
        user_input: str = input()
        if user_input.lower() == "выйти":
            game.state = GameState.EXITING
