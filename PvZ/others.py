#MODULE CREATION
import pygame
import os

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
OTHER_FOLDER = os.path.join(DIR_ROOT, 'miscellany')


class Square(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'small_square.png'))
    x_size = 60
    y_size = 80

    def __init__(self, x, y):
        super(Square, self).__init__()
        self.image = Square.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Sun(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'sun_PvZ.png'))
    size = 100
    y_speed = 1

    def __init__(self, x, y, speed):
        super(Sun, self).__init__()
        self.image = Sun.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_speed = speed
        self.last = pygame.time.get_ticks()

class SunBox(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'sunbox.jpg'))
    width = 62
    height = 59
    def __init__(self):
        super(SunBox, self).__init__()
        self.image = SunBox.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.sun_capacity = 0


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")