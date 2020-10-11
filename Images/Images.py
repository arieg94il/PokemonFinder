import pygame, sys
from pygame.locals import *
from Dimentions import PLAYER_WIDTH, PLAYER_HEIGHT, INTRO_IMG_WIDTH, INTRO_IMG_HEIGHT

player_image = pygame.image.load("Images/player.png")
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH,PLAYER_HEIGHT))

bul_image = pygame.image.load("Images/bul.png")
bul_image = pygame.transform.scale(bul_image, (PLAYER_WIDTH,PLAYER_HEIGHT))

char_image = pygame.image.load("Images/char.png")
char_image = pygame.transform.scale(char_image, (PLAYER_WIDTH,PLAYER_HEIGHT))

evee_image = pygame.image.load("Images/evee.png")
evee_image = pygame.transform.scale(evee_image, (PLAYER_WIDTH,PLAYER_HEIGHT))

pika_image = pygame.image.load("Images/pika.png")
pika_image = pygame.transform.scale(pika_image, (PLAYER_WIDTH,PLAYER_HEIGHT))

squir_image = pygame.image.load("Images/squir.png")
squir_image = pygame.transform.scale(squir_image, (PLAYER_WIDTH,PLAYER_HEIGHT))

Pikachu_Intro = pygame.image.load("Images/pikachu_intro.png")
Pikachu_Intro = pygame.transform.scale(Pikachu_Intro, (INTRO_IMG_WIDTH,INTRO_IMG_HEIGHT))

programIcon = pygame.image.load('Images/ball.png')

Ash = pygame.image.load("Images/ash.png")
Ash = pygame.transform.scale(Ash, (INTRO_IMG_WIDTH,INTRO_IMG_HEIGHT*2))

