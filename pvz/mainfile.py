#Always use updates. The only ones don't use update are the cards
import pygame, plants, others, zombies, random, os,time, cards, bullets
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
OTHER_FOLDER = os.path.join(DIR_ROOT, 'miscellany')
SOUND_FOLDER = os.path.join(DIR_ROOT, 'sound')

pygame.mixer.pre_init()
pygame.init()
#pygame.mixer.init(channels=8)
pygame.mixer.music.load(os.path.join(SOUND_FOLDER, 'WateryGrave.ogg'))
pygame.mixer.music.play(-1)

eating_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'eating_sound.ogg'))
hitting_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'hitting-sound.ogg'))
explosion_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'explosion.ogg'))
snowball_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'snowball-sound.ogg'))

myfont = pygame.font.SysFont('monospace', 25)
FPS = 40
display_width = 707 #used to be 710
display_height = 500
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Plants vs Zombies-Christmas Edition')
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#classes

class Square(others.Square):

    def __init__(self, x, y):
        super(Square, self).__init__(x, y)
        self.add_to_screen()
        squareList.append(self) #to test collision later

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])


class Message(pygame.sprite.Sprite):
    font = os.path.join(OTHER_FOLDER, 'blood_font.otf')

    def __init__(self, string, color, size, time):
        super(Message, self).__init__()
        myFont = pygame.font.Font(Message.font, size)
        textmessage = myFont.render(string,1, color)
        self.image = textmessage
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)
        self.last = pygame.time.get_ticks()
        self.time_last = time
        gameDisplay.blit(self.image, [self.rect.left, self.rect.top])
        allSprite.add(self, layer=10)
        textSprite.add(self)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.time_last:
            self.kill()


class SunBox(others.SunBox):
    def __init__(self):
        super(SunBox, self).__init__()
        self.add_to_screen()
        allSprite.add(self)

    def add_to_screen(self):
        myfont = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        scoretext=myfont.render(str(self.sun_capacity), 1,black)
        self.image = pygame.image.load(os.path.join(OTHER_FOLDER, 'sunbox.png'))
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, SunBox.height, SunBox.width])
        self.image.blit(scoretext, (25, 42))

    def update(self, sun_amount):
        self.sun_capacity += sun_amount
        self.add_to_screen()


class Shovel(others.Shovel):

    def __init__(self, x =425, y=20):
        super(Shovel, self).__init__(x=x, y=y)
        self.add_to_screen()
        allSprite.add(self, layer=others.Shovel.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image,[self.rect.x, self.rect.y, Shovel.width, Shovel.height])

    def move(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class Hypnoshroom_card(cards.Hypnoshroom_card):

    def __init__(self, x = 370, y=20, available=False):
        super(Hypnoshroom_card, self).__init__(available=available, x=x, y=y)
        allSprite.add(self, layer=cards.Hypnoshroom_card.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Hypnoshroom_card.x_size, Hypnoshroom_card.y_size])

    def update(self):
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


class Hypnoshroom(plants.Hypnoshroom):

    def __init__(self, x, y):
        super(Hypnoshroom, self).__init__(x, y)
        allSprite.add(self, layer= plants.Hypnoshroom.layer)
        plantSprite.add(self)

    def update(self):
        self.image = self.frames[self.cur_patch_num]
        if self.counter % 15 == 0:
            self.cur_patch_num += 1
        if self.cur_patch_num > (Hypnoshroom.frame_num-1):
            self.cur_patch_num = 0
        self.counter += 1
        if self.HP <= 0:
            self.kill()


class PotatoMine_card(cards.PotatoMine_card):

    def __init__(self, x = 260, y=20, available = False):
        super(PotatoMine_card, self).__init__(available=available, x=x, y=y)
        allSprite.add(self, layer=cards.PotatoMine_card.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, PotatoMine_card.x_size, PotatoMine_card.y_size])

    def update(self):
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


class PotatoMine(plants.PotatoMine):

    def __init__(self, x, y):
        super(PotatoMine, self).__init__(x, y)
        allSprite.add(self, layer=plants.PotatoMine.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, PotatoMine.x_size, PotatoMine.y_size])

    def exploded(self):
        explosion_sound.play(maxtime=1500)
        self.cur_patch_num = 2
        self.dead_already = True

    def update(self):
        self.image = self.frames[self.cur_patch_num]
        now = pygame.time.get_ticks()
        if self.HP <= 0:
            self.kill()
        if now - self.last >= self.deto_time and self.cur_patch_num != 2:
            self.cur_patch_num = 1
            self.explodable = True
        if self.cur_patch_num == 2:
            self.counter += 1
            if self.counter % (FPS) == 0:
                self.kill()


