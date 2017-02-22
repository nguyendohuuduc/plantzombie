import pygame
import os
import functions

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
SEED_FOLDER = os.path.join(DIR_ROOT, 'card_images')


class Card(pygame.sprite.Sprite):  # Abstract Base Class. Don't touch.
    layer = 2

    def __init__(self, available, cooldown, frame_num, sheet, x_size, y_size, x, y, gameDisplay, allSprite, cardSprite):
        super(Card, self).__init__()
        self.available = available
        self.last = pygame.time.get_ticks()
        self.cur_patch_num = 0
        self.frames = []
        self.counter = 0
        self.cooldown = cooldown
        self.x_size = x_size
        self.y_size = y_size
        for i in range(frame_num):
            self.frames.append(sheet.subsurface
                               (i*self.x_size, 0, self.x_size, self.y_size))
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        functions.add_to_screen(self, gameDisplay)
        allSprite.add(self, layer=Card.layer)
        cardSprite.add(self)

    def move(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    def update(self, FPS):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown and not self.available:
            self.available = True
        self.image = self.frames[self.cur_patch_num]
        if self.available:
            self.cur_patch_num = 0
            self.counter = 0
        elif not self.available:
            if self.counter % FPS == 0:
                self.cur_patch_num += 1
            self.counter += 1


class Hypnoshroom_card(Card):

    sheet = pygame.image.load(os.path.join(SEED_FOLDER,'hypnoshroom_card_sheet.png'))
    x_size = 40
    y_size = 57
    cooldown = 6000
    cost = 75
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available, x, y, gameDisplay, allSprite, cardSprite):
        super(Hypnoshroom_card, self).__init__(available, Hypnoshroom_card.cooldown, Hypnoshroom_card.frame_num,
                                               Hypnoshroom_card.sheet, Hypnoshroom_card.x_size,
                                               Hypnoshroom_card.y_size, x, y, gameDisplay, allSprite, cardSprite)


class PotatoMine_card(Card):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER,'potatomine_card_sheet.png'))
    x_size = 40
    y_size = 57
    cooldown = 8000
    cost = 25
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self, available, x, y, gameDisplay, allSprite, cardSprite):
        super(PotatoMine_card, self).__init__(available, PotatoMine_card.cooldown, PotatoMine_card.frame_num,
                                              PotatoMine_card.sheet, PotatoMine_card.x_size,
                                              PotatoMine_card.y_size, x, y, gameDisplay, allSprite, cardSprite)


class Wallnut_card(Card):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER,'wallnut_card_sheet.png'))
    x_size = 40
    y_size = 57
    cooldown = 7000
    cost = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available, x, y, gameDisplay, allSprite, cardSprite):
        super(Wallnut_card, self).__init__(available, Wallnut_card.cooldown, Wallnut_card.frame_num,
                                            Wallnut_card.sheet, Wallnut_card.x_size,
                                            Wallnut_card.y_size, x, y, gameDisplay, allSprite, cardSprite)


class SnowPea_card(Card):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER, 'snowpea_card_sheet.png'))
    x_size = 40
    y_size = 57
    cooldown = 4000
    cost = 175
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available, x, y, gameDisplay, allSprite, cardSprite):
        super(SnowPea_card, self).__init__(available, SnowPea_card.cooldown, SnowPea_card.frame_num,
                                            SnowPea_card.sheet, SnowPea_card.x_size,
                                            SnowPea_card.y_size, x, y, gameDisplay, allSprite, cardSprite)


class Peashooter_card(Card):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER, 'peashooter_card_sheet.jpg'))
    x_size = 40
    y_size = 55
    cooldown = 4000
    cost = 100
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available, x, y, gameDisplay, allSprite, cardSprite):
        super(Peashooter_card, self).__init__(available, Peashooter_card.cooldown, Peashooter_card.frame_num,
                                               Peashooter_card.sheet, Peashooter_card.x_size,
                                               Peashooter_card.y_size, x, y, gameDisplay, allSprite, cardSprite)


class Sunflower_card(Card):
    sheet = pygame.image.load(os.path.join(SEED_FOLDER, 'sunflower_card_sheet.png'))
    x_size = 40
    y_size = 56
    cooldown = 3000
    cost = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, available, x, y, gameDisplay, allSprite, cardSprite):
        super(Sunflower_card, self).__init__(available, Sunflower_card.cooldown, Sunflower_card.frame_num,
                                            Sunflower_card.sheet, Sunflower_card.x_size,
                                            Sunflower_card.y_size, x, y, gameDisplay, allSprite, cardSprite)

if __name__ == "__main__":
    print(SEED_FOLDER)
