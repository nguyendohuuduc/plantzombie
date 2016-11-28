#MODULE CREATION
import pygame
import os
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
SEED_FOLDER = os.path.join(DIR_ROOT, 'card_images')
PLANT_FOLDER = os.path.join(DIR_ROOT, 'plant_images')
BULLET_FOLDER = os.path.join(DIR_ROOT, 'bullet_images')
### PEASHOOTER
class Wallnut_card(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(SEED_FOLDER,'wallnut_card.png'))
    x_size = 40
    y_size = 57
    cooldown = 8000
    cost = 50

    def __init__(self, x=180, y=20, available = True):
        super(Wallnut_card, self).__init__()
        self.image = Wallnut_card.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.available = available
        self.cooldown = Wallnut_card.cooldown
        self.last = pygame.time.get_ticks()
        self.signature = 2

    def update(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class Wallnut(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'wallnutsheet.png'))
    x_size = 60
    y_size = 60
    HP = 120
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self):
        super(Wallnut, self).__init__()
        self.last = pygame.time.get_ticks()
        self.HP = Wallnut.HP
        self.frames = []
        for i in range(Wallnut.frame_num):
            self.frames.append(Wallnut.sheet.subsurface(i * Wallnut.x_size, 0, Wallnut.x_size, Wallnut.y_size))


class Peashooter_card(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(SEED_FOLDER,'peashooter_card.jpg'))
    x_size = 40
    y_size = 55
    cooldown = 4000
    cost = 100

    def __init__(self, x=80, y=20, available = False):
        super(Peashooter_card, self).__init__()
        self.image = Peashooter_card.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.available = available
        self.cooldown = Peashooter_card.cooldown
        self.last = pygame.time.get_ticks()
        self.signature = 0

    def update(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class Peashooter(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'peashootersheet.png'))
    x_size = 60
    y_size = 60
    HP = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self):
        super(Peashooter, self).__init__()
        self.last = pygame.time.get_ticks()
        self.between_bullet = 1000  #1 second
        self.HP = Peashooter.HP
        self.status = 'idle'
        self.cur_patch_num = 0
        self.frames = []
        for i in range(Peashooter.frame_num):
            self.frames.append(Peashooter.sheet.subsurface(i*Peashooter.x_size, 0, Peashooter.x_size, Peashooter.y_size))
        self.counter = 0


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


class Sunflower_card(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(SEED_FOLDER, 'sunflower_card.jpg'))
    x_size = 40
    y_size = 56
    cooldown = 3000
    cost = 50

    def __init__(self, x=130, y=20, available=False):
        super(Sunflower_card, self).__init__()
        self.image = Sunflower_card.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.available = available
        self.cooldown = Sunflower_card.cooldown
        self.last = pygame.time.get_ticks()
        self.signature = 1

    def update(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class Sunflower(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'sunflowersheet.png'))
    x_size = 60
    y_size = 60
    HP = 40
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self):
        super(Sunflower, self).__init__()
        self.HP = Sunflower.HP
        self.last = pygame.time.get_ticks()
        self.between_suns = 3000  # 3 second
        self.cur_patch_num = 0 #current frame
        self.frames = []
        for i in range(Sunflower.frame_num):
            self.frames.append(Sunflower.sheet.subsurface(i * Sunflower.x_size, 0, Sunflower.x_size, Sunflower.y_size))
        self.counter = 0

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
