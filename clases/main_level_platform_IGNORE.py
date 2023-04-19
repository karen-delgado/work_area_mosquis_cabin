
# VERSION MODDED KAREN
wall_group = pygame.sprite.Group()
# LIMITES DE LOS LADOS
# Caja grande para la cocina top
wall1 = Wall(354, 120, 0, 0)
wall_group.add(wall1)
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

# OBJETOS INTERACTUABLES
hitbox_group = pygame.sprite.Group()

# OBJETOS POSIBLEMENTE INTERACTUABLES CON COLISION ESTRICTA
# Mesita esquina abajo
buffet_bottom_left = Wall(32, 82, 32, 364)
wall_group.add(buffet_bottom_left)
buffet_bottom_left_inter = Hitbox(32, 82, 32+32, 364)
hitbox_group.add(buffet_bottom_left_inter)

# Cama jodia
janky_bed = Wall(108, 80, 618, 352)
wall_group.add(janky_bed)
hitbox_group.add(janky_bed)

# Ropero al fin de la cama
nightstand = Wall(40, 82, 574, 360)
wall_group.add(nightstand)
hitbox_group.add(nightstand)

# Tablillas a la izq, decouple de los bordes?

# Fireplace
fireplace = Wall(60, 116, 548, 42)
wall_group.add(fireplace)
hitbox_group.add(fireplace)

# Mesa
tabletop = Wall(62, 44, 160, 182)
wall_group.add(tabletop)
hitbox_group.add(tabletop)

# Silla abajo
bottom_chair = Wall(20, 28, 198, 226)
wall_group.add(bottom_chair)
hitbox_group.add(bottom_chair)

# Silla derecha
right_chair = Wall(26, 24, 226, 184)
wall_group.add(right_chair)
hitbox_group.add(right_chair)

# Bucket arriba derecha
crab_bucket = Wall(28, 58, 674, 100)
wall_group.add(crab_bucket)
hitbox_group.add(crab_bucket)

# OBJETOS CON HITBOXES

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
