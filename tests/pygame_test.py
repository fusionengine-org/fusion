import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
