# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
pygame.display.set_caption("Super Bubble 3000")
# Coordonnées (0,0) coin supérieur gauche
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
dt = 0
color_bg = (31, 38, 46)
color_yellow = (255, 162, 0)
# color_white = (255, 255, 255, 50)
score = 0

font = pygame.font.Font(None, 64)
score_display = font.render(str(score), True, (color_yellow))
score_position = score_display.get_rect(top=10, left=10)


def createBubble():
    bubble_image = pygame.image.load("bubble.png").convert_alpha()
    size_factor = random.randint(100, 300)
    print('Nouvelle bulle de taille :', size_factor)
    bubble = pygame.transform.scale(
        bubble_image, (size_factor, size_factor))
    return bubble


def randomSize():
    return random.randint(50, 200)


def initBubblePosition(bubble):
    bubble_position = bubble.get_rect()
    bubble_position.top = screen_height
    bubble_offset = bubble_position.width // 2
    bubble_position.centerx = random.randint(
        bubble_offset, screen_width - bubble_offset)
    return bubble_position


def resetBubble(object):
    del object
    new_bubble = createBubble()
    global bubble_position
    bubble_position = initBubblePosition(new_bubble)
    return new_bubble


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


bubble = createBubble()
bubble_position = initBubblePosition(bubble)

running = True
paused = False
gameover = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not gameover and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause()

    bubble_position = bubble_position.move(random.randint(-3, 3), -10)

    if bubble_position.bottom < 0:
        score -= 10
        bubble = resetBubble(bubble)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color_bg)

    # RENDER YOUR GAME HERE
    if score <= -50:
        gameover = True
        msgDisplay('GAME OVER')
    else:
        score_display = font.render(str(score), True, (color_yellow))
        screen.blit(score_display, score_position)
    screen.blit(bubble, bubble_position)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