class Wallnut_card(cards.Wallnut_card):

    def __init__(self, x = 205, y=20, available = False):
        super(Wallnut_card, self).__init__(available=available, x=x, y=y)
        allSprite.add(self, layer=cards.Wallnut_card.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Wallnut_card.x_size, Wallnut_card.y_size])

    def update(self):
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


class Wallnut(plants.Wallnut):

    def __init__(self, x, y):
        super(Wallnut, self).__init__(x, y)
        allSprite.add(self, layer=plants.Wallnut.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image,[self.rect.x, self.rect.y, Wallnut.x_size, Wallnut.y_size])

    def update(self):
        if self.HP <= 120:
            self.image = self.frames[1]
        if self.HP <= 80:
            self.image = self.frames[2]
        if self.HP <= 40:
            self.image = self.frames[3]
        if self.HP <= 0:
            self.kill()


class Sunflower_card(cards.Sunflower_card):

    def __init__(self, x=150, y=20, available = False):
        super(Sunflower_card, self).__init__(available=available, x=x, y=y)
        allSprite.add(self, layer=cards.Sunflower_card.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Peashooter_card.x_size, Peashooter_card.y_size])

    def update(self):
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


class Sunflower(plants.Sunflower):

    def __init__(self, x, y):
        super(Sunflower, self).__init__(x, y)
        allSprite.add(self, layer=plants.Sunflower.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])

    def generate_sun(self):
        Sun(x = self.rect.x, y = self.rect.y, speed=0)

    def update(self):
        self.counter += 1
        self.image = self.frames[self.cur_patch_num]
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_suns:
            self.last = now
            self.generate_sun()
        if self.counter % 10 == 0:
            self.cur_patch_num += 1
        if self.cur_patch_num > (self.frame_num - 1):
            self.cur_patch_num = 0
        if self.HP <= 0:
            self.kill()


class SnowPea_card(cards.SnowPea_card):

    def __init__(self, x=315, y=20, available = False):
        super(SnowPea_card, self).__init__(available=available, x=x, y=y)
        allSprite.add(self, layer=cards.SnowPea_card.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, SnowPea_card.x_size, SnowPea_card.y_size])

    def update(self):
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


class SnowPea(plants.SnowPea):

    def __init__(self, x, y):
        super(SnowPea, self).__init__(x, y)
        allSprite.add(self, layer=plants.SnowPea.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])

    def shoot_pea(self):
        Snowbullet(self.rect.x + Peashooter.x_size, self.rect.y + Peashooter.y_size/6)

    def change_status(self):
        if bool_lane[int((self.rect.y - 100)/Square.y_size)]:
            self.status = 'working'
        else:
            self.status = 'idle'

    def update(self):
        self.change_status()
        self.counter += 1
        self.image = self.frames[self.cur_patch_num]
        if self.counter % 10 == 0:
            self.cur_patch_num += 1
        if self.cur_patch_num > (SnowPea.frame_num - 1):
            self.cur_patch_num = 0
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_bullet and self.status == 'working':
            self.last = now
            self.shoot_pea()
        if self.HP <= 0:
            self.kill()


class Snowbullet(bullets.Snowbullet):

    def __init__(self, x, y):
        super(Snowbullet, self).__init__(x, y)
        self.add_to_screen()
        allSprite.add(self, layer=bullets.Snowbullet.layer)
        bulletSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])

    def update(self):
        self.rect.x = self.rect.x + Snowbullet.x_speed
        self.rect.y = self.rect.y + Snowbullet.y_speed
        if 0 > self.rect.x or self.rect.x > display_width: #if bullet out of screen, kill it. Better performance
            self.kill()
        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()


class Peashooter_card(cards.Peashooter_card):
    def __init__(self, x=95, y=20, available = False):
        super(Peashooter_card, self).__init__(available=available, x=x, y=y)
        allSprite.add(self, layer=cards.Peashooter_card.layer)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Peashooter_card.x_size, Peashooter_card.y_size])

    def update(self):
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


class Peashooter(plants.Peashooter):

    def __init__(self, x, y):
        super(Peashooter, self).__init__(x, y)
        allSprite.add(self, layer=plants.Peashooter.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])

    def shoot_pea(self):
        Peabullet(self.rect.x + Peashooter.x_size, self.rect.y + Peashooter.y_size/6)

    def change_status(self):
        if bool_lane[int((self.rect.y - 100)/Square.y_size)]:
            self.status = 'working'
        else:
            self.status = 'idle'

    def update(self):
        self.change_status()
        self.counter += 1
        self.image = self.frames[self.cur_patch_num]
        if self.counter % 10 == 0:
            self.cur_patch_num += 1
        if self.cur_patch_num > (Peashooter.frame_num - 1):
            self.cur_patch_num = 0
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_bullet and self.status == 'working':
            self.last = now
            self.shoot_pea()
        if self.HP <= 0:
            self.kill()


