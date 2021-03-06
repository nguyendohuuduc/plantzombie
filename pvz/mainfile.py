# Always use updates. The only ones don't use update are the cards
import pygame, plants, others, random, os, bullets, zombies, cards

DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
OTHER_FOLDER = os.path.join(DIR_ROOT, 'miscellany')
SOUND_FOLDER = os.path.join(DIR_ROOT, 'sound')

pygame.mixer.pre_init()
pygame.init()

eating_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'eating_sound.ogg'))
hitting_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'hitting-sound.ogg'))
explosion_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'explosion.ogg'))
snowball_sound = pygame.mixer.Sound(file=os.path.join(SOUND_FOLDER, 'snowball-sound.ogg'))

pygame.mixer.set_num_channels(50)
pygame.mixer.music.load(os.path.join(SOUND_FOLDER, 'WateryGrave.ogg'))

pygame.mixer.music.play(-1)


myfont = pygame.font.SysFont('monospace', 25)
FPS = 40
display_width = 707
display_height = 500
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Plants vs Zombies-Christmas Edition')
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# classes


class Hypnoshroom(plants.Hypnoshroom):

    def __init__(self, x, y):
        super(Hypnoshroom, self).__init__(x, y)
        allSprite.add(self, layer=plants.Hypnoshroom.layer)
        plantSprite.add(self)

    def update(self):
        self.image = self.frames[self.cur_patch_num]
        self.change_frame(15)
        self.counter += 1
        self.check_dead()


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

        self.check_dead()

        now = pygame.time.get_ticks()
        if now - self.last >= self.deto_time and self.cur_patch_num != 2:
            self.cur_patch_num = 1
            self.explodable = True
        if self.cur_patch_num == 2:
            self.counter += 1
            if self.counter % (FPS) == 0:
                self.kill()


class Wallnut(plants.Wallnut):

    def __init__(self, x, y):
        super(Wallnut, self).__init__(x, y)
        allSprite.add(self, layer=plants.Wallnut.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Wallnut.x_size, Wallnut.y_size])

    def update(self):
        self.change_frame()
        self.check_dead()


class Sunflower(plants.Sunflower):

    def __init__(self, x, y):
        super(Sunflower, self).__init__(x, y)
        allSprite.add(self, layer=plants.Sunflower.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Sunflower.x_size, Sunflower.y_size])

    def generate_sun(self):
        others.Sun(x=self.rect.x, y=self.rect.y, speed=0, gameDisplay=gameDisplay, allSprite=allSprite, sunList=sunList)

    def update(self):
        self.counter += 1
        self.image = self.frames[self.cur_patch_num]
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_suns:
            self.last = now
            self.generate_sun()
        self.change_frame(10)
        self.check_dead()


class SnowPea(plants.SnowPea):

    def __init__(self, x, y):
        super(SnowPea, self).__init__(x, y)
        allSprite.add(self, layer=plants.SnowPea.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, SnowPea.x_size, SnowPea.y_size])

    def shoot_pea(self):
        bullets.Snowbullet(self.rect.x + SnowPea.x_size, self.rect.y + SnowPea.y_size/6, gameDisplay, allSprite, bulletSprite)

    def change_status(self):
        if bool_lane[int((self.rect.y - 100)/others.Square.y_size)]:
            self.status = 'working'
        else:
            self.status = 'idle'

    def update(self):
        self.change_status()
        self.counter += 1
        self.image = self.frames[self.cur_patch_num]
        self.change_frame(10)
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_bullet and self.status == 'working':
            self.last = now
            self.shoot_pea()
        self.check_dead()


class Peashooter(plants.Peashooter):

    def __init__(self, x, y):
        super(Peashooter, self).__init__(x, y)
        allSprite.add(self, layer=plants.Peashooter.layer)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Peashooter.x_size, Peashooter.y_size])

    def shoot_pea(self):
        bullets.Peabullet(self.rect.x + Peashooter.x_size, self.rect.y + Peashooter.y_size/6, gameDisplay, allSprite, bulletSprite)

    def change_status(self):
        if bool_lane[int((self.rect.y - 100)/others.Square.y_size)]:
            self.status = 'working'
        else:
            self.status = 'idle'

    def update(self):
        self.change_status()
        self.counter += 1
        self.image = self.frames[self.cur_patch_num]
        self.change_frame(10)
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_bullet and self.status == 'working':
            self.last = now
            self.shoot_pea()
        self.check_dead()


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
        self.mark = False  # so that the zombie wont eat the plant it just jumps over
        zombieSprite.add(self)
        allSprite.add(self, layer=zombies.PoleZombie.layer + self.level)

    def bullet_collide(self, bullet):
        if self.status != 'jumping':
            self.HP -= bullet.damage
            hitting_sound.play(maxtime=500)
            if isinstance(bullet, bullets.Snowbullet):  # I dont want to stack slowness
                self.condition.append('frost')
                self.last = pygame.time.get_ticks()

    def plant_collide(self, plant):
        if self.has_pole:
            self.status = 'jumping'
            if not self.mark:
                self.mark = plant  # so that only one plant is self.mark forever. Sometimes when zombie
                                   # jumps, it collide with another plant as well
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
                self.speed /= 2
                self.dps /= 2
            if now - self.last >= bullets.Snowbullet.effect_time:
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

        if 0 > self.rect.x or self.rect.x > display_width:  # if bullet out of screen, kill it. Better performance
            self.kill()

        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()

        if self.HP <= 0:
            self.kill()


