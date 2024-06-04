import pygame
import time
import utils
import random

# Spill med karakterer som skyter partikler og faar poeng for hvert skutt partikkel
# bruk vektorer
# bruk objektorientert programmering
# bruk kollisjoner

pygame.init()

# colors
colorDict = {
    "B": (0, 0, 0),
    "background": (0, 0, 0),
    "text": (255, 255, 255),
    "white": (255, 255, 255)
}


# screen and sizes initialization
class GameScreen:
    def __init__(self, width, height):
        # Vector
        self.resolution = pygame.math.Vector2(width, height)
        self.screen = pygame.display.set_mode(self.resolution)
        self.half_res = self.resolution // 2
        self.x_half = self.resolution.x // 2
        self.y_half = self.resolution.y // 2

width = 800
height = 600
game_screen = GameScreen(width, height)

# text
title_font = pygame.font.Font(None, 36)
sub_title_font = pygame.font.Font(None, 36)

textDict = {
    "welcome": title_font.render("Choose your level", True, colorDict["text"]),
    "hard": sub_title_font.render("hard", True, colorDict["text"]),
    "medium": sub_title_font.render("medium", True, colorDict["text"]),
    "easy": sub_title_font.render("easy", True, colorDict["text"]),
    "end": sub_title_font.render("The game is over", True, colorDict["text"])
}

welcome_position = (game_screen.x_half - textDict["welcome"].get_width() // 2, game_screen.y_half - 200)
easy_position = (game_screen.x_half - textDict["easy"].get_width() // 2, game_screen.y_half - 100)
medium_position = (game_screen.x_half - textDict["medium"].get_width() // 2, game_screen.y_half)
hard_position = (game_screen.x_half - textDict["hard"].get_width() // 2, game_screen.y_half + 100)

# visible objects, characters, initialization of them
all_sprites = pygame.sprite.Group()
all_particles = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, size, color, pos, speed):
        super().__init__()
        self.image = pygame.Surface([size.x, size.y])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = pos.x
        self.rect.y = pos.y
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -bullet_size.y:
            all_sprites.remove(self)


bullet_width = 15
bullet_height = 40
bullet_size = pygame.Vector2(bullet_width, bullet_height)
bullet_color = colorDict["white"]
bullet_speed = 5

class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, size, color):
        super().__init__()
        self.image = pygame.Surface([size.x, size.y])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (game_screen.x_half, game_screen.y_half)
        self.speed = 5
        self.time_last_shot = time.time()
    def draw(self):
        pygame.draw.rect(game_screen.screen, colorDict["B"], self.character)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE]:
            print(bullet_ideal_time_between_shot)
            if time.time() - self.time_last_shot > bullet_ideal_time_between_shot:
                character_pos = pygame.Vector2(self.rect.x, self.rect.y)
                # Shoot the bullet from the center of the character
                bullet_origin_pos = pygame.Vector2(character_pos.x + bullet_width + 2, character_pos.y)
                bullet = Bullet(bullet_size, bullet_color, bullet_origin_pos, bullet_speed)
                all_sprites.add(bullet)
                all_bullets.add(bullet)
                self.time_last_shot = time.time()

        # Keep the sprite on the screen
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0


character_width = 50
character_height = 50
character_size = pygame.Vector2(character_width, character_height)
character_color = colorDict["white"]
bullet_ideal_time_between_shot = 0.5
main_character = MainCharacter(character_size, character_color)
all_sprites.add(main_character)

class Particle(pygame.sprite.Sprite):
    def __init__(self, size, color, speed, x):
        super().__init__()
        self.image = pygame.Surface([size.x, size.y])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > height:
            all_sprites.remove(self)
        for bullet in all_bullets:
            collided_particles = pygame.sprite.spritecollide(bullet, all_particles, True)
            if collided_particles:
                bullet.kill()
                self.kill()
        collided_character = pygame.sprite.spritecollide(main_character, all_particles, True)
        if collided_character:
            main_character.kill()
            self.kill()
            return True

particle_height = 25
particle_width = 25
particle_size = pygame.Vector2(particle_height, particle_width)
particle_color = colorDict["white"]
particle_speed = 8

# start
game_screen.screen.blit(textDict["welcome"], welcome_position)
game_screen.screen.blit(textDict["easy"], easy_position)
game_screen.screen.blit(textDict["medium"], medium_position)
game_screen.screen.blit(textDict["hard"], hard_position)

pygame.display.flip()

# game not running
game_mode_chosen = False
game_mode = ""
while game_mode_chosen == False:
    e = pygame.event.get()
    for event in e:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if textDict["easy"].get_rect(topleft=easy_position).collidepoint(pos):
                print("Easy mode chosen")
                game_mode = "easy"
                game_mode_chosen = True
                utils.clearScreenText(game_screen.screen, colorDict["background"], all_sprites)
            elif textDict["medium"].get_rect(topleft=medium_position).collidepoint(pos):
                print("Medium mode chosen")
                game_mode = "medium"
                game_mode_chosen = True
                utils.clearScreenText(game_screen.screen, colorDict["background"], all_sprites)
            elif textDict["hard"].get_rect(topleft=hard_position).collidepoint(pos):
                print("Hard mode chosen")
                game_mode = "hard"
                game_mode_chosen = True
                utils.clearScreenText(game_screen.screen, colorDict["background"], all_sprites)

# game running / initialization
game_screen.screen.fill(colorDict["background"])
all_sprites.update()
all_sprites.draw(game_screen.screen)
pygame.display.flip()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # rendering particles
    particle_x_start = random.randint(0, width)
    particle = Particle(particle_size, particle_color, particle_speed, particle_x_start)
    utils.renderParticle(particle, game_mode, all_sprites, all_particles)
    
    game_screen.screen.fill(colorDict["background"])
    all_sprites.draw(game_screen.screen)
    for sprite in all_sprites:
        end = sprite.update()
        if end:
            running = False
            break
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()