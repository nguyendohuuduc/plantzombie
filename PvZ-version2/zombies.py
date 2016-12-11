import random
import pygame
import os

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
ZOMBIE_FOLDER = os.path.join(DIR_ROOT, 'zombie_images')

#Abstract Base Class
class Zombie(pygame.sprite.Sprite):

    def __init__(self, speed, HP, dps):
        super(Zombie, self).__init__()
        self.walking_counter = 0
        self.eating_counter = 0
        self.condition = []
        self.speed = speed
        self.HP = HP
        self.status = 'moving'
        self.dps = dps
        self.at_frame_walking = 0
        self.at_frame_eating = 0


class NormZombie(Zombie):
    sheet_walking = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'walking-zombie.png'))
    sheet_eating = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'eating-zombie.png'))
    sheet_walking_frozen = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'walking-zombie-frozen.png'))
    sheet_eating_frozen = pygame.image.load(os.path.join(ZOMBIE_FOLDER,'eating-zombie-frozen.png'))
    speed = -1
    HP = 50
    dps = 10
    x_size = 49
    y_size = 90
    frame_num = int(sheet_walking.get_width() / x_size)
    frame_num2 = int(sheet_eating.get_width()/x_size)
    frame_num3 = int(sheet_walking_frozen.get_width()/x_size)
    frame_num4 = int(sheet_eating_frozen.get_width()/x_size)

    def __init__(self):
        super(NormZombie, self).__init__(NormZombie.speed, NormZombie.HP, NormZombie.dps)
        self.walking_frames = []
        for i in range(NormZombie.frame_num):
            self.walking_frames.append(NormZombie.sheet_walking.subsurface(i * NormZombie.x_size, 0, NormZombie.x_size, NormZombie.y_size))
        self.eating_frames = []
        for i in range(NormZombie.frame_num2):
            self.eating_frames.append(NormZombie.sheet_eating.subsurface(i*NormZombie.x_size, 0, NormZombie.x_size, NormZombie.y_size))
        self.walking_frozen_frames=[]
        for i in range(NormZombie.frame_num3):
            self.walking_frozen_frames.append(NormZombie.sheet_walking_frozen.subsurface(i * NormZombie.x_size, 0, NormZombie.x_size, NormZombie.y_size))
        self.eating_frozen_frames=[]
        for i in range (NormZombie.frame_num4):
            self.eating_frozen_frames.append(NormZombie.sheet_eating_frozen.subsurface(i * NormZombie.x_size, 0, NormZombie.x_size, NormZombie.y_size))


class PresentZombie(Zombie):
    sheet_walking1 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'present-zombie-walking.png'))
    sheet_eating1 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'present-zombie-eating.png'))
    sheet_walking2 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'zombie-non-present-walking.png'))
    sheet_eating2 = pygame.image.load(os.path.join(ZOMBIE_FOLDER,'zombie-non-present-eating.png'))
    sheet_frozen_walking1 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'present-zombie-walking-frozen.png'))
    sheet_frozen_eating1 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'present-zombie-eating-frozen.png'))
    sheet_frozen_walking2 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'zombie-non-present-walking-frozen.png'))
    sheet_frozen_eating2 = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'zombie-non-present-eating-frozen.png'))
    speed = -1
    HP = 70
    dps = 10
    x_size = 66
    y_size = 90
    frame_num1 = int(sheet_walking1.get_width() / x_size)
    frame_num2 = int(sheet_eating1.get_width()/x_size)
    frame_num3 = int(sheet_walking2.get_width()/x_size)
    frame_num4 = int(sheet_eating2.get_width()/x_size)
    frame_num5 = int(sheet_frozen_walking1.get_width()/x_size)
    frame_num6 = int(sheet_frozen_eating1.get_width()/x_size)
    frame_num7 = int(sheet_frozen_walking2.get_width()/x_size)
    frame_num8 = int(sheet_frozen_eating2.get_width()/x_size)

    def __init__(self):
        super(PresentZombie, self).__init__(PresentZombie.speed, PresentZombie.HP, PresentZombie.dps)
        self.walking_frames1 = []
        for i in range(PresentZombie.frame_num1):
            self.walking_frames1.append(PresentZombie.sheet_walking1.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.eating_frames1 = []
        for i in range(PresentZombie.frame_num2):
            self.eating_frames1.append(PresentZombie.sheet_eating1.subsurface(i*PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.walking_frames2=[]
        for i in range(PresentZombie.frame_num3):
            self.walking_frames2.append(PresentZombie.sheet_walking2.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.eating_frames2=[]
        for i in range (PresentZombie.frame_num4):
            self.eating_frames2.append(PresentZombie.sheet_eating2.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.walking_frames3=[]
        for i in range (PresentZombie.frame_num5):
            self.walking_frames3.append(PresentZombie.sheet_frozen_walking1.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.eating_frames3=[]
        for i in range (PresentZombie.frame_num6):
            self.eating_frames3.append(PresentZombie.sheet_frozen_eating1.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.walking_frames4=[]
        for i in range (PresentZombie.frame_num7):
            self.walking_frames4.append(PresentZombie.sheet_frozen_walking2.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))
        self.eating_frames4=[]
        for i in range (PresentZombie.frame_num8):
            self.eating_frames4.append(PresentZombie.sheet_frozen_eating2.subsurface(i * PresentZombie.x_size, 0, PresentZombie.x_size, PresentZombie.y_size))


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")