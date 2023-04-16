import pygame
import sys
import pygame_gui
from clases.player import Player

pygame.init()

#Background
background = pygame.image.load('mian_hub_ver1-0.png')

#FPS
FPS = 60

# Window
width = 768
height = 512
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Mosqui's Cabin")
clock = pygame.time.Clock()


#Game loop
while True:
    #RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    #Background Image
    screen.blit(background, (0, 0))

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # update the display
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
