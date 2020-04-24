import pygame
import random
from tile import Tile
from path1 import Path1
pygame.init()

                    
win = pygame.display.set_mode((1000,600))


pygame.display.set_caption("Jumanji")

bg = pygame.image.load(r'final project\game_bg.png')
char = pygame.image.load(r'final project\monkey2.png')

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
    global walkCount, x,y
    
    win.blit(bg, (12,10))  
    
    win.blit(char, (x, y))
        
    pygame.display.update() 

run = True

while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                incr = random.randint(1,6)
                 # show dice img with number
                steps += incr
                if (steps < 20):
                    x = Path1[steps].xCoordinate
                    y = Path1[steps].yCoordinate
                    print("dice rolled "+str(incr))
                    print("x: "+ str(x) + " y: "+ str(y))
                elif (steps == 20):
                    print("Jumangi")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    redrawGameWindow() 
    
    
pygame.quit()