class NormZombie(zombies.NormZombie):

    def __init__(self, x):
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
        if isinstance(bullet, bullets.Snowbullet):  # I dont want to stack slowness
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
                self.speed /= 2
                self.dps /= 2
            if now - self.last >= bullets.Snowbullet.effect_time:
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
        if isinstance(bullet, bullets.Snowbullet):  # I dont want to stack slowness
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
                self.speed /= 2
                self.dps /= 2
            if now - self.last >= bullets.Snowbullet.effect_time:
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
                    self.image = pygame.transform.flip(self.walking_frames3[self.at_frame_walking], True, False)
                else:
                    self.image = self.walking_frames3[self.at_frame_walking]
            else:
                if self.walking_counter % 15 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PresentZombie.frame_num1 - 1):
                    self.at_frame_walking = 0
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frames1[self.at_frame_walking], True, False)
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
                    self.image = pygame.transform.flip(self.eating_frames3[self.at_frame_eating],True,False)
                else:
                    self.image = self.eating_frames3[self.at_frame_eating]
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
                    self.image=pygame.transform.flip(self.walking_frames4[self.at_frame_walking], True, False)
                else:
                    self.image=self.walking_frames4[self.at_frame_walking]
            else:
                if self.walking_counter % 5 == 0:
                    self.at_frame_walking += 1
                if self.at_frame_walking > (PresentZombie.frame_num3 - 1):
                    self.at_frame_walking = 1
                if 'muddled' in self.condition:
                    self.image = pygame.transform.flip(self.walking_frames2[self.at_frame_walking],True,False)
                else:
                    self.image = self.walking_frames2[self.at_frame_walking]
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
                    self.image = self.eating_frames2[self.at_frame_eating]

        if 0 > self.rect.x or self.rect.x > display_width: #if bullet out of screen, kill it. Better performance
            self.kill()

        elif 0 > self.rect.y or self.rect.y > display_height:
            self.kill()

        if self.HP <= 30 and self.with_present:
            self.with_present = False
        if self.HP <= 0:
            self.kill()


# to satisfy peashooter/snowpea class. Cant hide these inside a function.
is_invaded0 = is_invaded1 = is_invaded2 = is_invaded3 = is_invaded4 = False
bool_lane = [is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4]

# Lists
zombieSprite = pygame.sprite.Group()
sunList = pygame.sprite.Group()
squareList = []
allSprite = pygame.sprite.LayeredUpdates()  # to update a portion of a map per frame
cardSprite = pygame.sprite.Group()  # a bunch of cards
bulletSprite = pygame.sprite.Group()  # a bunch of bullets
plantSprite = pygame.sprite.Group()
lawnmowerSprite = pygame.sprite.Group()
textSprite = pygame.sprite.Group()
befuddled_zombie = pygame.sprite.Group()


# function
def display_message(message, color, y_displace = 0):
    textSurface = myfont.render(message, True, color)
    textRect = textSurface.get_rect()
    textRect.center = [(display_width-50)/2, (display_height-100)/2 + y_displace]
    gameDisplay.blit(textSurface, textRect)

# MAP