class Peabullet(bullets.Peabullet):

    def __init__(self, x, y):
        super(Peabullet, self).__init__(x, y)
        self.add_to_screen()
        allSprite.add(self, layer=bullets.Peabullet.layer)
        bulletSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])

    def update(self):
        self.rect.x = self.rect.x + Peabullet.x_speed
        self.rect.y = self.rect.y + Peabullet.y_speed
        if 0 > self.rect.x or self.rect.x > display_width: #if bullet out of screen, kill it. Better performance
            self.kill()
        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()


class Sun(others.Sun):
    def __init__(self, x, y=100, speed=1):
        super(Sun, self).__init__(x=x, y=y, speed = speed)
        self.add_to_screen()
        sunList.add(self)
        allSprite.add(self, layer=9)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Sun.size, Sun.size])

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= 15000:
            self.kill()
        self.rect.y += self.y_speed
        if self.rect.bottom >= 500: #to improve performance
            self.y_speed = 0

class Snowball(others.Snowball):

    def __init__(self,x, y):
        super(Snowball, self).__init__(x=x, y=y)
        allSprite.add(self, layer=8)
        lawnmowerSprite.add(self)
        self.add_to_screen()
        self.sound_play = False #to ensure that sound is only played once. Bc sound in update, it keeps playing otherwise.

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Snowball.width, Snowball.height])

    def update(self):
        if self.status == 'moving':
            self.rect.x += self.speed
            if not self.sound_play:
                self.sound_play = True
                snowball_sound.play(maxtime=3200)
        if self.rect.x >= display_width:
            self.kill()
        for zombie in zombieSprite:
            if self.rect.colliderect(zombie.rect):
                self.status= 'moving'
                zombie.kill()


class PoleZombie(zombies.PoleZombie):

    def __init__(self, x):
        super(PoleZombie, self).__init__()
        self.image = self.walking_frame_with_pole[0]
        self.rect = self.image.get_rect()
        self.level = random.randint(1, 5)
        self.rect.x = x
        self.rect.bottom = 100 + self.level * 80
        self.last = 100000000000
        self.has_pole = True
        self.at_frame_jumping = 0
        self.jumping_counter = 0
        self.mark = False #so that the zombie wont eat the plant it just jumps over
        zombieSprite.add(self)
        allSprite.add(self, layer=zombies.PoleZombie.layer + self.level)

    def bullet_collide(self, bullet):
        if self.status != 'jumping':
            self.HP -= bullet.damage
            hitting_sound.play(maxtime=500)
            if isinstance(bullet, Snowbullet):  # I dont want to stack slowness
                self.condition.append('frost')
                self.last = pygame.time.get_ticks()

    def plant_collide(self, plant):
        if self.has_pole:
            self.status = 'jumping'
            if not self.mark:
                self.mark = plant #so that only one plant is self.mark forever. Sometimes when zombie
                                  #jumps, it collide with another plant as well
        else:
            if plant is not self.mark:
                self.status = 'eating'
                plant.HP -= self.dps/FPS
                eating_sound.play(maxtime=1000)
                if plant.HP <= 0 and isinstance(plant, Hypnoshroom):
                    self.add(befuddled_zombie)
                    self.remove(zombieSprite)
                    self.condition.append('muddled')
            else:
                self.status = 'moving'

    def update(self):
        now = pygame.time.get_ticks()
        if 'frost' in self.condition:
            if self.speed == PoleZombie.speed:
                self.speed = self.speed / 2
                self.dps = self.dps / 2
            if now - self.last >= Snowbullet.effect_time:
                self.speed = PoleZombie.speed
                self.dps = PoleZombie.dps
                self.condition.remove('frost')

        if 'muddled' in self.condition and self.speed < 0:
            self.status = 'moving'
            self.speed = -PoleZombie.speed

        if self.status == 'moving' and self.has_pole:
            self.walking_counter += 1
            self.eating_counter = 0
            self.rect.x += self.speed
            if 'frost' in self.condition:
                if self.walking_counter % 40 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PoleZombie.frame_num1-1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frame_with_pole[self.at_frame_walking],True,False)

            else:
                if self.walking_counter % 15 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PoleZombie.frame_num1-1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frame_with_pole[self.at_frame_walking], True, False)
                else:
                    self.image = self.walking_frame_with_pole[self.at_frame_walking]

        elif self.status == 'moving' and not self.has_pole:
            self.walking_counter += 1
            self.eating_counter = 0
            self.rect.x += self.speed
            if 'frost' in self.condition:
                if self.walking_counter % 40 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PoleZombie.frame_num2 - 1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frame_no_pole[self.at_frame_walking], True, False)

            else:
                if self.walking_counter % 15 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PoleZombie.frame_num2 - 1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frame_no_pole[self.at_frame_walking], True, False)
                else:
                    self.image = self.walking_frame_no_pole[self.at_frame_walking]

        elif self.status == 'eating':
            self.eating_counter += 1
            self.walking_counter = 0
            if 'frost' in self.condition:
                if self.eating_counter % 20 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (PoleZombie.frame_num4 - 1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.eating_frame[self.at_frame_eating], True, False)
                else:
                    self.image = self.eating_frame[self.at_frame_eating]

            else:
                if self.eating_counter % 5 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (PoleZombie.frame_num4 - 1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.eating_frame[self.at_frame_eating], True, False)
                else:
                    self.image = self.eating_frame[self.at_frame_eating]

        elif self.status == 'jumping':
            jump_time = 1.5
            self.rect.y = 100 + 80*self.level - 130
            self.eating_counter = self.walking_counter = 0
            self.jumping_counter += 1
            if 'muddled' in self.condition:
                self.image = pygame.transform.flip(self.jump_frame[self.at_frame_jumping], True, False)
            else:
                self.image = self.jump_frame[self.at_frame_jumping]
            if self.jumping_counter % (jump_time / PoleZombie.frame_num3 * FPS) == 0:
                self.at_frame_jumping += 1
                self.rect.x -= 7.9
            if self.at_frame_jumping > PoleZombie.frame_num3 - 1:
                self.status = 'moving'
                self.has_pole = False
                self.rect.bottom = 100 + 80*self.level

        if 0 > self.rect.x or self.rect.x > display_width: #if bullet out of screen, kill it. Better performance
            self.kill()

        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()

        if self.HP <= 0:
            self.kill()


