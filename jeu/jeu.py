# Example file showing a basic pygame "game loop"
import pygame
import random
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(main_dir, "assets")

# pygame setup // Rappel : Coordonnées (0,0) = coin supérieur gauche
pygame.init()
pygame.display.set_caption("Super Bubble 3000")
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
dt = 0
color_bg = (31, 38, 46)
color_yellow = (255, 162, 0)
# color_white = (255, 255, 255, 50)
score = 0
bubble_count = 0
BUBBLE_RELOAD = 30 # frames between new bubbles
BUBBLE_ODDS = 22  # chances a new bubble appears
bubbles_reload = BUBBLE_RELOAD

font = pygame.font.Font(None, 64)
score_display = font.render(str(score), True, (color_yellow))
score_position = score_display.get_rect(top=10, left=10)


def msgDisplay(text):
    font = pygame.font.Font(None, 128)
    message = font.render(text, True, (color_yellow))
    message_position = message.get_rect(
        centerx=screen_width / 2, centery=screen_height / 2)
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
        if not self.shooting:
            self.shooting = True
            return self.rect.colliderect(target.rect)


class Bubble(pygame.sprite.Sprite):

    VALUE = 15

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image, self.rect = loadImage("bubble.png")
        self.size = self.rect.width
        self.shooted = False
        self._randomSize()
        self._initRandomPosition()
        global bubble_count
        bubble_count += 1
        #print(bubble_count)

    def update(self):
        global score
        if self.rect.bottom < 0:
            self._destroy()
            score -= 10
        self._flyToTop()

    def _destroy(self):
        self.remove()
        global bubble_count
        bubble_count -= 1
        print('Destruction :',bubble_count)

    def _randomSize(self):
        self.size = random.randint(50, 200)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        print('Nouvel objet Bulle de taille :', self.size)

    def _initRandomPosition(self):
        offset = self.size // 2
        self.rect.centery = screen_height
        self.rect.centerx = random.randint(offset, screen_width - offset)

    def _flyToTop(self):
        new_position = self.rect.move(random.randint(-3, 3), -10)
        self.rect = new_position

    def touched(self):
        if not self.shooted:
            self._destroy()
            score += self.VALUE


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
            if sight.fire(bubble):
                pass

    # Create new bubble
    if bubbles_reload:
        bubbles_reload = bubbles_reload - 1
    elif not int(random.random() * BUBBLE_ODDS):
        Bubble(bubbles, all)
        bubbles_reload = BUBBLE_RELOAD

    # Reset scene
    screen.fill(color_bg)
    all.update()

    # RENDER YOUR GAME HERE
    if score <= -5000:
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
