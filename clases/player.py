import pygame

class Player(pygame.sprite.Sprite):
    def _init_(self, screenW, screenH):
        super()._init_()
        self.image = pygame.image.load("01-generic_cropped.png").convert()
        # self.image.fill(color)
        self.screenW = screenW
        self.screenH = screenH
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.change_x = 3
        self.change_y = 3
        self.level = None

    def move(self):
        self.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.change_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.change_x
        if keys[pygame.K_UP]:
            self.rect.y -= self.change_y
        if keys[pygame.K_DOWN]:
            self.rect.y += self.change_y
        if keys[pygame.K_SPACE]:
            self.jump()

    def update(self):
        """ Move the player. """


        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
