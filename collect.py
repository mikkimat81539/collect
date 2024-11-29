"""Create a game where the character moves and collects oranges."""

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Collection")
clock = pygame.time.Clock()
running = True

# character
char_w, char_h = 30, 40

# Initial character position
char_x, char_y = 256, 197

character = pygame.Rect((char_x, char_y), (char_w, char_h))

velocity = 5

# Food
def generate_food():
     return random.randint(5, 470), random.randint(5,340)

food_x, food_y = generate_food()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Show Coordinates
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#7efcf8")

    # RENDER YOUR GAME HERE

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        char_x -= velocity

    if keys[pygame.K_RIGHT]:
        char_x += velocity

    if keys[pygame.K_UP]:
        char_y -= velocity

    if keys[pygame.K_DOWN]:
        char_y += velocity

    # character
    pygame.draw.rect(screen, "red", character)

    # Update character position
    character = pygame.Rect((char_x, char_y), (char_w, char_h))

    # Food
    pygame.draw.circle(screen, "orange", (food_x, food_y), 10)

    # collision
    food_rect = pygame.Rect(food_x - 10, food_y - 10, 20, 20)  # 20x20 rectangle surrounding the food
    if character.colliderect(food_rect):
        food_x, food_y = generate_food()

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    pygame.display.update()

pygame.quit()