class NormZombie(zombies.NormZombie):

    def __init__(self,x):
        super(NormZombie, self).__init__()
        self.image = self.walking_frames[0]
        self.rect = self.image.get_rect()
        self.level = random.randint(1, 5)
        self.rect.x = x
        self.rect.y = 100 + self.level*80 - NormZombie.y_size
        self.last = 1000000000000
        zombieSprite.add(self)
        allSprite.add(self, layer=zombies.NormZombie.layer + self.level)

    def bullet_collide(self, bullet):
        self.HP -= bullet.damage

        hitting_sound.play(maxtime=500)
        if isinstance(bullet, Snowbullet):  # I dont want to stack slowness
            self.condition.append('frost')
            self.last = pygame.time.get_ticks()

    def plant_collide(self, plant):
        self.status = 'eating'
        plant.HP -= self.dps/FPS
        eating_sound.play(maxtime=1000)
        if plant.HP <= 0 and isinstance(plant, Hypnoshroom):
            self.add(befuddled_zombie)
            self.remove(zombieSprite)
            self.condition.append('muddled')

    def update(self):
        now = pygame.time.get_ticks()
        if 'frost' in self.condition:
            if self.speed == NormZombie.speed:
                self.speed = self.speed/2
                self.dps = self.dps/2
            if now - self.last >= Snowbullet.effect_time:
                self.speed = NormZombie.speed
                self.dps = NormZombie.dps
                self.condition.remove('frost')

        if 'muddled' in self.condition and self.speed < 0:
            self.status = 'moving'
            self.speed = -NormZombie.speed

        if self.status == 'moving':
            self.walking_counter += 1
            self.eating_counter = 0
            self.rect.x += self.speed
            if 'frost' in self.condition:
                if self.walking_counter % 40 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (NormZombie.frame_num-1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frozen_frames[self.at_frame_walking],True,False)
                else:
                    self.image = self.walking_frozen_frames[self.at_frame_walking]

            else:
                if self.walking_counter % 15 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (NormZombie.frame_num-1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frames[self.at_frame_walking], True, False)
                else:
                    self.image = self.walking_frames[self.at_frame_walking]


        elif self.status == 'eating':
            self.eating_counter += 1
            self.walking_counter = 0
            if 'frost' in self.condition:
                if self.eating_counter % 20 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (NormZombie.frame_num2-1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.eating_frozen_frames[self.at_frame_eating],True,False)
                else:
                    self.image = self.eating_frozen_frames[self.at_frame_eating]

            else:
                if self.eating_counter % 5 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (NormZombie.frame_num2-1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.eating_frames[self.at_frame_eating],True,False)
                else:
                    self.image = self.eating_frames[self.at_frame_eating]


        if 0 > self.rect.x or self.rect.x > display_width: #if bullet out of screen, kill it. Better performance
            self.kill()

        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()

        if self.HP <= 0:
            self.kill()


