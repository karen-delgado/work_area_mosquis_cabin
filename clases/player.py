import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
from clases.spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, screenW, screenH, wall_group):
        super().__init__()
        self.image = pygame.image.load("01-generic_cropped.png").convert()
        # self.image.fill(color)
        self.screenW = screenW
        self.screenH = screenH
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.change_x = 3
        self.change_y = 3
        self.level = None
        self.wall_group = wall_group
        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []

        # What direction is the player facing?
        self.direction = "D"

        sprite_sheet = SpriteSheet("01-generic_cropped.png")

        # TODO player llamará de level detect collisions en general
        # TODO player llamara de level detect collisions - lado

        # DOWN
        # TODO: LATER arreglar un clipping que tiene en la chola en la posicion neutral
        # Load all the down facing images into a list
        # x, y, width and height
        image = sprite_sheet.get_image(0, 0, 12, 15)
        image = pygame.transform.scale(image, (12 * 3, 15 * 3))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(16, 0, 13, 15)
        image = pygame.transform.scale(image, (13 * 3, 15 * 3))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(33, 0, 12, 15)
        image = pygame.transform.scale(image, (12 * 3, 15 * 3))
        self.walking_frames_d.append(image)
        # repetido a la segunda, es para que los brazos vuelvan neutrales
        image = sprite_sheet.get_image(16, 0, 13, 15)
        image = pygame.transform.scale(image, (13 * 3, 15 * 3))
        self.walking_frames_d.append(image)

        # LEFT
        image = sprite_sheet.get_image(1, 16, 10, 15)
        image = pygame.transform.scale(image, (10 * 3, 15 * 3))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(17, 15, 10, 16)
        image = pygame.transform.scale(image, (10 * 3, 16 * 3))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(33, 16, 12, 15)
        image = pygame.transform.scale(image, (12 * 3, 15 * 3))
        self.walking_frames_l.append(image)
        # repetido a la segunda, es para que los brazos vuelvan neutrales
        image = sprite_sheet.get_image(17, 15, 10, 15)
        image = pygame.transform.scale(image, (10 * 3, 15 * 3))
        self.walking_frames_l.append(image)

        # RIGHT
        image = sprite_sheet.get_image(1, 32, 10, 15)
        image = pygame.transform.scale(image, (10 * 3, 15 * 3))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(17, 31, 10, 16)
        image = pygame.transform.scale(image, (10 * 3, 16 * 3))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(33, 32, 10, 15)
        image = pygame.transform.scale(image, (10 * 3, 15 * 3))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(17, 31, 10, 16)
        image = pygame.transform.scale(image, (10 * 3, 16 * 3))
        self.walking_frames_r.append(image)

        # UP
        image = sprite_sheet.get_image(1, 48, 12, 15)
        image = pygame.transform.scale(image, (12 * 3, 15 * 3))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(16, 47, 13, 17)
        image = pygame.transform.scale(image, (13 * 3, 17 * 3))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(32, 48, 12, 15)
        image = pygame.transform.scale(image, (12 * 3, 15 * 3))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(16, 47, 13, 17)
        image = pygame.transform.scale(image, (13 * 3, 17 * 3))
        self.walking_frames_u.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_u[1]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.topleft = [screenW, screenH]

        # Set spawn point

    def move(self, wall_group):
        self.update(wall_group)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.change_x
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.change_x
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        if keys[pygame.K_UP]:
            self.rect.y -= self.change_y
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        if keys[pygame.K_DOWN]:
            self.rect.y += self.change_y
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]

    def check_wall_collision(self, wall_group):

        # See if we hit anything
        wall_hit_list = pygame.sprite.spritecollide(self, self.wall_group, False)
        keys = pygame.key.get_pressed()
        # TODO verificar esto
        for wall in wall_hit_list:
            if self.rect.left >= wall.rect.right:
                if keys[pygame.K_LEFT]:
                    pygame.event.set_blocked(KEYDOWN)

            #if self.change_x > 0:
            #elif self.change_x < 0:
               # self.change_x = 0

            #if self.change_y > 0:
               # self.change_y = 0
            #elif self.change_y < 0:
                #self.change_y = 0


    # TODO implementar esto when walking in sludge      self.change_x = 0+1
