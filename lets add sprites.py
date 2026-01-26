import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Sprites")

# Clock (controls FPS)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite sizes
SPRITE_WIDTH = 60
SPRITE_HEIGHT = 60

# Player sprite (controlled)
player = pygame.Rect(100, 100, SPRITE_WIDTH, SPRITE_HEIGHT)

# Second sprite (static)
enemy = pygame.Rect(500, 300, SPRITE_WIDTH, SPRITE_HEIGHT)

# Movement speed
speed = 5

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    # Draw sprites
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()