class PresentZombie(zombies.PresentZombie):

    def __init__(self, x):
        super(PresentZombie, self).__init__()
        self.image = self.walking_frames1[0]
        self.rect = self.image.get_rect()
        self.level = random.randint(1, 5)
        self.rect.x = x
        self.rect.y = 100 + self.level * 80 - PresentZombie.y_size
        self.last = 1000000000000
        self.with_present = True
        zombieSprite.add(self)
        allSprite.add(self, layer=zombies.PresentZombie.layer + self.level)

    def bullet_collide(self, bullet):
        self.HP -= bullet.damage
        hitting_sound.play(maxtime=500)
        if isinstance(bullet, Snowbullet):  # I dont want to stack slowness
            self.condition.append('frost') #if this is the case- then there would be many frosts
            self.last = pygame.time.get_ticks()

    def plant_collide(self, plant):
        self.status = 'eating'
        plant.HP -= self.dps / FPS
        eating_sound.play(maxtime=1000)
        if plant.HP <= 0 and isinstance(plant, Hypnoshroom):
            befuddled_zombie.add(self)
            zombieSprite.remove(self)
            self.condition.append('muddled')

    def update(self):
        now = pygame.time.get_ticks()
        if 'frost' in self.condition:
            if self.speed == PresentZombie.speed:
                self.speed = self.speed / 2
                self.dps = self.dps / 2
            if now - self.last >= Snowbullet.effect_time:
                self.speed = PresentZombie.speed
                self.dps = PresentZombie.dps
                self.condition.remove('frost')

        if 'muddled' in self.condition and self.speed < 0:
            self.speed = -self.speed
            self.status = 'moving'

        if self.status == 'moving' and self.with_present:
            self.walking_counter += 1
            self.eating_counter = 0
            self.rect.x += self.speed

            if 'frost' in self.condition:
                if self.walking_counter % 40 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PresentZombie.frame_num1 - 1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.walking_frames3[self.at_frame_walking],True,False)
                else:
                    self.image=self.walking_frames3[self.at_frame_walking]
            else:
                if self.walking_counter % 15 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PresentZombie.frame_num1 - 1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.walking_frames1[self.at_frame_walking],True,False)
                else:
                    self.image = self.walking_frames1[self.at_frame_walking]

        elif self.status == 'eating' and self.with_present:
            self.eating_counter += 1
            self.walking_counter = 0
            if 'frost' in self.condition:
                if self.eating_counter % 20 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (PresentZombie.frame_num2 - 1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.eating_frames3[self.at_frame_eating],True,False)
                else:
                    self.image=self.eating_frames3[self.at_frame_eating]
            else:
                if self.eating_counter % 5 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (PresentZombie.frame_num2 - 1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.eating_frames1[self.at_frame_eating], True, False)
                else:
                    self.image=self.eating_frames1[self.at_frame_eating]

        elif self.status == 'moving' and not self.with_present:
            self.rect.x += self.speed*3
            if 'frost' in self.condition:
                if self.walking_counter % 10 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PresentZombie.frame_num3 - 1):
                    self.at_frame_walking = 1
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.walking_frames4[self.at_frame_walking],True,False)
                else:
                    self.image=self.walking_frames4[self.at_frame_walking]
            else:
                if self.walking_counter % 5 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PresentZombie.frame_num3 - 1):
                    self.at_frame_walking = 1
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.walking_frames2[self.at_frame_walking],True,False)
                else:
                    self.image=self.walking_frames2[self.at_frame_walking]
            self.walking_counter += 1
            self.eating_counter = 0

        elif self.status == 'eating' and not self.with_present:
            self.eating_counter += 1
            self.walking_counter = 0
            if 'frost' in self.condition:
                if self.eating_counter % 10 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (PresentZombie.frame_num4 - 1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.eating_frames4[self.at_frame_eating],True,False)
                else:
                    self.image=self.eating_frames4[self.at_frame_eating]
            else:
                if self.eating_counter % 5 == 0:
                    self.at_frame_eating += 1
                if self.at_frame_eating > (PresentZombie.frame_num4 - 1):
                    self.at_frame_eating = 0
                if 'muddled' in self.condition:
                    self.image=pygame.transform.flip(self.eating_frames2[self.at_frame_eating],True,False)
                else:
                    self.image=self.eating_frames2[self.at_frame_eating]

        if 0 > self.rect.x or self.rect.x > display_width: #if bullet out of screen, kill it. Better performance
            self.kill()

        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()

        if self.HP <= 30 and self.with_present:
            self.with_present = False
        if self.HP <= 0:
            self.kill()


