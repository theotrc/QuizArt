from turtle import Screen, color
from urllib import response
from matplotlib.pyplot import text
from numpy import tile
import pygame
from sqlalchemy import false
from data.data import Title
from data.data import img
from time import *

transformer = Title.transformer

titres = Title.titles
print(transformer(titres[1]))


pygame.init()
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Quiz")
color = (225,225,225)
screen.fill(color)
pygame.display.flip()

color_rect = (215,215,215)


black = (0,0,0)
green = (0,152,0)
red = (200,0,0)
arial_font = pygame.font.SysFont("arial", 30, True)
user_text = ""

i = 1 
sous_partie = 0
game = 1
while game:

    image = pygame.image.load(img.img[i])
    image =  pygame.transform.scale(image, (image.get_size()[0]*1.5, image.get_size()[1]*1.5))
    text = arial_font.render(user_text, True, black)
    pygame.draw.rect(screen, color_rect, pygame.Rect(140, 30, 1000, 500))
    screen.blit(image, ((1280- image.get_size()[0])/2, 50))
    screen.blit(text, (300,560))
    pygame.display.flip()



    


    for event in pygame.event.get():
        # Change the index for the position
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
             game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
                screen.fill(color)
                print (image.get_size())
                print(image.get_size()[1]*2)

            elif event.key==pygame.K_RETURN:
                sous_partie = 1
                while sous_partie:

                    if transformer(user_text) == transformer(titres[i]):

                            image = pygame.image.load(img.img[i])
                            image =  pygame.transform.scale(image, (image.get_size()[0]*1.5, image.get_size()[1]*1.5))                
                            response = arial_font.render(user_text, True, green)
                            pygame.draw.rect(screen, color_rect, pygame.Rect(140, 30, 1000, 500))
                            screen.blit(image, ((1280 - image.get_size()[0])/2, 50))
                            screen.blit(response, (300,560))
                            pygame.display.flip()


                    elif transformer(user_text) != transformer(titres[i]):
                            image = pygame.image.load(img.img[i])
                            image =  pygame.transform.scale(image, (image.get_size()[0]*1.5, image.get_size()[1]*1.5))
                            good_response = arial_font.render(titres[i], True, green)
                                   
                            response = arial_font.render(user_text, True, red)
                            pygame.draw.rect(screen, color_rect, pygame.Rect(140, 30, 1000, 500))
                            screen.blit(image, ((1280- image.get_size()[0])/2, 50))
                            screen.blit(response, (300,560))
                            screen.blit(good_response, (300, 600))
                            pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            game = False
                            sous_partie = 0
                            
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                i += 1
                                user_text = ""
                                sous_partie = 0


                
            else:
                user_text += event.unicode
                print(user_text)
        screen.fill(color)