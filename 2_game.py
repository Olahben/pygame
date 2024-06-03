import pygame
import time

# Spill med karakterer som skyter partikler og faar poeng for hvert skutt partikkel
# bruk vektorer
# bruk objektorientert programmering
# bruk kollisjoner

pygame.init()

# colors
colorDict = {
    "B": (0, 0, 0),
    "text": (255, 255, 255),
    "white": (255, 255, 255)
}

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

# visible objects, characters, initialization of them
class MainCharacter:
    def __init__(self, width, height):
        self.character = pygame.Rect(game_screen.x_half, game_screen.y_half, width, height)
    def draw(self):
        pygame.draw.rect(game_screen.screen, colorDict["B"], self.character)

character_width = 50
character_height = 50
main_character = MainCharacter(character_width, character_height)
main_character.draw()

# start
game_screen.screen.blit(textDict["welcome"], game_screen.half_res)