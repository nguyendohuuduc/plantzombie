#Always use updates. The only ones don't use update are the cards
import pygame, plants, others, zombies, random, os
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
OTHER_FOLDER = os.path.join(DIR_ROOT, 'miscellany')


pygame.init()
myfont = pygame.font.SysFont('monospace', 25)
FPS = 40
display_width = 650
display_height = 500
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Plants vs Zombies')
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


class SunBox(others.SunBox):
    def __init__(self):
        super(SunBox, self).__init__()
        self.add_to_screen()
        allSprite.add(self)

    def add_to_screen(self):
        myfont = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        scoretext=myfont.render(str(self.sun_capacity), 1,(0,0,0))
        self.image = pygame.image.load(os.path.join(OTHER_FOLDER, 'sunbox.jpg'))
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, SunBox.height, SunBox.width])
        self.image.blit(scoretext, (10, 43))

    def update(self, sun_amount):
        self.sun_capacity += sun_amount
        self.add_to_screen()


class Sunflower_card(plants.Sunflower_card):
    def __init__(self, x=130, y=20, available = False):
        super(Sunflower_card, self).__init__(x=x, y=y, available=available)
        self.add_to_screen()
        allSprite.add(self)
        cardSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Peashooter_card.size, Peashooter_card.size])


class Sunflower(plants.Sunflower):

    def __init__(self, x, y):
        super(Sunflower, self).__init__()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.add_to_screen()
        allSprite.add(self)
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

class Peashooter_card(plants.Peashooter_card):
    def __init__(self, x=80, y=20, available = False):
        super(Peashooter_card, self).__init__(x=x, y=y, available=available)
        self.add_to_screen()
        allSprite.add(self)
        cardSprite.add(self)


    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Peashooter_card.size, Peashooter_card.size])


class Peashooter(plants.Peashooter):

    def __init__(self, x, y):
        super(Peashooter, self).__init__(x, y)
        self.add_to_screen()
        allSprite.add(self)
        plantSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Square.x_size, Square.y_size])

    def shoot_pea(self):
        Peabullet(self.rect.x + Peashooter.x_size, self.rect.y + Peashooter.y_size/6)

    def change_status(self):
        if bool[int((self.rect.y - 100)/Square.y_size)]:
            self.status = 'working'
        else:
            self.status = 'idle'

    def update(self):
        self.change_status()
        now = pygame.time.get_ticks()
        if now - self.last >= self.between_bullet and self.status == 'working':
            self.last = now
            self.shoot_pea()
        if self.HP <= 0:
            self.kill()


class Peabullet(plants.Peabullet):

    def __init__(self, x, y):
        super(Peabullet, self).__init__(x, y)
        self.add_to_screen()
        allSprite.add(self)
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
        allSprite.add(self)

    def add_to_screen(self):
        gameDisplay.blit(self.image, [self.rect.x, self.rect.y, Sun.size, Sun.size])

    def update(self):
        self.rect.y += self.y_speed
        if self.rect.top > 500: #to improve performance
            self.kill()


class NormZombie(zombies.NormZombie):

    def __init__(self):
        super(NormZombie, self).__init__()
        self.image = self.walking_frames[0]
        self.rect = self.image.get_rect()
        self.level = random.randint(1, 5)
        self.rect.x = 625
        self.rect.y = 100 + self.level*80 - NormZombie.y_size
        zombieSprite.add(self)
        allSprite.add(self)

    def bullet_collide(self):
        self.HP -= 5

    def plant_collide(self, plant):
        plant.HP -= self.dps/FPS

    def update(self):
        if self.status == 'moving':
            self.walking_counter += 1
            self.eating_counter = 0
            self.rect.x += NormZombie.speed
            self.image = self.walking_frames[self.at_frame_walking]
            if self.walking_counter % 10 == 0:
                self.at_frame_walking += 1
            if self.at_frame_walking > (NormZombie.frame_num-1):
                self.at_frame_walking = 0

        elif self.status == 'eating':
            self.eating_counter += 1
            self.walking_counter = 0
            self.image = self.eating_frames[self.at_frame_eating]
            if self.eating_counter % 5 == 0:
                self.at_frame_eating += 1
            if self.at_frame_eating > (NormZombie.frame_num2-1):
                self.at_frame_eating = 0

        if self.HP <= 0:
            self.kill()

#to satisfy peashooter class. Cant hide these behind a function.
is_invaded0 = is_invaded1 = is_invaded2 = is_invaded3 = is_invaded4 = False
bool = [is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4]

