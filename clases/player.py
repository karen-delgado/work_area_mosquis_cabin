import pygame
from clases.spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, screenW, screenH, platform_group):
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
        self.platform_group = platform_group
        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []

        # What direction is the player facing?
        self.direction = "D"

        sprite_sheet = SpriteSheet("01-generic_cropped.png")

        # DOWN
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
        self.image = self.walking_frames_d[1]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def move(self, platform_group):
        self.update(platform_group)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.change_x
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_l)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.change_x
            pos = self.rect.x
            frame = (pos // 30) % len(self.walking_frames_r)
        if keys[pygame.K_UP]:
            self.rect.y -= self.change_y
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_u)
        if keys[pygame.K_DOWN]:
            self.rect.y += self.change_y
            pos = self.rect.y
            frame = (pos // 30) % len(self.walking_frames_d)


    def update(self, platform_group):
        """ Move the player. """

        if self.change_x > 0:
            self.direction = "R"
        elif self.change_x < 0:
            self.direction = "L"
        if self.change_y > 0:  # moving down
            self.direction = "D"
        elif self.change_y < 0:  # moving up
            self.direction = "U"

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, platform_group, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

            if self.change_y > 0: # moving down
                self.rect.bottom = block.rect.top
            elif self.change_y < 0: # moving up
                self.rect_top = block.rect_bottom


        # Move up/down
        # TODO - is this necessary?
        # self.rect.y += self.change_y


        # Check and see if we hit anything
        # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
          #   if self.change_y > 0:
            #    self.rect.bottom = block.rect.top
            #elif self.change_y < 0:
             #   self.rect.top = block.rect.bottom

            # Stop our vertical movement
            # self.change_y = 0
