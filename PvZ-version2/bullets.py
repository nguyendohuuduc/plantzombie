import pygame, os

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
BULLET_FOLDER = os.path.join(DIR_ROOT, 'bullet_images')


class Peabullet(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(BULLET_FOLDER, 'peabullet.png'))
    x_size = 20
    y_size = 20
    damage = 5
    x_speed = 5
    y_speed = 0

    def __init__(self, x, y):
        super(Peabullet, self).__init__()
        self.image = Peabullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Snowbullet(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(BULLET_FOLDER, 'snowbullet.png'))
    x_size = 20
    y_size = 20
    damage = 5
    x_speed = 5
    y_speed = 0
    effect_time = 3000

    def __init__(self, x, y):
        super(Snowbullet, self).__init__()
        self.image = Snowbullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.effect_time = Snowbullet.effect_time