import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Player settings
player_width = 100
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 10

# Object settings
object_width = 30
object_height = 30
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height
object_speed = 5

# Game settings
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(white)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the falling object
    object_y += object_speed

    # Check if the object is caught
    if (player_x < object_x < player_x + player_width or
        player_x < object_x + object_width < player_x + player_width) and \
       player_y < object_y + object_height < player_y + player_height:
        score += 1
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height
        object_speed += 0.5  # Increase difficulty

    # Reset object if it goes off the screen
    if object_y > screen_height:
        object_x = random.randint(0, screen_width - object_width)
        object_y = -object_height

    # Draw player and object
    pygame.draw.rect(screen, blue, (player_x, player_y,
                     player_width, player_height))
    pygame.draw.rect(screen, red, (object_x, object_y,
                     object_width, object_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
