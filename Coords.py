#!/usr/bin/python
import pygame
from pygame.locals import *


def main():
   pygame.init()
   pygame.display.set_mode((1150,680))
   pygame.display.set_caption('Testing')
   pygame.image.load("monkey2.png").convert()
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

bg = pygame.image.load('yoyo1.PNG')
   #pygame.display.quit()

if __name__ == '__main__':
   main()