#to satisfy peashooter class. Cant hide these behind a function.
is_invaded0 = is_invaded1 = is_invaded2 = is_invaded3 = is_invaded4 = False
bool_lane = [is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4]

# Lists
zombieSprite = pygame.sprite.Group()
sunList = pygame.sprite.Group()
squareList = []
allSprite = pygame.sprite.LayeredUpdates() #to update a portion of a map per frame
cardSprite = pygame.sprite.Group() #a bunch of cards
bulletSprite = pygame.sprite.Group() #a bunch of bullets
plantSprite = pygame.sprite.Group()
lawnmowerSprite = pygame.sprite.Group()
textSprite = pygame.sprite.Group()
befuddled_zombie = pygame.sprite.Group()

#function
def display_message(message, color, y_displace = 0):
    textSurface = myfont.render(message, True, color)
    textRect = textSurface.get_rect()
    textRect.center = [(display_width-50)/2, (display_height-100)/2 + y_displace]
    gameDisplay.blit(textSurface, textRect)

#MAP


#MAIN LOOP
def gameloop():
    gameDisplay.fill(black)
    global bool_lane
    global is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4
    global zombieSprite, sunList, squareList, allSprite, cardSprite, bulletSprite, plantSprite, befuddled_zombie

    gameStarted = False
    ls = pygame.image.load("miscellany\loadingscreen.png")
    gameDisplay.blit(ls, [707, 500])

    while gameStarted == False:
        gameDisplay.blit(ls, [0, 0, 707, 500])
        display_message('Press C to start the game or Q to quit', red, 50)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_c:
                    gameStarted = True
                    pygame.display.update()

    # Lists
    zombieSprite = pygame.sprite.Group()
    sunList = pygame.sprite.Group()
    squareList = []
    allSprite = pygame.sprite.LayeredUpdates()  # to update a portion of a map per frame
    cardSprite = pygame.sprite.Group()  # a bunch of cards
    bulletSprite = pygame.sprite.Group()  # a bunch of bullets
    plantSprite = pygame.sprite.Group()
    first_wave_zombie = pygame.sprite.Group()
    second_wave_zombie = pygame.sprite.Group()
    final_wave_Zombie = pygame.sprite.Group()
    befuddled_zombie = pygame.sprite.Group()

    counter = 0
    MousePressed = False  # to choose the card
    MouseDown = False  # when mouse is held down, drag the card
    MouseRelease = False
    Target = None  # target of drag, drop
    is_invaded0 = is_invaded1 = is_invaded2 = is_invaded3 = is_invaded4 = False
    bool_lane = [is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4]
    gameExit = False
    gameOver = False
    gameWin = False

    mapList = [
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
              ]

    #MAP
    squarelistlist = []
    x = 60
    y = 100
    for row in mapList:
        squares = []
        for column in row:
            a = Square(x, y)
            x += 60
            squares.append(a)
        y += 80
        x = 60
        squarelistlist.append(squares)

    fence = pygame.image.load(os.path.join(OTHER_FOLDER, 'fence.png'))
    gameDisplay.blit(fence, [0,0])
    deck_image = pygame.image.load(os.path.join(OTHER_FOLDER, 'deck.png'))
    gameDisplay.blit(deck_image, [10, 10])
    shovel_box = pygame.image.load(os.path.join(OTHER_FOLDER, 'shovel-box.png'))
    gameDisplay.blit(shovel_box, [420, 15])

    #add some tiles
    tile_image = pygame.image.load(os.path.join(OTHER_FOLDER, 'red-tile.jpg'))
    for i in range(5):
        gameDisplay.blit(tile_image,[660, (100+i*80)])
        gameDisplay.blit(tile_image, [0, 100+i*80])
    background = gameDisplay.copy()

    for i in range(5):
        Snowball(0, (100 + i * 80))

    sunbox = SunBox()
    SnowPea_card()
    Peashooter_card()
    Sunflower_card()
    Wallnut_card()
    PotatoMine_card()
    Hypnoshroom_card()
    Shovel()

    pygame.display.update()

    planning_stage = stage1 = stage2 = stage3 = False #stage is between waves
    wave1 = wave2 = wave3 = False
    wave01 = wave02 = wave03 = False




    while not gameExit:

        while gameOver:
            gameDisplay.fill(white)
            display_message('GAME OVER!', red, -50)
            display_message('Press C to play again or Q to quit', black, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameloop()


        #if you survive the final wave of zombie, you win

        while gameWin:
            gameDisplay.fill(white)
            display_message('YOU WON!', red, -50)
            display_message('Press C to play again or Q to quit', black, 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameWin = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameWin = False
                    elif event.key == pygame.K_c:
                        gameloop()

        counter += 1
        if counter % (5*FPS) == 0: #create new sun every five secs. falling randomly
            x = random.randint(0, 550)
            Sun(x=x, y=100, speed=1)

        if counter == 20*FPS:
            NormZombie(700)
            PoleZombie(690)
        elif counter == 30 * FPS:
            PresentZombie(700)
            planning_stage = True

        if planning_stage:
            if counter % (20 *FPS) == 0:
                x = 0
                for i in range(random.randint(1, 2)):
                    NormZombie(700-x)
                    x += 10
            if counter % (70*FPS) == 0:
                PoleZombie(700)

        if counter == 80 * FPS:
           planning_stage = False
           stage1 = True

        if stage1:
            if counter % (8*FPS) == 0:
                PresentZombie(700)
            elif counter % (20*FPS) == 0:
                x = 0
                for i in range(random.randint(2, 3)):
                    NormZombie(700-x)
                    x += 10
            elif counter % (50*FPS) == 0:
                PoleZombie(700)

        if counter == 110 * FPS:
            stage1 = False
            Message('A huge wave of zombie is approaching!', red, 40, 3000)

        elif counter == 113 * FPS:
            wave1 = True
            wave01 = True #to make sure

        if wave1:
            x = 0
            for i in range(5):
                zom = NormZombie(700-x)
                first_wave_zombie.add(zom)
                x += 7
            x = 0
            for i in range(2):
                zom = PresentZombie(700-x)
                first_wave_zombie.add(zom)
                x+= 10
            x = 0
            for i in range(2):
                zom = PoleZombie(700-x)
                first_wave_zombie.add(zom)
            wave1 = False #so that zombies don't ooze out in tides

        if wave01 and len(first_wave_zombie) == 0:
            wave01 = False
            stage2 = True

        if stage2:
            if counter % (6*FPS) == 0:
                NormZombie(700)
                NormZombie(690)
                PoleZombie(680)
            elif counter % (15*FPS) == 0:
                x = 0
                PresentZombie(700)
                for i in range(random.randint(1, 3)):
                    NormZombie(700 - x)
                    x += 10
            elif counter % (30*FPS) == 0:
                PoleZombie(700)

        if counter == 170 * FPS:
            stage2 = False
            wave02 = True
            Message('A huge wave of zombie is approaching!', red, 40, 3000)

        elif counter == 173 *FPS:
            wave2 = True

        if wave2:
            x = 0
            for i in range(6):
                zom = NormZombie(700-x)
                second_wave_zombie.add(zom)
                x+=7
            x = 0
            for i in range(3):
                zom = PresentZombie(700-x)
                second_wave_zombie.add(zom)
                x+=5
            x = 0
            for i in range(2):
                zom = PoleZombie(700-x)
                second_wave_zombie.add(zom)
            wave2 = False

        if wave02 and len(second_wave_zombie) == 0:
            wave02 = False
            stage3 = True

        if stage3:
            if counter % (5*FPS) == 0:
                x = 0
                for i in range(random.randint(1,3)):
                    NormZombie(700-x)
                    x += 10
            elif counter % (14*FPS) == 0:
                x = 0
                for i in range(random.randint(2, 4)):
                    NormZombie(700-x)
                    x += 7
                x = 0
                for i in range(2):
                    PresentZombie(700-x)
                    x += 10
            elif counter % (20*FPS) == 0:
                x = 0
                PoleZombie(700-x)

        if counter == 210 * FPS:
            stage3 = False
            Message('A huge wave of zombie is approaching!', red, 40, 3000)
        elif counter == 213 * FPS:
            Message('Final Wave', red, 60, 2000)
        elif counter == 215 * FPS:
            wave3 = True

        if wave3:
            x = 0
            for i in range(11):
                zom = NormZombie(700 - x)
                final_wave_Zombie.add(zom)
                x += 5
            x=0
            for i in range(5):
                zom = PresentZombie(700-x)
                final_wave_Zombie.add(zom)
                x+=5
            x=0
            for i in range(3):
                zom = PoleZombie(700-x)
                final_wave_Zombie.add(zom)
            wave3 = False
            wave03 = True

        if wave03 and len(final_wave_Zombie) == 0:
            gameWin = True



        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    MousePressed = True
                    MouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                MouseRelease = True
                MouseDown = False

            if MousePressed:
                for card in cardSprite:
                    if card.rect.collidepoint(mx, my) and card.available and sunbox.sun_capacity >= card.cost:
                        Target = card
                        break
                for sun in sunList:
                    if sun.rect.collidepoint(mx, my):
                        sunbox.update(25)
                        sun.kill()


            if MouseDown and Target:
                Target.move(mx, my)

            if MouseRelease and Target:
                square_x = int(mx/Square.x_size)-1
                square_y=int(my/Square.y_size)-1
                if isinstance(Target,Peashooter_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        Peashooter(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        Peashooter_card()
                        sunbox.update(-Peashooter_card.cost)
                    else: #do not activate cooldown, nor cost user sunScore
                        Peashooter_card(available = True)

                elif isinstance(Target,SnowPea_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        SnowPea(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        SnowPea_card()
                        sunbox.update(-SnowPea_card.cost)
                    else: #do not activate cooldown, nor cost user sunScore
                        SnowPea_card(available = True)

                elif isinstance(Target, Sunflower_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        Sunflower(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        Sunflower_card()
                        sunbox.update(-Sunflower_card.cost)
                    else:
                        Sunflower_card(available= True)

                elif isinstance(Target, Wallnut_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        Wallnut(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        Wallnut_card()
                        sunbox.update(-Wallnut_card.cost)
                    else:
                        Wallnut_card(available= True)

                elif isinstance(Target, Hypnoshroom_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        Hypnoshroom(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        Hypnoshroom_card()
                        sunbox.update(-Hypnoshroom_card.cost)
                    else:
                        Hypnoshroom_card(available= True)

                elif isinstance(Target,PotatoMine_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        PotatoMine(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        PotatoMine_card()
                        sunbox.update(-PotatoMine_card.cost)
                    else:
                        PotatoMine_card(available=True)

                elif isinstance(Target, Shovel):
                    for plant in plantSprite:
                        if plant.rect.collidepoint(mx, my):
                            plant.kill()
                            break
                    Shovel()

                Target.kill()
                Target = None


        MousePressed = False
        MouseRelease = False

        plantSprite.update()
        bulletSprite.update()
        sunList.update()
        zombieSprite.update()
        cardSprite.update()
        sunList.update()
        lawnmowerSprite.update()
        textSprite.update()
        befuddled_zombie.update()

        for i in range(len(bool_lane)):
            bool_lane[i] = False

        for zombie in zombieSprite:
            bool_lane[zombie.level - 1] = True
            bullets = pygame.sprite.spritecollide(zombie, bulletSprite, dokill = False) #list of bullets collding with zombie
            if bullets:
                for bullet in bullets:
                    zombie.bullet_collide(bullet)
                    bullet.kill()
            plants = pygame.sprite.spritecollide(zombie, plantSprite, dokill = False)

            if plants: #a zombie can only eat a plant once at any time. so list length is 1
                zombie.plant_collide(plants[0])
                if isinstance(plants[0], PotatoMine) and plants[0].explodable and not plants[0].dead_already:
                    zombie.kill()
                    plants[0].exploded()

            traitors = pygame.sprite.spritecollide(zombie, befuddled_zombie, dokill=False)
            if traitors:
                eating = False
                for traitor in traitors:
                    if traitor.level == zombie.level:
                        zombie.plant_collide(traitor)
                        eating = True
                        break

                if eating == False:
                    if isinstance(zombie, PoleZombie):
                        if zombie.status != 'jumping':
                            zombie.status = 'moving'
                    else:
                        zombie.status = 'moving'
            elif not plants and not traitors:
                if isinstance(zombie, PoleZombie):
                    if zombie.status != 'jumping':
                        zombie.status = 'moving'
                else:
                    zombie.status = 'moving'

            if zombie.rect.left <= 0:
                gameOver = True

        for traitorZombie in befuddled_zombie:
            bad_zombies = pygame.sprite.spritecollide(traitorZombie, zombieSprite, dokill = False)
            if bad_zombies:
                eating = False
                for bad_zombie in bad_zombies:
                    if bad_zombie.level == traitorZombie.level:
                        traitorZombie.plant_collide(bad_zombie)
                        eating = True
                        break
                if eating == False:
                    if isinstance(traitorZombie, PoleZombie):
                        if traitorZombie.status != 'jumping':
                            traitorZombie.status = 'moving'
                    else:
                        traitorZombie.status = 'moving'

            else:
                if isinstance(traitorZombie, PoleZombie):
                    if traitorZombie.status != 'jumping':
                        traitorZombie.status = 'moving'
                else:
                    traitorZombie.status = 'moving'

        allSprite.clear(gameDisplay, background)
        new_positions = allSprite.draw(gameDisplay)
        pygame.display.update(new_positions)

        clock.tick(FPS)
    pygame.quit()
    quit()

gameloop()

