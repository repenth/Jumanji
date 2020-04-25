import pygame
from pygame import mixer
import random
from tile import Tile
from path1 import Path1

#initalize pygame
pygame.init()


def text_objects(text, font):
    textSurface = font.render(text, True, textcolor)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "play":   
                token_screen()     
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(r"jumangi\final project\fontfile.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
def game_btn(msg,x,y,w,h,ic,ac, action=None):
    global tk_screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tk_screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "next":   
                game_screen()     
    else:
        pygame.draw.rect(tk_screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont(r"final project\fontfile.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    tk_screen.blit(textSurf, textRect)


pygame.display.set_caption("Jumangi")
icon = pygame.image.load(r"final project\indian.png")
pygame.display.set_icon(icon)


#bg music

mixer.music.load(r"final project\jumangi.wav")
mixer.music.play(-1)

def intro():
    global screen, textcolor
    screen = pygame.display.set_mode((1000,600)) #(x,y)/(w,h)
    green = (36,63,40)
    light_green = (68,110,73)
    textcolor = (201,172,104)
    #background 
    background = pygame.image.load(r"final project\bg.png")

    
    #Title and Icone
    

    # Game loop
    running = True
    while running:
        # RGB = Red, Green, Blue
        screen.fill((255,255,255))
        #
        screen.blit(background,(0,0))
        #playerX += 0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        

        button("Play!",450, 390, 150, 55,green,light_green, "play")
        pygame.display.update()


def token_screen():
    #create the screen
    global tk_screen, background, textSurf, textRect, name
    green = (36,63,40)
    light_green = (68,110,73)
    textcolor = (201,172,104)
    tk_screen = pygame.display.set_mode((1000,600)) #(x,y)/(w,h)
    background = pygame.image.load(r"final project\screen2.png")

    # background music

    running = True
    while running:
        tk_screen.fill((255,255,255))
        tk_screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        game_btn("Proceed",740, 500, 150, 55,green,light_green, "next")
        
        pygame.display.update()

def game_screen():
    gm_screen = pygame.display.set_mode((1000,600))


    pygame.display.set_caption("Jumanji")

    bg = pygame.image.load(r'final project\game_bg.png')

    char = pygame.image.load(r"final project\image.png")
    x = 263
    y = 500

    elephant_ = pygame.image.load(r"final project\elephant.png")
    eX = 260
    eY = 10

    def elephant(x,y):
        gm_screen.blit(elephant_, (x, y))

    rhino_ = pygame.image.load(r"final project\rhino.png")
    rX = 705
    rY = 10

    def rhino(x,y):
        gm_screen.blit(rhino_, (x, y))

    croc_ = pygame.image.load(r"final project\croc.png")
    cX = 705
    cY = 500

    def croc(x,y):
        gm_screen.blit(croc_, (x, y))
    #width = 100
    #height = 100
    vel = 20
    incr = 0
    steps = 0





    clock = pygame.time.Clock()
    left = False
    right = False


    def redrawGameWindow(x ,y):
        
        gm_screen.blit(bg, (12,10))  
        
        gm_screen.blit(char, (x, y))
        elephant(eX,eY)
        rhino(rX,rY)
        croc(cX,cY)
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
                        x = 505
                        y = 251
                        print("Jumangi")

        redrawGameWindow(x, y) 
        
        
    pygame.quit()


intro()