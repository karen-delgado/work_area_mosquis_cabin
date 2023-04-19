import pygame
import sys
import pygame_gui
from clases.level import Level # TODO que se reescriba para su uso
from clases.platform import Wall
from clases.platform import Hitbox
from clases.player import Player

pygame.init()

# FPS
FPS = 30
clock = pygame.time.Clock()

# Window
width = 768
height = 512
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Mosqui's Cabin")
# background_main_hub = pygame.image.load('mian_hub_ver1-0.png')

# genera instancia de player, se le envia a que nivel esta
# dentro de level se determinan las colisiones, player a su vez recibe eso para dejar de moverse


# Declare player
# TODO poner variables de posicion dependiendo de que nivel este para determinar el spaw

# hay una funcion que devolvera estos valores al main en los ciclos para cambiar la posicion del player dependiendo de donde este
# el default es fuera de la pantalla

player = Player() # por default el player hace spawn fuera de la pantalla
#x_speed = 1.5
#y_speed = 1.5

# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)

# Levels logic # TODO rehacer
# level = Level(player, wall_group, screen) # TODO solo hay 1 por ahora
# levels = [Level(player), Level(player)]
# current_level = 'main_hub'
# current_level_num = 0
# current_level = levels[current_level_no]
# player.level = level

game_levels = Level(player, screen)

# Game loop
running = True
#current_level_index = 1
level_is_over = False

campsite_is_over = False
outside_cabin_is_over = False

while running:
    campsite_is_over = game_levels.campsite()
    if campsite_is_over:
        outside_cabin_is_over = game_levels.outside_cabin()
        if outside_cabin_is_over:
            game_levels.main_hub()
        #if outside_cabin_is_over:
    clock.tick(FPS)

# TODO notas de switching entre niveles en el main
# minimo: current_level, current_level index
# levels viene siendo una lista [Level1, Level2] <- la lista oficial de todos los niveles que tiene la clase
# primer nivel 0: level, current_level = 0
# current_level.startgame() -> nivel donde estas
# current_level_index.startgame() -> referencia al nivel donde esta, una fx que cambie entre una cosa  y otra cuando
# se cumplen los objetivos
