import pygame
import sys
import random
import time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

character = pygame.Rect(screen_width // 2, screen_height // 2, 50, 50)

bullets = []
particles = []
points = 0
font = pygame.font.Font(None, 36)
time_since_shot = 0

pointsText = font.render(str(points), True, (255, 255, 255))
youLostText = font.render("Hahahah HAHHahahhahah HAHAHAH", True, (255, 222, 210))
chooseLevelText = font.render("Choose your level", True, (255, 222, 210))
easyText = font.render("Easy", True, (255, 222, 210))
mediumText = font.render("Medium", True, (255, 222, 210))
hardText = font.render("Hard", True, (255, 222, 210))
startText = font.render("Are you ready?", True, (255, 222, 210))



# start
screen.blit(startText, (screen_width // 2, screen_height // 2))
pygame.display.flip()
pygame.time.wait(1500)

screen.blit(chooseLevelText, (screen_width // 2, screen_height // 2))
pygame.display.flip()
screen.blit(easyText, (screen_width // 2, screen_height // 2))
screen.blit(mediumText, (screen_width // 2, screen_height // 2 ))
screen.blit(hardText, (screen_width // 2, screen_height // 2 ))
pygame.display.flip()
level_chosen = False
level_chose = ""

# while not level is chosen
# listen for event when user presses mousebuttondown
# check if the mpusebuttondown is pressed on one of the level texts
# get click position
# get position of text
# check if click position matches with easy text, medium text, hard text
# choose level

while not level_chosen:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if easyText.get_rect(screen_width // 2, screen_height // 2):
                level_chose = "easy"
            elif mediumText.get_rect(screen_width // 2 + 40, screen_height // 2):
                level_chose = "medium"
            elif hardText.get_rect(screen_width // 2 + 40, screen_height // 2):
                level_chose = "hard"
            







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        character.move_ip(5, 0)
    if keys[pygame.K_UP]:
        character.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        character.move_ip(0, 5)

    if character.left < 0:
        character.left = 0
    if character.right > screen_width:
        character.right = screen_width
    if character.top < 0: 
        character.top = 0
    if character.bottom > screen_height: 
        character.bottom = screen_height

    if keys[pygame.K_SPACE]:
        now_time = time.time()
        if (now_time - time_since_shot > 0.5):
            bullet = pygame.Rect(character.x + character.width // 2, character.y + character.height // 2, 10, 10)
            bullets.append(bullet)
            time_since_shot = time.time()
        else:
            print("cant shoot")

    if level_chose == "easy":
         if random.randint(0, 100) < 5:
            particle = pygame.Rect(random.randint(0, screen_width), 0, 25, 25)
            particles.append(particle)
    elif level_chose == "medium":
         if random.randint(0, 100) < 10:
            particle = pygame.Rect(random.randint(0, screen_width), 0, 25, 25)
            particles.append(particle)
    elif level_chose == "hard":
         if random.randint(0, 100) < 25:
            particle = pygame.Rect(random.randint(0, screen_width), 0, 25, 25)
            particles.append(particle)
    

    for bullet in bullets:
        bullet.move_ip(0, -5)
        if bullet.y < 0:
            bullets.remove(bullet)
        for particle in particles:
            if particle.colliderect(bullet):
                try:
                    particles.remove(particle)
                    bullets.remove(bullet)
                    points += 1
                except NameError as e:
                    print(e)
                    continue
                except ValueError as e:
                    print(e)
                    continue  

                    


    for particle in particles:
        particle.move_ip(0, 5)
        if particle.colliderect(character):
            screen.blit(youLostText, (screen_width // 2 - 200, screen_height // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False 
        elif particle.y > screen_height:
            particles.remove(particle)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), character)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)
    for particle in particles:
        pygame.draw.rect(screen, (255, 0, 0), particle)
    screen.blit(pointsText, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()