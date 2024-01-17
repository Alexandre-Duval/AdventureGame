class Player:

    def __init__(self, position: str) -> None:
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position