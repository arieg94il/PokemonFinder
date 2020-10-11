from Dimentions import DROP_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_HEIGHT, PLAYER_WIDTH
import random

class Pokemon:

    def __init__(self, images, x_position,y_position, count_end):
        self.images=images
        self.x_position = random.randint(0, SCREEN_WIDTH-PLAYER_WIDTH)
        self.y_position = 0
        self.count_end = count_end


    def drop(self):
        if self.y_position < SCREEN_HEIGHT:
            while self.y_position<SCREEN_HEIGHT:
                self.y_position = self.y_position + DROP_SPEED

                return self.y_position

        if self.y_position+PLAYER_HEIGHT==SCREEN_HEIGHT:
            self.count_end -=1
            return self.count_end

        else:
            self.y_position=0
            return self.y_position



