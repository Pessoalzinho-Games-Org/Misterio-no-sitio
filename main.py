import pygame
pygame.init()

# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the player
player = pygame.Rect((300, 250, 50, 50))

while True:
    # Get the state of the keyboard
    key = pygame.key.get_pressed()
    
    # Move the player based on the pressed keys
    if key[pygame.K_LEFT]:
        player.x -= 1
    if key[pygame.K_RIGHT]:
        player.x += 1
    if key[pygame.K_UP]:
        player.y -= 1
    if key[pygame.K_DOWN]:
        player.y += 1

    # Check for Exit event and quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 255, 255), player)

    # Update the screen
    pygame.display.flip()