import pygame
from clases.platform import Wall
from clases.platform import Hitbox
# import random

# TODO hacer una clase base y una clase con cada cosa
# HERENCIA

# class GameState(): posible para añadir pausa y
  #   def __init__(self):
     #    self.state = 'active'

class Level:
    def __init__(self, player, screen):
        self.background = pygame.image.load('mian_hub_ver1-0.png')
        self.screen = screen
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.wall_group = pygame.sprite.Group()
        self.hitbox_group = pygame.sprite.Group()
        self.exit_level_hitbox = pygame.sprite.Group()

        self.did_campsite_initiate = False
        self.did_outside_cabin_initiate = False
        self.did_main_hub_initiate = False


    def start_screen(self):
        # Definir cosas básicas del juego
        self.background = pygame.image.load('title_screen_with_title.png')
        # TODO IAN programar los botones aqui
        # Game loop
        # Dentro del game loop:
        level_progress_conditions_are_met = False
        while level_progress_conditions_are_met != True:
            if self.level_progress_conditions_are_met:
                return True

    def initiate_campsite(self):
        # Definir cosas básicas del juego
        self.background = pygame.image.load('outside_camping.png')
        self.wall_group.empty()
        current_wall = Wall(768, 360, 0, 0)
        self.wall_group.add(current_wall)
        current_wall = Wall(472, 188, 296, 324)
        self.wall_group.add(current_wall)
        self.player.change_spawn_point(200, 420)
        self.did_campsite_initiate = True
        self.exit_level_hitbox.empty()
        current_hitbox = Hitbox(60, 188, 0, 324)
        current_hitbox.change_color(0, 255, 0)
        self.exit_level_hitbox.add(current_hitbox)

    def campsite(self):
        if self.did_campsite_initiate == False:
            self.initiate_campsite()
        else:
            # Game loop
            level_progress_conditions_are_met = False
            for event in pygame.event.get():  # entro a evento, pido que lo reciba. event es un objeto
                if event.type == pygame.KEYDOWN:  # si undio cualquier tipo de tecla:
                    if event.key == pygame.K_ESCAPE:  # solo acepta
                        exit()
                elif event.type == pygame.QUIT:  # x de la pantalla
                    exit()

            # Background Image
            self.screen.blit(self.background, (0, 0))
            # Player
            self.player.move()
            # TODO apagar esto luego de funcionalidad
            #self.wall_group.draw(self.screen)
            #self.exit_level_hitbox.draw(self.screen)
            # self.hitbox_group.draw(screen) #N/A en este nivel todavia
            self.all_sprites.draw(self.screen)

            # update the display
            pygame.display.flip()

            exit_level_hit_list = pygame.sprite.spritecollide(self.player, self.exit_level_hitbox, False)
            for exit in exit_level_hit_list:
                level_progress_conditions_are_met = True
            # TODO volver a incorporar verificador de que el nivel termino
            # Dentro del game loop:
            if level_progress_conditions_are_met:
                return True

    def initiate_outside_cabin(self):
        # Definir cosas básicas del juego
        self.background = pygame.image.load('outside.png')
        self.wall_group.empty()
        current_wall = Wall(762, 360, 0, 0)
        self.wall_group.add(current_wall)
        current_wall = Wall(12, 75, 148, 332)
        self.wall_group.add(current_wall)
        current_wall = Wall(12, 75, 225, 332)
        self.wall_group.add(current_wall)
        self.player.change_spawn_point(702, 420)
        self.did_outside_cabin_initiate = True
        self.exit_level_hitbox.empty()
        current_hitbox = Hitbox(58, 24, 162, 344)
        current_hitbox.change_color(0, 255, 0)
        self.exit_level_hitbox.add(current_hitbox)

    def outside_cabin(self):
        if self.did_outside_cabin_initiate == False:
            self.initiate_outside_cabin()
        else:
            # Game loop
            level_progress_conditions_are_met = False
            for event in pygame.event.get():  # entro a evento, pido que lo reciba. event es un objeto
                if event.type == pygame.KEYDOWN:  # si undio cualquier tipo de tecla:
                    if event.key == pygame.K_ESCAPE:  # solo acepta
                        exit()
                elif event.type == pygame.QUIT:  # x de la pantalla
                    exit()

            # Background Image
            self.screen.blit(self.background, (0, 0))
            # Player
            self.player.move()
            # TODO apagar esto luego de funcionalidad
            #self.wall_group.draw(self.screen)
            #self.exit_level_hitbox.draw(self.screen)
            # self.hitbox_group.draw(screen) #N/A en este nivel todavia
            self.all_sprites.draw(self.screen)

            # update the display
            pygame.display.flip()

            exit_level_hit_list = pygame.sprite.spritecollide(self.player, self.exit_level_hitbox, False)
            for exit in exit_level_hit_list:
                level_progress_conditions_are_met = True
            # TODO volver a incorporar verificador de que el nivel termino
            # Dentro del game loop:
            if level_progress_conditions_are_met:
                return True

    def initiate_main_hub(self):
        # Definir cosas básicas del juego
        self.background = pygame.image.load('mian_hub_ver1-0.png')
        self.wall_group.empty()
        self.exit_level_hitbox.empty()
        self.hitbox_group.empty()
        # TODO PLACEHOLDER, es para que corra el programa
        current_hitbox = Hitbox(1, 1, 1, 1)
        current_hitbox.change_color(0, 255, 0)
        self.exit_level_hitbox.add(current_hitbox)

        # LIMITES DE LOS LADOS
        # Caja grande para la cocina top
        wall1 = Wall(354, 120, 0, 0)
        self.wall_group.add(wall1)
        # Caja grande para la cocina al lado izq
        wall2 = Wall(96, 240, 0, 0)
        self.wall_group.add(wall2)
        # Caja grande para la sala derecha top
        wall3 = Wall(354, 120, 414, 0)
        self.wall_group.add(wall3)
        # Borde pantalla izquierda
        wall4 = Wall(35, 295, 0, 0)
        self.wall_group.add(wall4)
        # Borde pantalla derecha arriba + tablilleros
        wall5 = Wall(62, 242, 706, 0)
        self.wall_group.add(wall5)
        # Borde patalla derecha abajo
        wall6 = Wall(60, 180, 704, 332)
        self.wall_group.add(wall6)
        # Esquina abajo derecha
        wall7 = Wall(320, 64, 448, 448)
        self.wall_group.add(wall7)
        # Esquina abajo izq
        wall8 = Wall(350, 62, 0, 448)
        self.wall_group.add(wall8)
        # Esquina izq abajo
        wall9 = Wall(32, 130, 0, 382)
        self.wall_group.add(wall9)

        # OBJETOS POSIBLEMENTE INTERACTUABLES CON COLISION ESTRICTA
        # Mesita esquina abajo
        buffet_bottom_left = Wall(32, 82, 32, 364)
        self.wall_group.add(buffet_bottom_left)
        buffet_bottom_left_inter = Hitbox(24, 59, 64, 369)
        self.hitbox_group.add(buffet_bottom_left_inter)

        # Cama jodia
        janky_bed = Wall(108, 80, 618, 352)
        self.wall_group.add(janky_bed)
        janky_bed_inter = Hitbox(98, 25, 620, 335)
        self.hitbox_group.add(janky_bed_inter)

        # Ropero al fin de la cama
        nightstand = Wall(40, 82, 574, 360)
        self.wall_group.add(nightstand)
        nightstand_inter = Hitbox(23, 55, 550, 371)
        self.hitbox_group.add(nightstand_inter)

        # Tablillas a la izq, decouple de los bordes?

        # Fireplace
        fireplace = Wall(60, 116, 548, 42)
        self.wall_group.add(fireplace)
        fireplace_inter = Hitbox(58, 49, 548, 158)
        self.hitbox_group.add(fireplace_inter)

        # Mesa
        tabletop = Wall(62, 44, 160, 182)
        self.wall_group.add(tabletop)
        tabletop_inter = Hitbox(90, 82, 133, 184)
        self.hitbox_group.add(tabletop_inter)

        # test
        testbox = Hitbox(152, 113, 322, 276)
        testbox.change_color(255, 0, 0)
        self.hitbox_group.add(testbox)

        # Silla abajo
        bottom_chair = Wall(20, 28, 198, 226)
        self.wall_group.add(bottom_chair)
        #hitbox_group.add(bottom_chair)

        # Silla derecha
        right_chair = Wall(26, 24, 226, 184)
        self.wall_group.add(right_chair)
        #hitbox_group.add(right_chair)

        # Bucket arriba derecha
        crab_bucket = Wall(28, 58, 674, 100)
        self.wall_group.add(crab_bucket)
        #self.hitbox_group.add(crab_bucket)

        self.player.change_spawn_point(385, 486)
        self.did_outside_cabin_initiate = True

    def main_hub(self):
        if self.did_main_hub_initiate == False:
            self.initiate_main_hub()
        else:
            # Game loop
            level_progress_conditions_are_met = False
            for event in pygame.event.get():  # entro a evento, pido que lo reciba. event es un objeto
                if event.type == pygame.KEYDOWN:  # si undio cualquier tipo de tecla:
                    if event.key == pygame.K_ESCAPE:  # solo acepta
                        exit()
                elif event.type == pygame.QUIT:  # x de la pantalla
                    exit()

            # Background Image
            self.screen.blit(self.background, (0, 0))
            # Player
            self.player.move()
            # TODO apagar esto luego de funcionalidad
            self.wall_group.draw(self.screen)
            self.hitbox_group.draw(self.screen)
            self.exit_level_hitbox.draw(self.screen)
            self.all_sprites.draw(self.screen)

            # update the display
            pygame.display.flip()

            exit_level_hit_list = pygame.sprite.spritecollide(self.player, self.exit_level_hitbox, False)
            for exit in exit_level_hit_list:
                level_progress_conditions_are_met = True
            # TODO volver a incorporar verificador de que el nivel termino
            # Dentro del game loop:
            if level_progress_conditions_are_met:
                return True


    # TODO podria estar trayendo problemas, redefinir en algun momneto
    # def level_switcher(self, current_level_index):
      #  level_is_over = False
      #  if current_level_index == 0:
       #     level_is_over = self.start_screen(current_level_index)
        #    if level_is_over:
         #        return current_level_index + 1
        #if current_level_index == 1:
           # level_is_over = self.campsite(current_level_index)
           # if level_is_over:
             #   return (current_level_index + 1)


