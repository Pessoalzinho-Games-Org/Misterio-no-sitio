import pygame
pygame.init()

# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the background image and scale it to the screen size
background = pygame.image.load('test-bg.webp')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Load the player image, scale it down to 10px and place it in the center of the screen
player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (30, 30))
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


while True:
    # Get the state of the keyboard
    key = pygame.key.get_pressed()
    
    # Move the player based on the pressed keys
    if key[pygame.K_LEFT]:
        player_rect.x -= 1
    if key[pygame.K_RIGHT]:
        player_rect.x += 1
    if key[pygame.K_UP]:
        player_rect.y -= 1
    if key[pygame.K_DOWN]:
        player_rect.y += 1

    # Check for Exit event and quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the player
    screen.blit(player_image, player_rect)

    # Update the screen
    pygame.display.flip()