import pygame

from clases.spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("01-generic_cropped.png").convert()
        # self.image.fill(color)
        self.image.set_colorkey((0, 0, 0))
        self.change_x = 3
        self.change_y = 3
        self.level = None
        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []
        self.rect = self.image.get_rect()
        self.wall_group = pygame.sprite.Group()
        self.level_x_pos = 768
        self.level_y_pos = 512
        # por default el player hace spawn fuera de la pantalla

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
        self.rect.topleft = [self.level_x_pos, self.level_y_pos]

        # Set spawn point

    def change_spawn_point(self, new_x, new_y):
        self.level_x_pos = new_x
        self.level_y_pos = new_y
        self.rect.topleft = [self.level_x_pos, self.level_y_pos]

    def change_wall_group(self, collision_sprite_array):
        self.wall_group = collision_sprite_array

    def move(self):
        # TODO trabajar con las colisiones
        # where_col = self.update()
        where_col = 'nan'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and where_col != 'l':
            self.rect.x -= self.change_x
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        else:
            pygame.event.set_blocked(pygame.KEYDOWN)
        if keys[pygame.K_RIGHT] and where_col != 'r':
            self.rect.x += self.change_x
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            pygame.event.set_blocked(pygame.KEYDOWN)
        if keys[pygame.K_UP] and where_col != 'u':
            self.rect.y -= self.change_y
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        else:
            pygame.event.set_blocked(pygame.KEYDOWN)
        if keys[pygame.K_DOWN] and where_col != 'd':
            self.rect.y += self.change_y
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]
        else:
            pygame.event.set_blocked(pygame.KEYDOWN)
        if where_col == 'nan':
            pass

    def update(self):
        stat = 'nan'
        for wall in self.wall_group:
            if pygame.sprite.collide_rect(self, wall):
                if self.change_x > 0:
                    self.rect.right = wall.rect.left
                    self.change_x = 0
                    stat = 'r'
                if self.change_x < 0:
                    self.rect.left = wall.rect.right
                    self.change_x = 0
                    stat = 'l'
                if self.change_y < 0:
                    self.rect.bottom = wall.rect.top
                    self.change_y = 0
                    stat = 'u'
                if self.change_y > 0:
                    self.rect.top = wall.rect.bottom
                    self.change_y = 0
                    stat = 'b'
        return stat


        # self.rect.y = self.rect.y + self.change_y
        # self.rect.x += self.change_x


    # TODO implementar esto when walking in sludge      self.change_x = 0+1
