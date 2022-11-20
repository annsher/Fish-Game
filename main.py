import time
import pygame
import random
from os import path
import sys

img_dir = path.join(path.dirname(__file__), 'img')
font_name = pygame.font.match_font('helvetica')

WIDTH = 600
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish hunt")
clock = pygame.time.Clock()

def show_go_screen():
    screen.blit(goscreen, goscreen_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                     waiting = False

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 70 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def newmob():
    m = BigFish()
    all_sprites.add(m)
    bigfish.add(m)
    m = SmallFish()
    all_sprites.add(m)
    smallfish.add(m)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(path.join(img_dir, "player.png")).convert())
        self.images[0] = pygame.transform.scale(self.images[0], (90, 50))
        self.images[0].set_colorkey(BLACK)
        self.rect = self.images[0].get_rect()
        self.images.append(pygame.image.load(path.join(img_dir, "player.png")).convert())
        self.images[1] = pygame.transform.scale(self.images[1], (90, 50))
        self.images[1] = pygame.transform.flip(self.images[1], True, False)
        self.images[1].set_colorkey(BLACK)
        self.index = 0
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH / 2
        self.speedx = 0
        self.speedy = 0
        self.image = self.images[self.index]
    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -3
        elif keystate[pygame.K_s]:
            self.speedy = 3
        elif keystate[pygame.K_a]:
            self.speedx = -3
            self.index = 0
            self.image = self.images[self.index]
        elif keystate[pygame.K_d]:
            self.index = 1
            self.image = self.images[self.index]
            self.speedx = 3
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class BigFish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(path.join(img_dir, "bigfish.png")).convert())
        self.images[0] = pygame.transform.scale(self.images[0], (100, 100))
        self.images[0].set_colorkey(BLACK)
        self.rect = self.images[0].get_rect()
        self.images.append(pygame.image.load(path.join(img_dir, "bigfish.png")).convert())
        self.images[1] = pygame.transform.scale(self.images[1], (100, 100))
        self.images[1] = pygame.transform.flip(self.images[1], True, False)
        self.images[1].set_colorkey(BLACK)
        self.rect = self.images[1].get_rect()
        self.index = random.randrange(0,2)
        self.image = self.images[self.index]
        if self.index == 1:
            self.rect.x = random.randrange(-20, -2)
            self.rect.y = random.randrange(75, 525, 75)
            self.speedx = random.randrange(2, 5)
        elif self.index == 0:
            self.rect.x = random.randrange(WIDTH + 5, WIDTH + 15)
            self.rect.y = random.randrange(75, 525, 75)
            self.speedx = random.randrange(-5, -2)

    def update(self):
        self.rect.x += self.speedx
        if (self.rect.left < -25 and self.index == 0) or (self.rect.left > WIDTH + 20 and self.index == 1):
            self.index = random.randrange(0, 2)
            if self.index == 1:
                self.image = self.images[self.index]
                self.rect.x = random.randrange(-20, -2)
                self.rect.y = random.randrange(75, 525, 75)
                self.speedx = random.randrange(2, 5)
            elif self.index == 0:
                self.image = self.images[self.index]
                self.rect.x = random.randrange(WIDTH + 5, WIDTH + 15)
                self.rect.y = random.randrange(75, 525, 75)
                self.speedx = random.randrange(-5, -2)

class SmallFish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(path.join(img_dir, "smallfish.png")).convert())
        self.images[0] = pygame.transform.scale(self.images[0], (60, 40))
        self.images[0].set_colorkey(BLACK)
        self.rect = self.images[0].get_rect()
        self.images.append(pygame.image.load(path.join(img_dir, "smallfish.png")).convert())
        self.images[1] = pygame.transform.scale(self.images[1], (60, 40))
        self.images[1] = pygame.transform.flip(self.images[1], True, False)
        self.images[1].set_colorkey(BLACK)
        self.rect = self.images[1].get_rect()
        self.index = random.randrange(0,2)
        self.image = self.images[self.index]
        if self.index == 1:
            self.rect.x = random.randrange(-20, -2)
            self.rect.y = random.randrange(40, 560, 50)
            self.speedx = random.randrange(2, 5)
        elif self.index == 0:
            self.rect.x = random.randrange(WIDTH + 5, WIDTH + 15)
            self.rect.y = random.randrange(40, 560, 50)
            self.speedx = random.randrange(-5, -2)

    def update(self):
        self.rect.x += self.speedx
        if (self.rect.left < -25 and self.index == 0) or (self.rect.left > WIDTH + 20 and self.index == 1):
            self.index = random.randrange(0, 2)
            if self.index == 1:
                self.image = self.images[self.index]
                self.rect.x = random.randrange(-20, -2)
                self.rect.y = random.randrange(40, 560, 50)
                self.speedx = random.randrange(2, 5)
            elif self.index == 0:
                self.image = self.images[self.index]
                self.rect.x = random.randrange(WIDTH + 5, WIDTH + 15)
                self.rect.y = random.randrange(40, 560, 50)
                self.speedx = random.randrange(-5, -2)

goscreen = pygame.image.load(path.join(img_dir, "start.jpg")).convert()
goscreen = pygame.transform.scale(goscreen, (WIDTH, HEIGHT))
goscreen_rect = goscreen.get_rect()
endscreen = pygame.image.load(path.join(img_dir, "end.jpg")).convert()
endscreen = pygame.transform.scale(endscreen, (WIDTH, HEIGHT))
endscreen_rect = endscreen.get_rect()
background = pygame.image.load(path.join(img_dir, "bg.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "player.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (60, 30))
player_mini_img.set_colorkey(BLACK)
lives = 5
score = 0
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
bigfish = pygame.sprite.Group()
smallfish = pygame.sprite.Group()
for i in range(2):
    m = BigFish()
    all_sprites.add(m)
    bigfish.add(m)
for i in range(2):
    m = SmallFish()
    all_sprites.add(m)
    smallfish.add(m)
running = True
game_over = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        lives = 5
        score = 0
        all_sprites = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        bigfish = pygame.sprite.Group()
        smallfish = pygame.sprite.Group()
        for i in range(2):
            newmob()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if lives == 0:
        screen.blit(endscreen, endscreen_rect)
        pygame.display.flip()
        time.sleep(2)
        game_over = True
    fish_hits = pygame.sprite.spritecollide(player, bigfish, True)
    for hit in fish_hits:
        lives -= 1
        m = BigFish()
        all_sprites.add(m)
        bigfish.add(m)
    fish_eats = pygame.sprite.spritecollide(player, smallfish, True)
    for hit in fish_eats:
        score += 1
        m = SmallFish()
        all_sprites.add(m)
        smallfish.add(m)

    all_sprites.update()

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_lives(screen, 0, 5, lives, player_mini_img)
    draw_text(screen, "Съедено рыб: " + str(score), 24, WIDTH - 90, 10)
    pygame.display.flip()

pygame.quit()
sys.exit()