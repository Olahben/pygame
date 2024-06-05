import pygame
import random

def clearScreenText(screen, background_color, all_sprites):
    screen.fill(background_color)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

def renderParticle(particle, game_mode, sprites, particles):
    if game_mode == "easy":
        if random.randint(0, 100) < 12:
            sprites.add(particle)
            particles.add(particle)
    elif game_mode == "medium":
        if random.randint(0, 100) < 22:
            sprites.add(particle)
            particles.add(particle)
    elif game_mode == "hard":
        if random.randint(0, 100) < 45:
            sprites.add(particle)
            particles.add(particle)
