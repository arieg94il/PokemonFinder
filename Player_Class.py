from Dimentions import MOVE_SPEED

class Player:

    def __init__(self, image, position):
        self.image=image
        self.position = position

    def move_left(self):
        self.position = (int(self.position[0]) - MOVE_SPEED, int(self.position[1]))
        return self.position

    def move_right(self):
        self.position = (int(self.position[0] + MOVE_SPEED), int(self.position[1]))
        return self.position