import pygame, os, functions

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
BULLET_FOLDER = os.path.join(DIR_ROOT, 'bullet_images')


class Peabullet(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(BULLET_FOLDER, 'peabullet.png'))
    x_size = 20
    y_size = 20
    damage = 5
    x_speed = 5
    y_speed = 0
    layer = 9

    def __init__(self, x, y, gameDisplay, allSprite, bulletSprite):
        super(Peabullet, self).__init__()
        self.image = Peabullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_size = Peabullet.x_size
        self.y_size = Peabullet.y_size
        functions.add_to_screen(self, gameDisplay)
        allSprite.add(self, layer=Peabullet.layer)
        bulletSprite.add(self)

    def update(self, display_width, display_height):
        self.rect.x += Peabullet.x_speed
        self.rect.y += Peabullet.y_speed
        if 0 > self.rect.x or self.rect.x > display_width:  # if bullet out of screen, kill it. Better performance
            self.kill()
        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()


class Snowbullet(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(BULLET_FOLDER, 'snowbullet.png'))
    x_size = 20
    y_size = 20
    damage = 5
    x_speed = 5
    y_speed = 0
    effect_time = 3000
    layer = 9

    def __init__(self, x, y, gameDisplay, allSprite, bulletSprite):
        super(Snowbullet, self).__init__()
        self.image = Snowbullet.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.effect_time = Snowbullet.effect_time
        functions.add_to_screen(self, gameDisplay)
        allSprite.add(self, layer=Snowbullet.layer)
        bulletSprite.add(self)

    def update(self, display_width, display_height):
        self.rect.x += Snowbullet.x_speed
        self.rect.y += Snowbullet.y_speed
        if 0 > self.rect.x or self.rect.x > display_width:  # if bullet out of screen, kill it. Better performance
            self.kill()
        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()