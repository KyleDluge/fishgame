#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:08:38 2021

@author: kyledluge
"""
# setup 
import pygame
import random
import math
import time


pygame.init()
screen = pygame.display.set_mode((800, 600))



#Title/Display
pygame.display.set_caption("GAMETRON")

icon= pygame.image.load("fisherman.png")
pygame.display.set_icon(icon)

seaweed = pygame.image.load('seaweed.png')
seaweedX = 200
seaweedY = 540

seaweed2 = pygame.image.load('seaweed2.png')
seaweed2X = 600
seaweed2Y = 490


sun = pygame.image.load('sun.png')
sunX = 700
sunY = 20

#Score

score_value = 0
level_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

level_textX = 10
level_textY = 40




def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 0 ))
    screen.blit(score, (x, y))

def show_level(x, y):
    level = font.render("Level: " + str(level_value), True, (255, 255, 0))
    screen.blit(level, (x, y))


#Weapons

anchor = pygame.image.load('anchor.png')
anchorX = 0
anchorY = 150
anchorX_change = 0
anchorY_change = .2
anchor_state = "ready"

#Player - Fisherman
fisherman = pygame.image.load("fisherman.png")
fishermanX = 100
fishermanY = 150
fishermanX_change = 0 



#Fishboys
fishboy = pygame.image.load("fish.png")
fishboyX = random.randint(32, 768)
fishboyY = random.randint(200, 568)
fishboyX_change = 0.3
fishboyY_change = 10

fishboy2 = pygame.image.load('fish.png')
fishboy2X = random.randint(32, 768)
fishboy2Y = random.randint(200, 568)
fishboy2X_change = 0.2
fishboy2Y_change = 5

fishboy3 = pygame.image.load('fish2.png')
fishboy3X = random.randint(32, 768)
fishboy3Y = random.randint(200, 568)
fishboy3X_change = 0.1

fishboy4 = pygame.image.load('fish3.png')
fishboy4X = random.randint(32, 768)
fishboy4Y = random.randint(200, 568)
fishboy4X_change = 0.5


diver = pygame.image.load('scuba.png')
diverX = random.randint(32, 768)
diverY = random.randint(200, 568)
diverX_change = 0.1
diverY_change = 0.1

jelly = pygame.image.load('jellyfish.png')
jellyX = random.randint(32, 768)
jellyY = random.randint(200, 568)
jellyX_change = 0.03
jellyY_change = 0.03





#Functions 

def fish(x, y):
    screen.blit(fishboy, (x, y))

def fish2(x, y):
    screen.blit(fishboy2, (x, y))

def fish3(x, y):
    screen.blit(fishboy3, (x, y))
    
def fish4(x, y):
    screen.blit(fishboy4, (x, y))
    
def player(x, y):
    screen.blit(fisherman,(x, y))
    
def scuba(x, y):
    screen.blit(diver, (x, y))
    
def jellyfish(x, y):
    screen.blit(jelly, (x, y))

#object functions
def weed():
    screen.blit(seaweed, (seaweedX, seaweedY))

def weed2():
    screen.blit(seaweed2, (seaweed2X, seaweed2Y))
    
def sunny():
    screen.blit(sun, (sunX, sunY))
    
    

def fire_anchor(x, y):
    global anchor_state
    anchor_state = 'fire'
    screen.blit(anchor, (x, y))
    
    
def isCollision(fishboyX, fishboyY, anchorX, anchorY):
    distance = math.sqrt((math.pow(fishboyX - anchorX,2))+(math.pow(fishboyY - anchorY,2)))
    if distance < 27:
        return True
    else:
        return False

def isCollision2(fishboy2X, fishboy2Y, anchorX, anchorY):
    distance = math.sqrt((math.pow(fishboy2X - anchorX,2))+(math.pow(fishboy2Y - anchorY,2)))
    if distance < 27:
        return True
    else:
        return False

def isCollision3(fishboy3X, fishboy3Y, anchorX, anchorY):
    distance = math.sqrt((math.pow(fishboy3X - anchorX,2))+(math.pow(fishboy3Y - anchorY,2)))
    if distance < 32:
        return True
    else:
        return False
    
def isCollision4(fishboy4X, fishboy4Y, anchorX, anchorY):
    distance = math.sqrt((math.pow(fishboy4X - anchorX,2))+(math.pow(fishboy4Y - anchorY,2)))
    if distance < 32:
        return True
    else:
        return False
    
def isCollision5(diverX, diverY, anchorX, anchorY):
    distance = math.sqrt((math.pow(diverX - anchorX,2))+(math.pow(diverY - anchorY,2)))
    if distance < 27:
        return True
    else:
        return False
    
def isCollision6(jellyX, jellyY, anchorX, anchorY):
    distance = math.sqrt((math.pow(jellyX - anchorX,2))+(math.pow(jellyY - anchorY,2)))
    if distance < 20:
        return True
    else:
        return False







running = True

while running:
    screen.fill((64, 188, 255)) 
    

    #Keyboard 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fishermanX_change = 0.15
            if event.key == pygame.K_LEFT:
                fishermanX_change = -0.15
            if event.key == pygame.K_SPACE:
                if anchor_state is 'ready':
                    anchorX = fishermanX
                    fire_anchor(anchorX, anchorY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                fishermanX_change = 0
        

                
                
                
    # Player Boudary     
    fishermanX += fishermanX_change
    if fishermanX <=0:
        fishermanX = 0 
    elif fishermanX >= 736:
        fishermanX = 736
        
        

    # Fish Boundaries and movement
    fishboyX += fishboyX_change
    if fishboyX <=0:
        fishboyX_change = 0.2

    elif fishboyX >= 736:
        fishboyX_change = -0.2

      
    fishboy2X += fishboy2X_change
    if fishboy2X <=0:
        fishboy2X_change = 0.5
 
    elif fishboy2X >= 736:
        fishboy2X_change = -0.3

        
    fishboy3X += fishboy3X_change
    if fishboy3X <=0:
        fishboy3X_change = 0.3
    elif fishboy3X >= 736:
        fishboy3X_change = -0.1
    
    fishboy4X += fishboy4X_change
    if fishboy4X <=0:
        fishboy4X_change = 0.3
        
    elif fishboy4X >= 736:
        fishboy4X_change = -0.4
        
    diverX += diverX_change
    if diverX <=0:
        diverX_change = 0.1
    elif diverX >= 736:
        diverX_change = -0.1
        
    diverY += diverY_change
    if diverY <=200:
        diverY_change = 0.1
    elif diverY >=800:
        diverY_change = -0.1
        
    jellyX += jellyX_change
    if jellyX <=0:
        jellyX_change = 0.03
    elif jellyX >= 736:
        jellyX_change = -0.02       
        
    jellyY += jellyY_change
    if jellyY <=300:
        jellyY_change = 0.03
    elif jellyY >=800:
        jellyY_change = -0.04
        
        
        
        
    #Levels
    if score_value >=300:
        level_value =1
    if score_value >=800:
        level_value =2
    if score_value >=1500:
        level_value =3
    if score_value >=2000:
        level_value =4
    if score_value >=3000:
        level_value =5
    if score_value >=4200:
        level_value =6
    if score_value >=5500:
        level_value =7
    if score_value >=7500:
        level_value =8
    if score_value >=9800:
        level_value =9
    if score_value >=11500:
        level_value =10
    if score_value >=15000:
        level_value =11
    if score_value >=20000:
        level_value =12
        
        
        
    # Anchor Movement
    if anchorY >= 600:
        anchorY = 150 
        anchor_state = "ready"
        
    if anchor_state is "fire":
        fire_anchor(anchorX, anchorY)
        anchorY += anchorY_change
        
        
    #Collision
    collision = isCollision(fishboyX, fishboyY, anchorX, anchorY)
    if collision:
        anchorY = 150
        anchor_state = 'ready'
        score_value += 100
        fishboyX = random.randint(32, 768)
        fishboyY = random.randint(200, 568)
        
    collision2 = isCollision2(fishboy2X, fishboy2Y, anchorX, anchorY)
    if collision2:
        anchorY = 150
        anchor_state = 'ready'
        score_value += 100
        fishboy2X = random.randint(32, 768)
        fishboy2Y = random.randint(200, 568)
        
    collision3 = isCollision3(fishboy3X, fishboy3Y, anchorX, anchorY)
    if collision3:
        anchorY = 150
        anchor_state = 'ready'
        score_value += 100    
        fishboy3X = random.randint(32, 768)
        fishboy3Y = random.randint(200, 568)
        
    collision4 = isCollision4(fishboy4X, fishboy4Y, anchorX, anchorY)
    if collision4:
        anchorY = 150
        anchor_state = 'ready'
        score_value += 200
        fishboy4X = random.randint(32, 768)
        fishboy4Y = random.randint(200, 568)

    collision5 = isCollision5(diverX, diverY, anchorX, anchorY)
    if collision5:
        anchorY = 150
        anchor_state = 'ready'
        score_value -= 500
        diverX = random.randint(32, 768)
        diverY = random.randint(200, 568)
        
    collision6 = isCollision6(jellyX, jellyY, anchorX, anchorY)
    if collision6:
        anchorY = 150
        anchor_state = 'ready'
        score_value += 300
        jellyX = random.randint(0, 800)
        jellyY = random.randint(300, 800)
        
        
    fish(fishboyX, fishboyY)
    fish2(fishboy2X, fishboy2Y)
    fish3(fishboy3X, fishboy3Y)
    fish4(fishboy4X, fishboy4Y)
    scuba(diverX, diverY)
    jellyfish(jellyX, jellyY)
    
    

    player(fishermanX, fishermanY)
    weed()
    weed2()
    sunny()
    show_score(textX, textY)
    show_level(level_textX, level_textY)
    pygame.display.update()
    