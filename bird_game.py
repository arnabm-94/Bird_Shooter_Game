import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird Shooter")

# Load images and resize
bird_img = pygame.transform.scale(pygame.image.load("bird.png"), (40, 40))
bomb_img = pygame.transform.scale(pygame.image.load("bomb.png"), (40, 40))
brick_img = pygame.transform.scale(pygame.image.load("brick.png"), (40, 40))
gun_img = pygame.transform.scale(pygame.image.load("gun.png"), (100, 100))
background_img = pygame.transform.scale(pygame.image.load("background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
rock_img = pygame.transform.scale(pygame.image.load("rock.png"), (40, 40))  
game_over_img = pygame.transform.scale(pygame.image.load("game_over.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up game variables
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 100
player_speed = 5
player_width = gun_img.get_width()
player_height = gun_img.get_height()

bird_width = bird_img.get_width()
bird_height = bird_img.get_height()
birds = []
bird_speed = 3
bird_spawn_rate = 60  # Adjust spawn rate as needed

bomb_width = bomb_img.get_width()
bomb_height = bomb_img.get_height()
bombs = []
bomb_speed = 3
bomb_spawn_rate = 100  # Adjust spawn rate as needed

brick_width = brick_img.get_width()
brick_height = brick_img.get_height()
bricks = []
brick_speed = 5
brick_spawn_rate = 120  # Adjust spawn rate as needed

rock_width = rock_img.get_width()  # New obstacle width
rock_height = rock_img.get_height()  # New obstacle height
rocks = []  # New obstacle list
rock_speed = 9  # New obstacle speed
rock_spawn_rate = 150  # Adjust spawn rate as needed for new obstacle

score = 0
level = 1
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Function to draw player, birds, bombs, bricks, and rocks
def draw_elements():
    screen.blit(background_img, (0, 0))  # Draw background
    screen.blit(gun_img, (player_x, player_y))
    for bird in birds:
        screen.blit(bird_img, (bird[0], bird[1]))
    for bomb in bombs:
        screen.blit(bomb_img, (bomb[0], bomb[1]))
    for brick in bricks:
        screen.blit(brick_img, (brick[0], brick[1]))
    for rock in rocks:  # Draw rocks
        screen.blit(rock_img, (rock[0], rock[1]))

# Function to update game level
def update_level():
    global level
    print("Score:", score, "Level:", level)  # Debugging line
    if score >= 15 and level == 1:
        level = 2
        pygame.display.set_caption("Bird Shooter - Level 2")
    elif score >= 20 and level == 2: 
        level = 3
        pygame.display.set_caption("Bird Shooter - Level 3")

# Main game loop
running = True
game_over = False
game_over_time = 0
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if game_over:
        if pygame.time.get_ticks() - game_over_time > 2000:  # 2 seconds
            pygame.quit()
            sys.exit()
        else:
            screen.blit(game_over_img, (0, 0))
            pygame.display.update()
            continue  # Skip the rest of the loop if game over
    
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    
    # Spawn birds
    if random.randint(1, bird_spawn_rate) == 1:
        bird_x = random.randint(0, SCREEN_WIDTH - bird_width)
        bird_y = -bird_height
        birds.append([bird_x, bird_y])
    
    # Move and remove birds
    for bird in birds:
        bird_rect = pygame.Rect(bird[0], bird[1], bird_width, bird_height)
        bird[1] += bird_speed
        if bird[1] > SCREEN_HEIGHT:
            birds.remove(bird)
        if bird_rect.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            score += 1
            birds.remove(bird)
    
    # Spawn bombs
    if random.randint(1, bomb_spawn_rate) == 1:
        bomb_x = random.randint(0, SCREEN_WIDTH - bomb_width)
        bomb_y = -bomb_height
        bombs.append([bomb_x, bomb_y])
    
    # Move and remove bombs
    for bomb in bombs:
        bomb_rect = pygame.Rect(bomb[0], bomb[1], bomb_width, bomb_height)
        bomb[1] += bomb_speed
        if bomb[1] > SCREEN_HEIGHT:
            bombs.remove(bomb)
        if bomb_rect.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            game_over = True
            game_over_time = pygame.time.get_ticks()

    # If in level 2, spawn bricks
    if level == 2:
        if random.randint(1, brick_spawn_rate) == 1:
            brick_x = random.randint(0, SCREEN_WIDTH - brick_width)
            brick_y = -brick_height
            bricks.append([brick_x, brick_y])

        # Move and remove bricks
        for brick in bricks:
            brick_rect = pygame.Rect(brick[0], brick[1], brick_width, brick_height)
            brick[1] += brick_speed
            if brick[1] > SCREEN_HEIGHT:
                bricks.remove(brick)
            if brick_rect.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                game_over = True
                game_over_time = pygame.time.get_ticks()

    # Spawn rocks
    if level == 3:
        if random.randint(1, rock_spawn_rate) == 1:
            rock_x = random.randint(0, SCREEN_WIDTH - rock_width)
            rock_y = -rock_height
            rocks.append([rock_x, rock_y])

        # Move and remove rocks
        for rock in rocks:
            rock_rect = pygame.Rect(rock[0], rock[1], rock_width, rock_height)
            rock[1] += rock_speed
            if rock[1] > SCREEN_HEIGHT:
                rocks.remove(rock)
            if rock_rect.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                game_over = True
                game_over_time = pygame.time.get_ticks()
    
    # Draw elements
    draw_elements()
    
    # Display score and level in a box
    score_box = pygame.Rect(10, 10, 150, 50)
    pygame.draw.rect(screen, YELLOW, score_box)
    level_box = pygame.Rect(10, 70, 150, 50)
    pygame.draw.rect(screen, GREEN, level_box)
    
    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)
    screen.blit(score_text, (score_box.x + 10, score_box.y + 10))
    screen.blit(level_text, (level_box.x + 10, level_box.y + 10))
    
    # Update the game level
    update_level()
    
    # Update the display
    pygame.display.update()
    
    # Tick clock
    clock.tick(60)

# Game over
screen.blit(game_over_img, (0, 0))
screen.blit(game_over_img, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 20))
pygame.display.update()

# Wait for a moment before quitting
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()




































