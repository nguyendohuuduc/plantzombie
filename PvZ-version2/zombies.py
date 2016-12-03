import random
import pygame
import os

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
ZOMBIE_FOLDER = os.path.join(DIR_ROOT, 'zombie_images')

class NormZombie(pygame.sprite.Sprite):
    sheet_walking = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'walking-zombie.png'))
    sheet_eating = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'eating-zombie.png'))
    sheet_walking_frozen = pygame.image.load(os.path.join(ZOMBIE_FOLDER, 'walking-zombie-frozen.png'))
    sheet_eating_frozen = pygame.image.load(os.path.join(ZOMBIE_FOLDER,'eating-zombie-frozen.png'))
    speed = -0.5
    HP = 50
    dps = 10
    x_size = 49
    y_size = 90
    frame_num = int(sheet_walking.get_width() / x_size)
    frame_num2 = int(sheet_eating.get_width()/x_size)
    frame_num3 = int(sheet_walking_frozen.get_width()/x_size)
    frame_num4 = int(sheet_eating_frozen.get_width()/x_size)

    def __init__(self):
        super(NormZombie, self).__init__()
        self.HP = NormZombie.HP
        self.status = 'moving'
        self.dps = NormZombie.dps
        self.at_frame_walking = 0
        self.at_frame_eating = 0
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
        self.walking_counter = 0
        self.eating_counter = 0
        self.condition = []
        self.speed = NormZombie.speed

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")