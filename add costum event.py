import pygame
import random

pygame.init()


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event")


CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  


sprite1 = pygame.Rect(150, 180, 50, 50)
sprite2 = pygame.Rect(400, 180, 50, 50)

color1 = (255, 0, 0)
color2 = (0, 0, 255)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    pygame.display.update()

pygame.quit()