# Lists
zombieSprite = pygame.sprite.Group()
sunList = pygame.sprite.Group()
squareList = []
allSprite = pygame.sprite.RenderUpdates() #to update a portion of a map per frame
cardSprite = pygame.sprite.Group() #a bunch of cards
bulletSprite = pygame.sprite.Group() #a bunch of bullets
plantSprite = pygame.sprite.Group()


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
    global bool
    global is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4
    global zombieSprite, sunList, squareList, allSprite, cardSprite, bulletSprite, plantSprite

    # Lists
    zombieSprite = pygame.sprite.Group()
    sunList = pygame.sprite.Group()
    squareList = []
    allSprite = pygame.sprite.RenderUpdates()  # to update a portion of a map per frame
    cardSprite = pygame.sprite.Group()  # a bunch of cards
    bulletSprite = pygame.sprite.Group()  # a bunch of bullets
    plantSprite = pygame.sprite.Group()

    counter = 0
    MousePressed = False  # to choose the card
    MouseDown = False  # when mouse is held down, drag the card
    MouseRelease = False
    Target = None  # target of drag, drop
    is_invaded0 = is_invaded1 = is_invaded2 = is_invaded3 = is_invaded4 = False
    bool = [is_invaded0, is_invaded1, is_invaded2, is_invaded3, is_invaded4]
    gameExit = False
    gameOver = False

    mapList = [
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
              ]

    #MAP
    squarelistlist = []
    x = 0
    y = 100
    for row in mapList:
        squares = []
        for column in row:
            a = Square(x, y)
            x += 60
            squares.append(a)
        y += 80
        x = 0
        squarelistlist.append(squares)

    pygame.draw.rect(gameDisplay, white, [0, 0, 400, 100])

    background = gameDisplay.copy()

    sunbox = SunBox()
    Peashooter_card()
    Sunflower_card()
    pygame.display.update()

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


        counter += 1
        if counter % (3*FPS) == 0: #create new sun every five secs. falling randomly
            x = random.randint(0, 550)
            Sun(x=x, y=100, speed=1)
        if counter % (10*FPS) == 0:
            NormZombie()

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
                Target.update(mx, my)

            if MouseRelease and Target:
                square_x = int(mx/Square.x_size)
                square_y=int(my/Square.y_size)-1
                if Target.signature == 0: #each card will have a signature
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        Peashooter(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        Peashooter_card()
                        sunbox.update(-Peashooter_card.cost)
                    else: #do not activate cooldown, nor cost user sunScore
                        Peashooter_card(available = True)

                elif Target.signature == 1:
                    if 0 <= square_x <= 9 and 0 <= square_y <= 4 \
                    and not pygame.sprite.spritecollide(squarelistlist[square_y][square_x], plantSprite, dokill = False):
                        Sunflower(squarelistlist[square_y][square_x].rect.left, squarelistlist[square_y][square_x].rect.top)
                        Sunflower_card()
                        sunbox.update(-Sunflower_card.cost)
                    else:
                        Sunflower_card(available= True)

                Target.kill()
                Target = None


        now = pygame.time.get_ticks() #check plants' cooldown
        for card in cardSprite:
            if now - card.last >= card.cooldown and not card.available:
                card.available = True

        for sun in sunList:
            if now - sun.last >= 10000: #10 seconds if unpicked, kill
                sun.kill()

        MousePressed = False
        MouseRelease = False

        plantSprite.update()
        bulletSprite.update()
        sunList.update()
        zombieSprite.update()
        for i in range(len(bool)):
            bool[i] = False

        for zombie in zombieSprite:
            bool[zombie.level - 1] = True
            bullets = pygame.sprite.spritecollide(zombie, bulletSprite, dokill = False) #list of bullets collding with zombie
            if bullets:
                zombie.bullet_collide()
                for bullet in bullets:
                    bullet.kill()
            plants = pygame.sprite.spritecollide(zombie, plantSprite, dokill = False)
            if plants: #a zombie can only eat a plant once at any time. so list length is 1
                zombie.plant_collide(plants[0])
                zombie.status = 'eating'
            elif not plants:
                zombie.status = 'moving'
            if zombie.rect.left <= 0:
                gameOver = True



        allSprite.clear(gameDisplay, background)
        new_positions = allSprite.draw(gameDisplay)
        pygame.display.update(new_positions)

        clock.tick(FPS)
    pygame.quit()
    quit()

gameloop()