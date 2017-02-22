#MODULE CREATION
import pygame, os
from abc import abstractmethod
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
PLANT_FOLDER = os.path.join(DIR_ROOT, 'plant_images')


#Abstract Base Class
class Plant(pygame.sprite.Sprite):
    layer = 1

    def __init__(self, HP, frame_num, sheet, x_size, y_size, x, y):
        super(Plant, self).__init__()
        self.cur_patch_num = 0
        self.frames = []
        self.counter = 0
        self.HP = HP
        self.frame_num = frame_num
        for i in range(self.frame_num):
            self.frames.append(sheet.subsurface(i*x_size, 0, x_size, y_size))
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.add_to_screen()

    @abstractmethod
    def add_to_screen(self):
        """add plants to screen the moment of initialization"""

    def change_frame(self, switch_counter):
        if self.counter % switch_counter == 0:
            self.cur_patch_num += 1
        if self.cur_patch_num > (self.frame_num-1):
            self.cur_patch_num = 0

    def check_dead(self):
        if self.HP <= 0:
            self.kill()


class Hypnoshroom(Plant):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'hypnoshroomsheet.png'))
    x_size = 46
    y_size = 60
    HP = 25
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, x, y):
        super(Hypnoshroom, self).__init__(Hypnoshroom.HP, Hypnoshroom.frame_num,
                                          Hypnoshroom.sheet, Hypnoshroom.x_size,
                                          Hypnoshroom.y_size, x, y)


class PotatoMine(Plant):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'potatomine-snow-sheet.png'))
    x_size = 60
    y_size = 60
    HP = 40
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self, x, y):
        super(PotatoMine, self).__init__(PotatoMine.HP, PotatoMine.frame_num,
                                         PotatoMine.sheet, PotatoMine.x_size,
                                         PotatoMine.y_size, x, y)
        self.last = pygame.time.get_ticks()
        self.deto_time = 6000
        self.explodable = False
        self.dead_already = False


class Wallnut(Plant):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'wallnutsheet.png'))
    x_size = 60
    y_size = 60
    HP = 160
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self, x, y):
        super(Wallnut, self).__init__(Wallnut.HP, Wallnut.frame_num,
                                      Wallnut.sheet, Wallnut.x_size,
                                      Wallnut.y_size, x, y)
        self.last = pygame.time.get_ticks()

    def change_frame(self):
        if self.HP <= 120:
            self.image = self.frames[1]
        if self.HP <= 80:
            self.image = self.frames[2]
        if self.HP <= 40:
            self.image = self.frames[3]


class SnowPea(Plant):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'snowpeasheet.png'))
    x_size = 60
    y_size = 60
    HP = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, x, y):
        super(SnowPea, self).__init__(SnowPea.HP, SnowPea.frame_num,
                                      SnowPea.sheet, SnowPea.x_size,
                                      SnowPea.y_size, x, y)
        self.last = pygame.time.get_ticks()
        self.between_bullet = 1000  #1.0 second
        self.status = 'idle'


class Peashooter(Plant):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'peashootersheet.png'))
    x_size = 60
    y_size = 60
    HP = 50
    frame_num = int(sheet.get_width()/x_size)

    def __init__(self, x, y):
        super(Peashooter, self).__init__(Peashooter.HP, Peashooter.frame_num,
                                         Peashooter.sheet, Peashooter.x_size,
                                         Peashooter.y_size, x, y)
        self.last = pygame.time.get_ticks()
        self.between_bullet = 1000  #1.0 second
        self.status = 'idle'


class Sunflower(Plant):
    sheet = pygame.image.load(os.path.join(PLANT_FOLDER, 'sunflowersheet.png'))
    x_size = 60
    y_size = 60
    HP = 40
    frame_num = int(sheet.get_width() / x_size)

    def __init__(self, x, y):
        super(Sunflower, self).__init__(Sunflower.HP, Sunflower.frame_num,
                                        Sunflower.sheet, Sunflower.x_size,
                                        Sunflower.y_size, x, y)
        self.last = pygame.time.get_ticks()
        self.between_suns = 20000  # 20 seconds


if __name__ == "__main__":
    pass
