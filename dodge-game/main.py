import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
player_x = 375
player_y = 550

score = 0

font = pygame.font.SysFont("Arial", 36)
game_over_font = pygame.font.SysFont("Arial", 60, bold=True)

obstacle_x = random.randint(0, 750)
obstacle_y = 0
obstacle_speed = 5

player_speed = 10
clock = pygame.time.Clock()

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    text_surface = font.render(f"Score: {score}", False, "white")
    screen.blit(text_surface, (0,0))

    pygame.draw.rect(screen, (0,102,204), (player_x,player_y,50,50))
    pygame.draw.rect(screen, (255,0,0), (obstacle_x,obstacle_y,50,50))

    keys = pygame.key.get_pressed()

    if not game_over:
        if obstacle_y >= 550:
            obstacle_y = 0
            obstacle_x = random.randint(0, 750)
            score += 1
            obstacle_speed += 0.5
        else:
            obstacle_y += obstacle_speed

        if keys[pygame.K_a]:
            if player_x <= 0:
                player_x = 0
            else:
                player_x -= player_speed
        if keys[pygame.K_d]:
            if player_x >= 750:
                player_x = 750
            else:
                player_x += player_speed

        player_rect = pygame.Rect(player_x, player_y, 50,50)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 50, 50)

        if player_rect.colliderect(obstacle_rect):
            game_over = True

    if game_over:
        text_surface = game_over_font.render("GAME OVER", False, "red")
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Press R to restart!", False, "red")
        text_rect = text_surface.get_rect(center=(400, 350))
        screen.blit(text_surface, text_rect)

        if keys[pygame.K_r]:

            score = 0

            player_x = 375
            player_y = 550

            obstacle_x = random.randint(0, 750)
            obstacle_y = 0
            obstacle_speed = 5

            game_over = False
            
    pygame.display.flip()
    clock.tick(60)

pygame.quit()