#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:08:38 2021

@author: kyledluge
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

#Title
pygame.display.set_caption("GAMETRON")

icon= pygame.image.load("fisherman.png")
pygame.display.set_icon(icon)



#Player - Fisherman

fisherman = pygame.image.load("fisherman.png")
fishermanX = 100
fishermanY = 150
fishermanX_change = 0 

fishboy = pygame.image.load("fish.png")
fishboyX = 400
fishboyY = 450

fishboy2 = pygame.image.load('fish.png')
fishboy2X = 570
fishboy2Y = 320

fishboy3 = pygame.image.load('fish.png')
fishboy3X = 120
fishboy3Y = 420


def fish():
    screen.blit(fishboy, (fishboyX,fishboyY))

def fish2():
    screen.blit(fishboy2, (fishboy2X, fishboy2Y))

def fish3(x, y):
    screen.blit(fishboy3, (x, y))
    
def player(x, y):
    screen.blit(fisherman,(x, y))


running = True

while running:
    screen.fill((255, 255, 50)) 

    if fishboy3X < 700:
        fishboy3X += .1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fishermanX_change = 0.1
            if event.key == pygame.K_LEFT:
                fishermanX_change = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                fishermanX_change = 0
    
    fish()
    fish2()
    fish3(fishboy3X, fishboy3Y)
    fishermanX += fishermanX_change
    player(fishermanX, fishermanY)

    pygame.display.update()
    