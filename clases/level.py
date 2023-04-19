import pygame
from clases.platform import Wall
import random

# TODO hacer una clase base y una clase con cada cosa
# HERENCIA

# class GameState(): posible para añadir pausa y
  #   def __init__(self):
     #    self.state = 'active'

class Level:
    def __init__(self, player, screen):
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.background = pygame.image.load('mian_hub_ver1-0.png')


class Initial_Hub(Level):
    pass
    # LIMITES DE LOS LADOS
    # Caja grande para la cocina top
    def __init__(self):
        Level.__init__(self, player, screen)
    def set_walls(self):
        wall1 = Wall(354, 120, 0, 0)
        self.wall_group.add(wall1)
        # Caja grande para la cocina al lado izq
        wall2 = Wall(96, 240, 0, 0)
        wall_group.add(wall2)
        # Caja grande para la sala derecha top
        wall3 = Wall(354, 120, 414, 0)
        wall_group.add(wall3)
        # Borde pantalla izquierda
        wall4 = Wall(35, 295, 0, 0)
        wall_group.add(wall4)
        # Borde pantalla derecha arriba + tablilleros
        wall5 = Wall(62, 242, 706, 0)
        wall_group.add(wall5)
        # Borde patalla derecha abajo
        wall6 = Wall(60, 180, 704, 332)
        wall_group.add(wall6)
        # Esquina abajo derecha
        wall7 = Wall(320, 64, 448, 448)
        wall_group.add(wall7)
        # Esquina abajo izq
        wall8 = Wall(350, 62, 0, 448)
        wall_group.add(wall8)
        # Esquina izq abajo
        wall9 = Wall(32, 130, 0, 382)
        wall_group.add(wall9)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()

        # screen.fill((0, 0, 0))
        # Background Image
        screen.blit(self.background_main_hub, (0, 0))

        # Player
        player.move(wall_group)
        player.update(wall_group)
        # TODO volver a prender
        # TODO buscar como hacer esto transparente
        # self.wall_group.draw(screen)
        self.all_sprites.draw(screen)

        # update the display
        pygame.display.update()
        pygame.display.flip()


