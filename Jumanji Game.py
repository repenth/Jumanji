import pygame
import random
from tile import Tile
from path1 import Path1
pygame.init()

                    
win = pygame.display.set_mode((1050,650))


pygame.display.set_caption("Jumanji")

bg = pygame.image.load('game_bg.png')
char = pygame.image.load('image.png')

x = 400
y = 400
width = 40
height = 60
vel = 20
incr = 0
steps = 0





clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0



def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (12,10))  
    
    win.blit(char, (x, y))
        
    pygame.display.update() 

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        incr = random.randint(1,6)
        print("dice rolled "+str(incr)) # show dice img with number
        steps += incr
        if (steps < 20):
            x = Path1[steps].xCoordinate
            y = Path1[steps].yCoordinate
            print("x: "+ str(x) + " y: "+ str(y))
        else:
            print("all moves have ended")

        

    redrawGameWindow() 
    
    
pygame.quit()