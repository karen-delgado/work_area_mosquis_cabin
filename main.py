import pygame
import sys
import pygame_gui
from clases.level import Level
from clases.player import Player
from clases.platform import Platform

pygame.init()

# FPS
FPS = 30
clock = pygame.time.Clock()

# Window
width = 768
height = 512
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Mosqui's Cabin")

# genera instancia de player, se le envia a que nivel esta
# dentro de level se determinan las colisiones, player a su vez recibe eso para dejar de moverse


# Platforms TODO store this better, dear god
platform_group = pygame.sprite.Group()

# VERSION MODDED KAREN

# LIMITES DE LOS LADOS
# Caja grande para la cocina top
platform1 = Platform(354, 120, 0, 0)
platform_group.add(platform1)
# Caja grande para la cocina al lado izq
platform2 = Platform(96, 240, 0, 0)
platform_group.add(platform2)
# Caja grande para la sala derecha top
platform3 = Platform(354, 120, 414, 0)
platform_group.add(platform3)
# Borde pantalla izquierda
platform4 = Platform(35, 295, 0, 0)
platform_group.add(platform4)
# Borde pantalla derecha arriba + tablilleros
platform5 = Platform(62, 242, 706, 0)
platform_group.add(platform5)
# Borde patalla derecha abajo
platform6 = Platform(60, 180, 704, 332)
platform_group.add(platform6)
# Esquina abajo derecha
platform7 = Platform(320, 64, 448, 448)
platform_group.add(platform7)
# Esquina abajo izq
platform8 = Platform(350, 62, 0, 448)
platform_group.add(platform8)
# Esquina izq abajo
platform9 = Platform(32, 130, 0, 382)
platform_group.add(platform9)


# OBJETOS POSIBLEMENTE INTERACTUABLES CON COLISION

# Mesita esquina abajo
buffet_bottom_left = Platform(32, 82, 32, 364)
platform_group.add(buffet_bottom_left)

# Cama jodia
janky_bed = Platform(108, 80, 618, 352)
platform_group.add(janky_bed)

# Ropero al fin de la cama
nightstand = Platform(40, 82, 574, 360)
platform_group.add(nightstand)

# Tablillas a la izq, decouple de los bordes?

# Fireplace
fireplace = Platform(60, 116, 548, 42)
platform_group.add(fireplace)

# Mesa
tabletop = Platform(62, 44, 160, 182)
platform_group.add(tabletop)

# Silla abajo
bottom_chair = Platform(20, 28, 198, 226)
platform_group.add(bottom_chair)

# Silla derecha
right_chair = Platform(26, 24, 226, 184)
platform_group.add(right_chair)

# Bucket arriba derecha
crab_bucket = Platform(28, 58, 674, 100)
platform_group.add(crab_bucket)

# OBJETOS SIN COLISIONES ESTRICTAS

# Kitchenware
# Mesa
# Barriles
# Bookshelf 1 (alto)
# Bookshelf 2 (bajito)
# Fireplace
# Logs
# Bucket
# SLEEPING PAD
# Janky bed
# Nightstand
# Buffet
# Trapdoor
# Bookshelf de al lado

# Salida oeste
# Salida norte
# Salida este
# Salida sur


# Declare player
# TODO poner variables de posicion dependiendo de que nivel este para determinar el spawn
player = Player(300, 200, platform_group)
x_speed = 1.5
y_speed = 1.5

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Levels logic
level = Level(player, platform_group, screen) # TODO solo hay 1 por ahora
# levels = [Level(player), Level(player)]
current_level = 'main_hub'
# current_level_num = 0
# current_level = levels[current_level_no]
player.level = level

# Game loop
while True:
    level.main_hub(screen, platform_group, player)
    # level.player.move(platform_group)
    # level.draw(screen, platform_group)
    clock.tick(FPS)

# TODO notas de switching entre niveles en el main
# minimo: current_level, current_level index
# levels viene siendo una lista [Level1, Level2] <- la lista oficial de todos los niveles que tiene la clase
# primer nivel 0: level, current_level = 0
# current_level.startgame() -> nivel donde estas
# current_level_index.startgame() -> referencia al nivel donde esta, una fx que cambie entre una cosa  y otra cuando
# se cumplen los objetivos