# MAIN LOOP
def gameloop():
    gameDisplay.fill(black)
    global bool_lane
    global is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4
    global zombieSprite, sunList, squareList, allSprite, cardSprite, bulletSprite, plantSprite, befuddled_zombie


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

    # MAP
    squarelistlist = []
    x = 60
    y = 100
    for row in mapList:
        squares = []
        for column in row:
            a = others.Square(x=x, y=y, gameDisplay=gameDisplay, squareList=squareList)
            x += 60
            squares.append(a)
        y += 80
        x = 60
        squarelistlist.append(squares)

    fence = pygame.image.load(os.path.join(OTHER_FOLDER, 'fence.png'))
    gameDisplay.blit(fence, [0, 0])
    deck_image = pygame.image.load(os.path.join(OTHER_FOLDER, 'deck.png'))
    gameDisplay.blit(deck_image, [10, 10])
    shovel_box = pygame.image.load(os.path.join(OTHER_FOLDER, 'shovel-box.png'))
    gameDisplay.blit(shovel_box, [420, 15])

    # add some tiles
    tile_image = pygame.image.load(os.path.join(OTHER_FOLDER, 'red-tile.jpg'))
    for i in range(5):
        gameDisplay.blit(tile_image,[660, (100+i*80)])
        gameDisplay.blit(tile_image, [0, 100+i*80])
    background = gameDisplay.copy()

    for i in range(5):
        others.Snowball(0, (100 + i * 80), gameDisplay=gameDisplay, allSprite=allSprite, lawnmowerSprite=lawnmowerSprite)

    sunbox = others.SunBox(gameDisplay, allSprite)
    cards.SnowPea_card(available=False, gameDisplay=gameDisplay, x=315, y=20, allSprite=allSprite, cardSprite=cardSprite)
    cards.Peashooter_card(available=False, gameDisplay=gameDisplay, x=95, y=20, allSprite=allSprite, cardSprite=cardSprite)
    cards.Sunflower_card(available=False, gameDisplay=gameDisplay, x=150, y=20, allSprite=allSprite, cardSprite=cardSprite)
    cards.Wallnut_card(available=False, gameDisplay=gameDisplay, x=205, y=20, allSprite=allSprite, cardSprite=cardSprite)
    cards.PotatoMine_card(available=False, gameDisplay=gameDisplay, x=260, y=20, allSprite=allSprite, cardSprite=cardSprite)
    cards.Hypnoshroom_card(available=False, gameDisplay=gameDisplay, x=370, y=20, allSprite=allSprite, cardSprite=cardSprite)
    others.Shovel(x=425, y=20, gameDisplay=gameDisplay, allSprite=allSprite, cardSprite=cardSprite)

    pygame.display.update()

    planning_stage = stage1 = stage2 = stage3 = False  # stage is between waves
    wave1 = wave2 = wave3 = False
    wave01 = wave02 = wave03 = False

    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            display_message('Game over', red, -50)
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

        # if you survive the final wave of zombie, you win

        while gameWin:
            gameDisplay.fill(white)
            display_message('Game Win', red, -50)
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
        if counter % (5*FPS) == 0:  # create new sun every five secs. falling randomly
            x = random.randint(0, 550)
            others.Sun(x=x, y=100, speed=1, gameDisplay=gameDisplay, allSprite=allSprite, sunList=sunList)

        if counter == 20*FPS:
            NormZombie(700)

        elif counter == 30 * FPS:
            NormZombie(700)
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
            if counter % (10*FPS) == 0:
                PresentZombie(700)
            elif counter % (20*FPS) == 0:
                x = 0
                for i in range(random.randint(1, 3)):
                    NormZombie(700-x)
                    x += 10
            elif counter % (50*FPS) == 0:
                PoleZombie(700)

        if counter == 110 * FPS:
            stage1 = False
            others.Message('A huge wave of zombie is approaching!', red, 40, 3000, display_width, display_height,
                           gameDisplay, allSprite, textSprite)

        elif counter == 113 * FPS:
            wave1 = True
            wave01 = True  # to make sure

        if wave1:
            x = 0
            for i in range(4):
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
            wave1 = False  # so that zombies don't ooze out in tides

        if wave01 and len(first_wave_zombie) == 0:
            wave01 = False
            stage2 = True

        if stage2:
            if counter % (8*FPS) == 0:
                NormZombie(700)
                NormZombie(690)
                PoleZombie(680)
            elif counter % (20*FPS) == 0:
                x = 0
                PresentZombie(700)
                for i in range(random.randint(1, 3)):
                    NormZombie(700 - x)
                    x += 10
            elif counter % (35*FPS) == 0:
                PoleZombie(700)

        if counter == 170 * FPS:
            stage2 = False
            wave02 = True
            others.Message('A huge wave of zombie is approaching!', red, 40, 3000, display_width, display_height,
                           gameDisplay, allSprite, textSprite)

        elif counter == 173 * FPS:
            wave2 = True

        if wave2:
            x = 0
            for i in range(4):
                zom = NormZombie(700-x)
                second_wave_zombie.add(zom)
                x+=7
            x = 0
            for i in range(2):
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
            if counter % (8*FPS) == 0:
                x = 0
                for i in range(random.randint(1,3)):
                    NormZombie(700-x)
                    x += 10
            elif counter % (16*FPS) == 0:
                x = 0
                for i in range(random.randint(1, 4)):
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
            others.Message('A huge wave of zombie is approaching!', red, 40, 3000, display_width, display_height,
                           gameDisplay, allSprite, textSprite)
        elif counter == 213 * FPS:
            others.Message('Final Wave!', red, 60, 2000, display_width, display_height,
                           gameDisplay, allSprite, textSprite)
        elif counter == 215 * FPS:
            wave3 = True

        if wave3:
            x = 0
            for i in range(7):
                zom = NormZombie(700 - x)
                final_wave_Zombie.add(zom)
                x += 5
            x=0
            for i in range(2):
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
                        sunbox.update(25, gameDisplay)
                        sun.kill()

            if MouseDown and Target:
                Target.move(mx, my)

            if MouseRelease and Target:
                square_x = int(mx/others.Square.x_size)-1
                square_y = int(my/others.Square.y_size)-1
                if isinstance(Target, cards.Peashooter_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        Peashooter(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        cards.Peashooter_card(available=False, gameDisplay=gameDisplay, x=95, y=20, allSprite=allSprite, cardSprite=cardSprite)
                        sunbox.update(-cards.Peashooter_card.cost, gameDisplay)
                    else:  # do not activate cooldown, nor cost user sunScore
                        cards.Peashooter_card(available=True, gameDisplay=gameDisplay, x=95, y=20, allSprite=allSprite, cardSprite=cardSprite)

                elif isinstance(Target, cards.SnowPea_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        SnowPea(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        cards.SnowPea_card(available=False, gameDisplay=gameDisplay, x=315, y=20, allSprite=allSprite, cardSprite=cardSprite)
                        sunbox.update(-cards.SnowPea_card.cost, gameDisplay)
                    else:  # do not activate cooldown, nor cost user sunScore
                        cards.SnowPea_card(available=True, gameDisplay=gameDisplay, x=315, y=20, allSprite=allSprite, cardSprite=cardSprite)

                elif isinstance(Target, cards.Sunflower_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        Sunflower(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        cards.Sunflower_card(available=False, gameDisplay=gameDisplay, x=150, y=20, allSprite=allSprite, cardSprite=cardSprite)
                        sunbox.update(-cards.Sunflower_card.cost, gameDisplay)
                    else:
                        cards.Sunflower_card(available=True, gameDisplay=gameDisplay, x=150, y=20, allSprite=allSprite, cardSprite=cardSprite)

                elif isinstance(Target, cards.Wallnut_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        Wallnut(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        cards.Wallnut_card(available=False, gameDisplay=gameDisplay, x=205, y=20, allSprite=allSprite, cardSprite=cardSprite)
                        sunbox.update(-cards.Wallnut_card.cost, gameDisplay)
                    else:
                        cards.Wallnut_card(available=True, gameDisplay=gameDisplay, x=205, y=20, allSprite=allSprite, cardSprite=cardSprite)

                elif isinstance(Target, cards.Hypnoshroom_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        Hypnoshroom(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        cards.Hypnoshroom_card(available=False, gameDisplay=gameDisplay, x=370, y=20, allSprite=allSprite, cardSprite=cardSprite)
                        sunbox.update(-cards.Hypnoshroom_card.cost, gameDisplay)
                    else:
                        cards.Hypnoshroom_card(available=True, gameDisplay=gameDisplay, x=370, y=20, allSprite=allSprite, cardSprite=cardSprite)

                elif isinstance(Target, cards.PotatoMine_card):
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill=False):
                        PotatoMine(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        cards.PotatoMine_card(available=False, gameDisplay=gameDisplay, x=260, y=20, allSprite=allSprite, cardSprite=cardSprite)
                        sunbox.update(-cards.PotatoMine_card.cost, gameDisplay)
                    else:
                        cards.PotatoMine_card(available=True, gameDisplay=gameDisplay, x=260, y=20, allSprite=allSprite, cardSprite=cardSprite)

                elif isinstance(Target, others.Shovel):
                    for plant in plantSprite:
                        if plant.rect.collidepoint(mx, my):
                            plant.kill()
                            break
                    others.Shovel(x=425, y=20, gameDisplay=gameDisplay, allSprite=allSprite, cardSprite=cardSprite)

                Target.kill()
                Target = None

        MousePressed = False
        MouseRelease = False

        plantSprite.update()
        bulletSprite.update(display_width, display_height)
        sunList.update()
        zombieSprite.update()
        cardSprite.update(FPS)
        sunList.update()
        lawnmowerSprite.update(snowball_sound, display_width, zombieSprite)
        textSprite.update()
        befuddled_zombie.update()

        for i in range(len(bool_lane)):
            bool_lane[i] = False

        for zombie in zombieSprite:
            bool_lane[zombie.level - 1] = True
            bullets = pygame.sprite.spritecollide(zombie, bulletSprite, dokill=False)  # list of bullets collding with zombie
            if bullets:
                for bullet in bullets:
                    zombie.bullet_collide(bullet)
                    bullet.kill()
            plants = pygame.sprite.spritecollide(zombie, plantSprite, dokill=False)

            if plants:  # a zombie can only eat a plant once at any time. so list length is 1
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
                if not eating:
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
