import pygame

def clearScreenText(screen, background_color, all_sprites):
    screen.fill(background_color)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()