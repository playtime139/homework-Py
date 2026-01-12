import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game Screen")

font = pygame.font.SysFont(None, 40)
text = font.render("My First Game Screen", True, (0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((150, 200, 255))
    screen.blit(text, (150, 180))
    pygame.display.update()

pygame.quit()
