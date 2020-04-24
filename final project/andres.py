import pygame
pygame.init()
x = 0
y = 0

screen = pygame.display.set_mode((1000,600))
bg = pygame.image.load(r'final project\yoyo1.PNG')
pygame.display.set_caption('Testing')
token_x = 400
token_y = 400
token = pygame.image.load(r"final project\monkey2.png")
running = True
while running:
   for event in pygame.event.get():
      if event.type == QUIT:
         running = False
      if event.type == KEYDOWN and event.key == K_ESCAPE:
         running = False
      if event.type == MOUSEBUTTONDOWN:
         #print event.button
         print(pygame.mouse.get_pos())
   
   pygame.display.update()