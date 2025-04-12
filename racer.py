import pygame
import time
import random
pygame.init()  

WIDTH = 400
HEIGHT = 600
RED = (255, 0, 0) 
PLAYER_SPEED = 10
ENEMY_SPEED = 10 

crash_sound = pygame.mixer.Sound("resources/crash.wav")
coin_sound = pygame.mixer.Sound("resources/coin.mp3")
background_music = pygame.mixer.music.load('resources/background.wav') 

background = pygame.image.load("resources/AnimatedStreet.png") 
font1 = pygame.font.SysFont("Verdana", 60)
game_over = font1.render("Game Over", True, "black") 

pygame.mixer.music.play(-1) 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

clock = pygame.time.Clock()
FPS = 60

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.w, WIDTH - self.rect.w), 0) 

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(self.rect.w, WIDTH - self.rect.w), 0) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.w // 2
        self.rect.y = HEIGHT - self.rect.h 

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH 

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-100, -40) 

    def respawn(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.w)
        self.rect.y = random.randint(-100, -40) 
    def move(self):
        self.rect.move_ip(0, 5) 
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.w)
            self.rect.y = random.randint(-100, -40)
            

enemy = Enemy() 
coin=Coin()
player=Player()
coins = pygame.sprite.Group()
coins.add(coin)
enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin) 
collected_coins = 0
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    
    for entity in all_sprites:
        entity.move() 

    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        screen.fill(RED)
        center_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, center_rect)
        pygame.display.flip()
        time.sleep(2)  
        running = False 
    
    if pygame.sprite.spritecollideany(player,  coins): 
        coin_sound.play() 
        collected_coins+=1 
        coin.respawn() 
    
    screen.blit(background, (0, 0))  
    font2 = pygame.font.SysFont("Verdana", 30)
    coin_text = font2.render(f"Coins: {collected_coins}", True, "black")
    screen.blit(coin_text, (WIDTH - 150, 20)) 

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)  

  
    pygame.display.flip() 

    clock.tick(FPS) 
pygame.quit()  
