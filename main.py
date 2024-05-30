import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

while True:

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.x -= 1
    if key[pygame.K_RIGHT]:
        player.x += 1
    if key[pygame.K_UP]:
        player.y -= 1
    if key[pygame.K_DOWN]:
        player.y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.flip()