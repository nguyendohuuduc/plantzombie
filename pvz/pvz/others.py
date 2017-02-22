#MODULE CREATION
import pygame
import os
import functions


DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
OTHER_FOLDER = os.path.join(DIR_ROOT, 'miscellany')


class Square(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'snowy.jpg'))
    x_size = 60
    y_size = 80

    def __init__(self, x, y, gameDisplay, squareList):
        super(Square, self).__init__()
        self.image = Square.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_size = Square.x_size
        self.y_size = Square.y_size
        functions.add_to_screen(self, gameDisplay)
        squareList.append(self)


class Sun(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'snowflake.png'))
    size = 65
    y_speed = 1
    layer = 9

    def __init__(self, x, y, speed, gameDisplay, allSprite, sunList):
        super(Sun, self).__init__()
        self.image = Sun.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_size = self.y_size = Sun.size
        self.y_speed = speed
        self.last = pygame.time.get_ticks()
        functions.add_to_screen(self, gameDisplay)
        allSprite.add(self, layer=Sun.layer)
        sunList.add(self)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= 15000:
            self.kill()
        self.rect.y += self.y_speed
        if self.rect.bottom >= 500:  # to improve performance
            self.y_speed = 0


class SunBox(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'sunbox.png'))
    width = 62
    height = 59

    def __init__(self):
        super(SunBox, self).__init__()
        self.image = SunBox.image
        self.rect = self.image.get_rect()
        self.rect.x = 17
        self.rect.y = 19
        self.sun_capacity = 50


class Shovel(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'snow-shovel.png'))
    width = 56
    height = 60
    layer = 9

    def __init__(self, x, y, gameDisplay, allSprite, cardSprite):
        super(Shovel, self).__init__()
        self.image = Shovel.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.signature = -1
        self.last = -1
        self.cooldown = -1
        self.cost = 0
        self.x_size = Shovel.width
        self.y_size = Shovel.height
        self.available = True
        functions.add_to_screen(self, gameDisplay)
        allSprite.add(self, layer=Shovel.layer)
        cardSprite.add(self)

    def move(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y


class Snowball(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(OTHER_FOLDER, 'Snowballs.png'))
    width = 60
    height = 60
    speed = 5
    layer = 9

    def __init__(self, x, y, gameDisplay, allSprite, lawnmowerSprite):
        super(Snowball, self).__init__()
        self.image = Snowball.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_size = Snowball.width
        self.y_size = Snowball.height
        self.speed = Snowball.speed
        self.status = 'idle'
        self.sound_play = False  # to ensure that sound is only played once. Bc sound in update, it keeps playing otherwise.
        functions.add_to_screen(self, gameDisplay)
        allSprite.add(self, layer=Snowball.layer)
        lawnmowerSprite.add(self)

    def update(self, snowball_sound, display_width, zombieSprite):
        if self.status == 'moving':
            self.rect.x += self.speed
            if not self.sound_play:
                self.sound_play = True
                snowball_sound.play(maxtime=3200)
        if self.rect.x >= display_width:
            self.kill()
        for zombie in zombieSprite:
            if self.rect.colliderect(zombie.rect):
                self.status = 'moving'
                zombie.kill()


class Message(pygame.sprite.Sprite):
    font = os.path.join(OTHER_FOLDER, 'blood_font.otf')
    layer = 10

    def __init__(self, string, color, size, time, display_width, display_height, gameDisplay, allSprite, textSprite):
        super(Message, self).__init__()
        myFont = pygame.font.Font(Message.font, size)
        textmessage = myFont.render(string, 1, color)
        self.image = textmessage
        self.rect = self.image.get_rect()
        self.rect.center = (display_width/2, display_height/2)
        self.last = pygame.time.get_ticks()
        self.time_last = time
        gameDisplay.blit(self.image, [self.rect.left, self.rect.top])
        allSprite.add(self, layer=Message.layer)
        textSprite.add(self)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.time_last:
            self.kill()


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")