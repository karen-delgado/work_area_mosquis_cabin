import pygame
from clases.platform import Platform
import random

# TODO hacer una clase base y una clase con cada cosa
# HERENCIA

class Level():
    def __init__(self, player, platform_group, screen):
        self.state = 'main_hub'
        self.background_main_hub = pygame.image.load('mian_hub_ver1-0.png')
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.platform_group = platform_group
        self.all_sprites.add(self.player)

    def main_hub(self, screen, platform_group, player):
        # handle events

        # TODO definir las colisiones aqui con platform group

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # screen.fill((0, 0, 0))
        # Background Image
        screen.blit(self.background_main_hub, (0, 0))

        # Player
        player.move(platform_group)
        player.update(platform_group)
        # TODO volver a prender
        # TODO buscar como hacer esto transparente
        # self.platform_group.draw(screen)
        self.all_sprites.draw(screen)

        # update the display
        pygame.display.update()
        pygame.display.flip()


