import pygame, random

WIDTH = 1000
HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()


def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/nav2.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.speed_y = 0
		self.shield = 100

	def update(self):
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed() 
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
			self.image = pygame.image.load("assets/nav2fast.png").convert()
			self.image.set_colorkey(BLACK)
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
			self.image = pygame.image.load("assets/nav2fast.png").convert()
			self.image.set_colorkey(BLACK)
		if keystate[pygame.K_DOWN]:
			self.speed_y = 5 
			self.image = pygame.image.load("assets/nav2.png").convert()
			self.image.set_colorkey(BLACK)
		if keystate[pygame.K_UP]:
			self.speed_y = -5	 
			self.image = pygame.image.load("assets/nav2fast.png").convert()
			self.image.set_colorkey(BLACK)		 
		self.rect.x += self.speed_x	
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0: 
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT

	def shoot(self):  
			bullet = Bullet(self.rect.centerx, self.rect.top)
			all_sprites.add(bullet)
			bullets.add(bullet)

			#Agregamos sonido
			laser_sound.play()

class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(meteor_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx 
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)

			#Change this variable
			self.rect.y = random.randrange(-150, -100)
			self.speedy = random.randrange(1, 8)



class Navenemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/navene.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = -80
        self.speedx = random.randrange(-7, 9)
        self.speedy = 3
        self.direction = 1
        self.delay = random.randrange(200, 600)  # Retardo de aparición inicial
        self.timer = 0  # Temporizador para rastrear el tiempo transcurrido

    def update(self):
        self.timer += 1
        if self.timer >= self.delay:
            self.rect.x += self.speedx
            self.rect.y += self.speedy * self.direction

            if self.rect.top > HEIGHT + 10 or self.rect.bottom < -10:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = -80
                self.speedx = random.randrange(-7, 9)
                self.direction *= -1
                self.delay = random.randrange(200, 600)  # Retardo de aparición aleatorio
                self.timer = 0  # Reiniciar el temporizador
                
class Navenemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/navene2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-120, -100)
        self.speedx = random.randrange(-7, 9)
        self.speedy = 3
        self.direction = 1
        self.delay = random.randrange(200, 600)  # Retardo de aparición inicial
        self.timer = 0  # Temporizador para rastrear el tiempo transcurrido

    def update(self):
        self.timer += 1
        if self.timer >= self.delay:
            self.rect.x += self.speedx
            self.rect.y += self.speedy * self.direction

            if self.rect.top > HEIGHT + 10 or self.rect.bottom < -10:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = -80
                self.speedx = random.randrange(-7, 9)
                self.direction *= -1
                self.delay = random.randrange(200, 600)  # Retardo de aparición aleatorio
                self.timer = 0       
 

class Estrella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.estrellas_imagenes = []
        for img in estrellas_lista:
            self.estrellas_imagenes.append(pygame.image.load(img))
        self.image = random.choice(self.estrellas_imagenes)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-50, -2)
        self.fy = self.rect.y
        self.vel_y = self.rect.width / 10

    def update(self):
        self.fy += self.vel_y
        self.rect.y = self.fy

        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-50, -2)
            self.fy = self.rect.y

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/laser1.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # how long to wait for the next frame VELOCITY OF THE EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill() # if we get to the end of the animation we don't keep going.
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center


class Navelider(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/navelider.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-10, -4)
		self.speedy = 0
		self.speedx = 0

	def update(self):
		self.rect.x += self.speedx 
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-15, -10)
			self.speedy = random.randrange(1, 4)




