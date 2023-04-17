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



# Platforms TODO store this better, dear god
platform_group = pygame.sprite.Group()
platform1 = Platform(93, 110, 260, 50)
platform_group.add(platform1)
platform2 = Platform(415, 110, 130, 50)
platform_group.add(platform2)
platform3 = Platform(605, 110, 133, 50)
platform_group.add(platform3)
platform4 = Platform(545, 110, 60, 75)
platform_group.add(platform4)
platform5 = Platform(708, 110, 60, 160)
platform_group.add(platform5)
platform6 = Platform(35, 110, 60, 165)
platform_group.add(platform6)
platform7 = Platform(35, 365, 27, 75)
platform_group.add(platform7)
platform8 = Platform(577, 360, 150, 80)
platform_group.add(platform8)
platform9 = Platform(30, 450, 320, 80)
platform_group.add(platform9)
platform10 = Platform(450, 450, 290, 80)
platform_group.add(platform10)
platform11 = Platform(160, 185, 65, 50)
platform_group.add(platform11)
platform12 = Platform(190, 185, 65, 25)
platform_group.add(platform12)
platform13 = Platform(200, 185, 15, 75)
platform_group.add(platform13)
platform14 = Platform(700, 360, 100, 150)
platform_group.add(platform14)

# Declare player
player = Player(width, height, platform_group)
x_speed = 2
y_speed = 2

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
