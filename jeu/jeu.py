# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
pygame.display.set_caption("Super Bubble 3000")
# Coordonnées (0,0) coin supérieur gauche
screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
dt = 0
color_bg = (31, 38, 46)
color_yellow = (255, 162, 0)
color_white = (255, 255, 255, 50)


class Bubble:
    bubble_image = pygame.image.load("bubble.png").convert_alpha()

    def __init__(self) -> None:
        size_factor = random.randint(100, 300)
        print(size_factor)
        bubble = pygame.transform.scale(
            self.bubble_image, (size_factor, size_factor))
        bubble.get_rect()

    def randomSize():
        return random.randint(100, 300)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height())

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            size_factor = random.randint(100, 300)
            bubble = pygame.transform.scale(
                bubble_image, (size_factor, size_factor))
            print('Change la taille à :', size_factor)
        """

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color_bg)

    # RENDER YOUR GAME HERE
    bubble = Bubble()

    """
    screen.blit(bubble, player_pos -
        (bubble.get_height()/2, bubble.get_width() / 2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_e] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    """

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()
