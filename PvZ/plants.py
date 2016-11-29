#MODULE CREATION
import pygame
import os
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
SEED_FOLDER = os.path.join(DIR_ROOT, 'card_images')
PLANT_FOLDER = os.path.join(DIR_ROOT, 'plant_images')
BULLET_FOLDER = os.path.join(DIR_ROOT, 'bullet_images')


class PotatoMine_card(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER,'potatomine_card_sheet.png'))
    x_size = 40
    y_size = 57
    cooldown = 8000
    cost = 25
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self, available=False):
        super(PotatoMine_card, self).__init__()
        self.available = available
        self.cooldown = PotatoMine_card.cooldown
        self.last = pygame.time.get_ticks()
        self.cur_patch_num = 0
        self.frames = []
        for i in range(PotatoMine_card.frame_num):
            self.frames.append(PotatoMine_card.sheet.subsurface(i * PotatoMine_card.x_size, 0, PotatoMine_card.x_size, PotatoMine_card.y_size))
        self.counter = 0


class PotatoMine(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'potatominesheet.png'))
    x_size = 60
    y_size = 60
    HP = 40
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self):
        super(PotatoMine, self).__init__()
        self.last = pygame.time.get_ticks()
        self.HP = PotatoMine.HP
        self.deto_time = 6000
        self.cur_patch_num = 0
        self.frames = []
        for i in range(PotatoMine.frame_num):
            self.frames.append(PotatoMine.sheet.subsurface(i * PotatoMine.x_size, 0, PotatoMine.x_size, PotatoMine.y_size))
        self.counter = 0


class Wallnut_card(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER,'wallnut_card_sheet.png'))
    x_size = 40
    y_size = 57
    cooldown = 7000
    cost = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available = False):
        super(Wallnut_card, self).__init__()
        self.available = available
        self.cooldown = Wallnut_card.cooldown
        self.last = pygame.time.get_ticks()
        self.cur_patch_num = 0
        self.frames = []
        for i in range(Wallnut_card.frame_num):
            self.frames.append(Wallnut_card.sheet.subsurface(i*Wallnut_card.x_size, 0, Wallnut_card.x_size, Wallnut_card.y_size))
        self.counter = 0


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
    sheet = pygame.image.load(os.path.join(SEED_FOLDER, 'peashooter_card_sheet.jpg'))
    x_size = 40
    y_size = 55
    cooldown = 4000
    cost = 100
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available = False):
        super(Peashooter_card, self).__init__()
        self.available = available
        self.cooldown = Peashooter_card.cooldown
        self.last = pygame.time.get_ticks()
        self.cur_patch_num = 0
        self.frames = []
        for i in range(Peashooter_card.frame_num):
            self.frames.append(Peashooter_card.sheet.subsurface(i*Peashooter_card.x_size,0,Peashooter_card.x_size, Peashooter_card.y_size))
        self.counter = 0


class Peashooter(pygame.sprite.Sprite):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'peashootersheet.png'))
    x_size = 60
    y_size = 60
    HP = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self):
        super(Peashooter, self).__init__()
        self.last = pygame.time.get_ticks()
        self.between_bullet = 1000  #1.0 second
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
    sheet = pygame.image.load(os.path.join(SEED_FOLDER, 'sunflower_card_sheet.png'))
    x_size = 40
    y_size = 56
    cooldown = 3000
    cost = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available=False):
        super(Sunflower_card, self).__init__()
        self.available = available
        self.cooldown = Sunflower_card.cooldown
        self.last = pygame.time.get_ticks()
        self.cur_patch_num = 0
        self.frames = []
        for i in range(Sunflower_card.frame_num):
            self.frames.append(Sunflower_card.sheet.subsurface(i*Sunflower_card.x_size, 0, Sunflower_card.x_size, Sunflower_card.y_size))
        self.counter = 0


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
