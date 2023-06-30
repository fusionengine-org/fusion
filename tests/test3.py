import pygame
 
pygame.init()
 
window = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Example: 1')
 
image = pygame.image.load("test.png").convert()
 
window.blit(image, (100, 100))
 
pygame.display.flip()

running = True

while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

