import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
player_x = 375
player_y = 550

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0,102,204), (player_x,player_y,50,50))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if player_x == 0:
            player_x = 0
        else:
            player_x -= 1
    if keys[pygame.K_d]:
        if player_x == 750:
            player_x = 750
        else:
            player_x += 1

    pygame.display.flip()

pygame.quit()