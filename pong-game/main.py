import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

height = 120
width = 25
speed = 10

player_x = 25
player_y = 240
player_score = 0

enemy_x = 750
enemy_y = 240
enemy_score = 0

ball_x = 390
ball_y = 290

ball_speed_x =random.choice([-5,5])
ball_speed_y =random.choice([-5,5])

font = pygame.font.SysFont("Ariel", 36)
game_over_font = pygame.font.SysFont("Ariel", 60, bold=True)

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    pygame.draw.rect(screen, "blue", (player_x, player_y, width, height))
    pygame.draw.rect(screen, "red", (enemy_x, enemy_y, width, height))
    pygame.draw.rect(screen, "green", (ball_x, ball_y, 20, 20))

    player_score_text = font.render(f"Player: {player_score}", False, "white")
    player_score_rect = player_score_text.get_rect(center=(150,25))
    enemy_score_text = font.render(f"Enemy: {enemy_score}", False, "white")
    enemy_score_rect = enemy_score_text.get_rect(center=(620,25))
    screen.blit(player_score_text, player_score_rect)
    screen.blit(enemy_score_text, enemy_score_rect)

    player_rect = pygame.Rect(player_x, player_y, width, height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, width, height)
    ball_rect = pygame.Rect(ball_x, ball_y, 20, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False

    if not game_over:
        if ball_rect.colliderect(enemy_rect) and ball_speed_x > 0:
            ball_speed_x *= -1

        if ball_rect.colliderect(player_rect) and ball_speed_x < 0:
            ball_speed_x *= -1

        if ball_y <= 0 or ball_y >= 580:
            ball_speed_y *= -1

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x >= 780:
            ball_x = 390
            ball_y = 290
            ball_speed_x =random.choice([-5,5])
            ball_speed_y =random.choice([-5,5])
            player_score += 1

        if ball_x <= 0:
            ball_x = 390
            ball_y = 290
            ball_speed_x =random.choice([-5,5])
            ball_speed_y =random.choice([-5,5])
            enemy_score += 1

        if player_score == 5:
            game_over = True

        if enemy_score == 5:
            game_over = True

        if keys[pygame.K_w]:
            if player_y <= 0:
                player_y = 0
            else:
                player_y -= speed

        if keys[pygame.K_s]:
            if player_y >= 480:
                player_y = 480
            else:
                player_y += speed

        if keys[pygame.K_i]:
            if enemy_y <= 0:
                enemy_y = 0
            else:
                enemy_y -= speed
                
        if keys[pygame.K_k]:
            if enemy_y >= 480:
                enemy_y = 480
            else:
                enemy_y += speed

# SIMPLE ENEMY AI
#        if ball_speed_x > 0:
#            if enemy_y <= ball_y:
#                enemy_y += 3
#            if enemy_y >= 480:
#                enemy_y = 480
#            if enemy_y <= 0:
#                enemy_y = 0
#            if enemy_y >= ball_y:
#                enemy_y -= 3

    if game_over:
        game_over_text = game_over_font.render("Game over!", False, "red", "black")
        game_over_rect = game_over_text.get_rect(center=(400, 250))
        screen.blit(game_over_text, game_over_rect)
        if player_score >= 5:
            game_over_text = game_over_font.render("Player has won!", False, "red", "black")
            game_over_rect = game_over_text.get_rect(center=(400, 300))
            screen.blit(game_over_text, game_over_rect)
        elif enemy_score >= 5:
            game_over_text = game_over_font.render("Enemy has won!", False, "red", "black")
            game_over_rect = game_over_text.get_rect(center=(400, 300))
            screen.blit(game_over_text, game_over_rect)  
        game_over_text = font.render(f"Press Q to quit or R to restart", False, "red", "black")
        game_over_rect = game_over_text.get_rect(center=(400, 350))
        screen.blit(game_over_text, game_over_rect)

        if keys[pygame.K_r]:
            player_x = 25
            player_y = 240
            player_score = 0

            enemy_x = 750
            enemy_y = 240
            enemy_score = 0

            ball_x = 390
            ball_y = 290

            ball_speed_x =random.choice([-5,5])
            ball_speed_y =random.choice([-5,5])

            game_over = False

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
        
