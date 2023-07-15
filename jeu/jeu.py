# Simple click game in Python
# You have to click on bubbles before they leave the screen
import pygame
import random
import os

# Path to filesystem defintions
main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, "assets")

# pygame setup // Reminder : (0,0) = upper left corner
pygame.init()
pygame.display.set_caption("Super Bubble 3000")
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
dt = 0
color_bg = (31, 38, 46)
color_yellow = (255, 162, 0)
# color_white = (255, 255, 255, 50)
score = 0
bubble_count = 0
BUBBLE_RELOAD = 30  # frames between new bubbles
BUBBLE_ODDS = 20  # chances a new bubble appears
bubbles_reload = BUBBLE_RELOAD

font = pygame.font.Font(None, 64)
score_display = font.render(str(score), True, (color_yellow))
score_position = score_display.get_rect(top=10, left=10)


def msgDisplay(text):
    font = pygame.font.Font(None, 128)
    message = font.render(text, True, (color_yellow))
    message_position = message.get_rect(
        centerx=SCREEN_WIDTH / 2, centery=SCREEN_HEIGHT / 2)
    screen.blit(message, message_position)
    if paused:
        pygame.display.update()


def pause():
    global paused
    paused = True
    global running
    msgDisplay('PAUSE')
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = False


def loadImage(name):
    fullname = os.path.join(assets_dir, name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image, image.get_rect()


class Sight(pygame.sprite.Sprite):
    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image, self.rect = loadImage("sight.png")
        self.shooting = False

    def update(self):
        position = pygame.mouse.get_pos()
        self.rect.center = position

    def fire(self, target):
        print("FEU !")
        for bubble in pygame.sprite.spritecollide(self,target,0):
            bubble.shooted = True
            print("Touché :", id(bubble))




class Bubble(pygame.sprite.Sprite):

    BUBBLE_VALUE = 15
    BUBBLE_SPEED = -5
    BUBBLE_SIZE = 50

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image, self.rect = loadImage("bubble.png")
        self.size = self.rect.width
        self.shooted = False
        self._randomSize()
        self._initRandomPosition()
        global bubble_count
        bubble_count += 1
        print('Nouvelle Bulle de taille :', self.size, 'ID :', id(self), "Bubble_count =", bubble_count)

    def update(self):
        global score
        self.touched()
        if self.rect.bottom < 0:
            self._destroy()
            score -= self.BUBBLE_VALUE * 2
        self._flyToTop()

    def _destroy(self):
        global bubble_count
        bubble_count -= 1
        print('Destruction Bulle ID :', id(self), "Bubble_count =", bubble_count)  # Debug
        self.kill()

    def _randomSize(self):
        self.size = random.randint(1, 6) * self.BUBBLE_SIZE
        self.BUBBLE_VALUE = self.size
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()

    def _initRandomPosition(self):
        offset = self.size // 2
        self.rect.centery = SCREEN_HEIGHT
        self.rect.centerx = random.randint(offset, SCREEN_WIDTH - offset)

    def _flyToTop(self):
        speed = self.BUBBLE_SPEED * (self.size / 300) -2
        new_position = self.rect.move(random.randint(-3, 3), speed)
        self.rect = new_position

    def touched(self):
        global score
        if self.shooted:
            score += self.BUBBLE_VALUE
            self._destroy()


running = True
paused = False
gameover = False

# Initialize game Objects
bubbles = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()
sight = Sight(all)
Bubble(bubbles, all)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not gameover and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause()

        if event.type == pygame.MOUSEBUTTONDOWN:
            sight.fire(bubbles)

    # Create new bubble
    if bubbles_reload:
        bubbles_reload = bubbles_reload - 1
    elif not int(random.random() * BUBBLE_ODDS):
        Bubble(bubbles, all)
        bubbles_reload = BUBBLE_RELOAD

    # Reset scene
    screen.fill(color_bg)
    all.update()

    # Game Over
    if score <= -1000:
        gameover = True
        msgDisplay('GAME OVER')
    else:
        score_display = font.render(str(score), True, (color_yellow))
        screen.blit(score_display, score_position)

    # Render the scene
    all.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
