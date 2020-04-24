import pygame
from pygame import mixer
pygame.init()

class Jumanji():

    def __init__(self):    
        return None


    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, self.textcolor)
        return self.textSurface, self.textSurface.get_rect()

    def button(self, msg,x,y,w,h,ic,ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(self.screen, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("fontfile.ttf",20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.screen.blit(textSurf, textRect)

    #create the screen
    def create_screen(self):
        self.screen = pygame.display.set_mode((1000,600)) #(x,y)/(w,h)
        green = (36,63,40)
        light_green = (68,110,73)
        self.textcolor = (201,172,104)
        #background 
        background = pygame.image.load(r"paint\bg.png")

        # background music
        mixer.music.load(r"final project\jumangi.wav")
        mixer.music.play(-1)

        #Title and Icone
        pygame.display.set_caption("Jumangi")
        icon = pygame.image.load(r"final project\indian.png")
        pygame.display.set_icon(icon)


        # Game loop
        running = True
        while running:
            # RGB = Red, Green, Blue
            self.screen.fill((255,255,255))
            #
            self.screen.blit(background,(0,0))
            #playerX += 0.1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            self.button("Play",450, 390, 150, 55,green,light_green) #game_loop)
            pygame.display.update()

ju = Jumanji()
ju.create_screen()