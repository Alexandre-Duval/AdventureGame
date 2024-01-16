class Player:
    def __init__(self, hp: int, position: str) -> None:
        self.hp = hp
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
