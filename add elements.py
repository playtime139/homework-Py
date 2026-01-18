import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont(None, 40)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))         
    pygame.draw.rect(screen, (0, 0, 255), (200, 150, 200, 60))  
    screen.blit(font.render("Hello!", True, (0, 0, 0)), (250, 160))  

    pygame.display.update()

pygame.quit()
