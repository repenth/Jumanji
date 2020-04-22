import pygame
from pygame import mixer

#initalize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1000,600)) #(x,y)/(w,h)

# background music
mixer.music.load(r"final project\jumangi.wav")
mixer.music.play(-1)

#Title and Icone
pygame.display.set_caption("Jumangi")
icon = pygame.image.load(r"final project\indian.png")
pygame.display.set_icon(icon)


logo_img = pygame.image.load(r"final project\logo.png")
logoX = 000
logoY = 50

#players
player_img = pygame.image.load(r"final project\player.png")
pX = 250
pY = 210

def logo(x,y):
    screen.blit(logo_img, (x, y))

def player(x,y):
    screen.blit(player_img, (x, y))


# Game loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((255,255,255))
    #playerX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    

    logo(logoX, logoY)
    player(pX,pY)

    pygame.display.update()