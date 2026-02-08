import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader - Part 1")

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

player_img = pygame.Surface((40, 40))
player_img.fill((0, 255, 0))
player_x = 380
player_y = 500
player_speed = 5

enemy_imgs = []
enemy_x = []
enemy_y = []

for i in range(7):
    img = pygame.Surface((40, 40))
    img.fill((255, 0, 0))
    enemy_imgs.append(img)
    enemy_x.append(random.randint(0, 760))
    enemy_y.append(random.randint(50, 200))

def is_collision(px, py, ex, ey):
    distance = math.sqrt((px - ex)**2 + (py - ey)**2)
    return distance < 40

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 760:
        player_x += player_speed

    screen.blit(player_img, (player_x, player_y))

    for i in range(7):
        screen.blit(enemy_imgs[i], (enemy_x[i], enemy_y[i]))

        if is_collision(player_x, player_y, enemy_x[i], enemy_y[i]):
            score += 1
            enemy_x[i] = random.randint(0, 760)
            enemy_y[i] = random.randint(50, 200)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