def show_go_screen():
	screen.blit(background, [0, 0])
	draw_text(screen, "Muerte en el espacio", 65, WIDTH // 2, HEIGHT / 4)
	draw_text(screen, "1.Tienes una barra de salud de 4 impactos", 27, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "2.Los meteoros te dan 1 punto", 27, WIDTH // 2, HEIGHT // 2 + 50)
	draw_text(screen, "3.Las naves te dan 2 puntos", 27, WIDTH // 2, HEIGHT // 2 + 100)
	draw_text(screen, "Presiona una tecla para iniciar", 17, WIDTH // 2, HEIGHT * 3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False

meteor_images = []
meteor_list = [ "assets/meteorGrey_big3.png", 
				"assets/meteorGrey_med1.png", "assets/meteorGrey_med2.png", "assets/meteorGrey_small1.png", "assets/meteorGrey_small2.png"]
for img in meteor_list:
	meteor_images.append(pygame.image.load(img).convert())

## --------------- CARGAR IMAGENES EXPLOSIÓN -------------------------- ##
explosion_anim = []
for i in range(9):
	file = "assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70, 70))
	explosion_anim.append(img_scale)


# Cargar fondo.
background = pygame.image.load("assets/espafond.png").convert()
estrellas_lista = [
	"assets/estrella_imagen3x3.png","assets/estrella_imagen3x3.png","assets/estrella_imagen5x5.png","assets/estrella_imagen7x7.png",	
]

# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/laser5.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music.ogg")
pygame.mixer.music.set_volume(0.9)


pygame.mixer.music.play(loops=-1)

# Game Loop
game_over = True
running = True
while running:
	if game_over:
		show_go_screen()
		game_over = False
		all_sprites = pygame.sprite.Group()
		meteor_list = pygame.sprite.Group()
		addibujar_list = pygame.sprite.Group()
		navene_list= pygame.sprite.Group()
		navener_list= pygame.sprite.Group()	
		bullets = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)

		for i in range(8):
			meteor = Meteor()
			all_sprites.add(meteor)
			meteor_list.add(meteor)
   
		for n in range(9):
			nave = Navenemy()
			all_sprites.add(nave)
			navene_list.add(nave) 

		for j in range(6):
			nave1 = Navenemy1()
			all_sprites.add(nave1)
			navener_list.add(nave1)
    
 
		for img in estrellas_lista:
			estrella = Estrella()
			estrella.estrellas_imagenes.append(pygame.image.load(img))
			addibujar_list.add(estrella)

		#Marcador / Score
		score = 0
	# Keep loop running at the right speed
	clock.tick(60)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()
		

	# Update
	all_sprites.update()

	# Colisiones meteoro - laser
	hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
	for hit in hits:
		score += 1
		
		explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)

		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)

	hits1 = pygame.sprite.groupcollide(navene_list, bullets, True, True)
	for hit in hits1:
		score += 2
		explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)

		nave= Navenemy()
		all_sprites.add(nave)
		navene_list.add(nave)

	hits2 = pygame.sprite.groupcollide(navener_list, bullets, True, True)
	for hit in hits2:
		score += 2
		explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)

		nave1= Navenemy1()
		all_sprites.add(nave1)
		navener_list.add(nave1)
	
	"""
	if score >= 50:
		# Eliminar los meteoros y naves enemigas
		meteor_list.empty()
		navene_list.empty()
		navener_list.empty() 

		naveli = Navelider()
		all_sprites.add(naveli)
	"""
	
 
	# Colisiones jugador - meteoro
	hits = pygame.sprite.spritecollide(player, meteor_list, True) 
	for hit in hits:
		player.shield -= 25
		meteor = Meteor()
		all_sprites.add(meteor)
		meteor_list.add(meteor)
		if player.shield <= 0:
			#running = False
			game_over = True
	

	hits1 = pygame.sprite.spritecollide(player, navene_list, True)
	for hit in hits1:
		player.shield -= 25
		nave= Navenemy()
		all_sprites.add(nave)
		navene_list.add(nave)		
		if player.shield <= 0:
			#running = False 
			game_over = True
   
	hits2 = pygame.sprite.spritecollide(player, navener_list, True)
	for hit in hits2:
		player.shield -= 25
		nave1= Navenemy1()
		all_sprites.add(nave1)
		navener_list.add(nave1)		
		if player.shield <= 0:
			#running = False 
			game_over = True

	#Draw / Render
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)

	# Marcador
	draw_text(screen, str(score), 25, WIDTH // 2, 10)

	# ESCUDO.
	draw_shield_bar(screen, 5, 5, player.shield)


	pygame.display.flip()

pygame.quit()
