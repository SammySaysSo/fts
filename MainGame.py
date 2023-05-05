# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:35:12 2021

@author: sambr
"""
#todolist: 
import pygame
import random

#to do list: controls & what to do(intro-spacebar), ending credits(music/starter code), change code

pygame.init()
pygame.display.set_caption('Finish The Song')

score = 0
checkS = 0
WIDTH = 800
HEIGHT = 600
c = 1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pPos = [WIDTH/2, HEIGHT-100]
pSize = 50

ePos = [random.randint(0, WIDTH-50), 0]
eList = [ePos]
speed = 7
ePosRight = [-50, random.randint(0, HEIGHT-50)]
ePosLeft = [WIDTH, random.randint(0, HEIGHT-50)]
ePosUp = [random.randint(0, WIDTH-50), HEIGHT]
timeCheck = [900, 0]

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
green = (0, 255, 0)

gameOver = False
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)
myFont2 = pygame.font.SysFont("monospace", 70)


def dropEnemies(eList, c):
    delay = random.random()
    if len(eList) < c and delay < 0.1: eList.append([random.randint(0, WIDTH-50), 0])
def drawEnemies(eList):
    for ePos in eList:
        pygame.draw.rect(screen, blue, (ePos[0], ePos[1], pSize, pSize))  
def updateEnemyPositions(eList, score):
    for indx, ePos in enumerate(eList):
        if ePos[1] >= 0 and ePos[1] < HEIGHT: ePos[1] += speed
        else: 
            eList.pop(indx)
            score += 1
    return score
def detectCollision(eList, pPos):
    for ePos in eList:
        if collisionCheck(pPos, ePos): return True
    return False
def collisionCheck(pPos, ePos):
    px = pPos[0]
    py = pPos[1]
    ex = ePos[0]
    ey = ePos[1]
    if ex >= px and ex < (px+pSize) or px >= ex and px < (ex+pSize):
        if ey >= py and ey < (py+pSize) or py >= ey and py < (ey+pSize):
            return True
    return False
def addEnemies(score, c, checkS):
    if score >= 3: c = 2
    if score >= 10: c = 3
    if score >= 20: c = 4
    if score >= 40: c = 5
    if score >= 60: c = 7
    if score >= 90: c = 8
    if checkS > 45: c = 1
    if checkS >= 77: c = 7
    if checkS >= 100: c = 1 #end 100, 110
    return c
def addSpeed(score, speed):
    if score >= 3: speed = 8
    if score >= 20: speed = 9
    if score >= 40: speed = 10
    if score >= 60: speed = 11
    if score >= 90: speed = 12
    return speed

def introToGame():
    print('running intro')
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_RETURN:
                     intro = False
                     mainGame(score, c, speed)
                     break
                 if event.key == pygame.K_SPACE:
                     intro = False
                     introRules()
                     break
        #draw our start screen to the display
        if intro:
            screen.fill(red)
            text = "Finish The Song"
            text2 = "Press Enter to start the game"
            text3 = "Press Space to see how to play"
            label = myFont2.render(text, 1, white)
            label2 = myFont.render(text2, 1, black)
            label3 = myFont.render(text3, 1, black)
            screen.blit(label, (95, HEIGHT/2-200))
            screen.blit(label2, (100, HEIGHT/2))
            screen.blit(label3, (100, HEIGHT/2+100))
            
            pygame.display.update()
            clock.tick(15)

def introRules():
    print('running introRules')
    introRules = True
    while introRules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     introRules = False
                     introToGame()
                     break
        #draw our start screen to the display
        if introRules:
            screen.fill(red)
            text = "Finish The Song"
            text2 = "Press Space to go back to main"
            text3 = "Use the wsad/arrow keys to move"
            text4 = "Dodge the blue boxes"
            text5 = "Finish the song to win the game"
            label = myFont2.render(text, 1, white)
            label2 = myFont.render(text2, 1, black)
            label3 = myFont.render(text3, 1, black)
            label4 = myFont.render(text4, 1, black)
            label5 = myFont.render(text5, 1, black)
            screen.blit(label, (95, 50))
            screen.blit(label2, (100, 500))
            screen.blit(label3, (100, 200))
            screen.blit(label4, (100, 300))
            screen.blit(label5, (100, 400))
            
            pygame.display.update()
            clock.tick(15)

def ending(checkS):
    print('running end', checkS)
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_RETURN:
                     end = False
                     mainGame(score, c, speed)
                     break
                 if event.key == pygame.K_SPACE:
                     end = False
                     endingCredits(checkS)
                     break
        #draw our start screen to the display
        if end:
            screen.fill(blue)
            if checkS < 110: text3 = "You Failed to"
            else: text3 = "You Completed"
            text = "Finish the Song"
            text2 = "Press Enter to play again"
            text4 = "Press Space to go to credits"
            label = myFont2.render(text, 1, white)
            label2 = myFont.render(text2, 1, black)
            label4 = myFont.render(text4, 1, black)
            label3 = myFont2.render(text3, 1, white)
            screen.blit(label, (95, HEIGHT/2-200))
            screen.blit(label2, (100, HEIGHT/2))
            screen.blit(label4, (100, HEIGHT/2+100))
            screen.blit(label3, (95, HEIGHT/2-300))
            
            pygame.display.update()
            clock.tick(15)
            
def endingCredits(checkS):
    print('running endingCredits')
    endCredits = True
    ch = 0
    while endCredits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     endCredits = False
                     ending(checkS)
                     break
        #draw our start screen to the display
        if endCredits:
            screen.fill(blue)
            text = "Credits"
            text2 = "Press Space to go back to ending"
            text3 = "Made by Sam Brey"
            text4 = "EKU \u00A9 2021"
            text5 = "See console for more details"
            label = myFont2.render(text, 1, white)
            label2 = myFont.render(text2, 1, black)
            label3 = myFont.render(text3, 1, black)
            label4 = myFont.render(text4, 1, black)
            label5 = myFont.render(text5, 1, black)
            screen.blit(label, (95, 50))
            screen.blit(label2, (100, 500))
            screen.blit(label3, (100, 200))
            screen.blit(label4, (100, 300))
            screen.blit(label5, (100, 400))
            if ch == 0:
                print('Song: Warriyo - Mortals (feat. Laura Brehm) [NCS Release]')
                print('Song by NCS(NoCopyrightSounds) and thus free for me to use since I\'m making no money and showing where I got the song from.')
                print('Used various parts of the internet and class materials to bring this game togther.')
                print('1: Used pygame: https://www.pygame.org/docs/ref/display.html')
                print('2: Uses from google: https://www.fileformat.info/info/unicode/char/a9/index.htm & https://www.rapidtables.com/web/color/RGB_Color.html & https://www.youtube.com/watch?v=-8n91btt5d8 by Keith Galli(says free to use for educational purposes) with https://github.com/KeithGalli/Basic-Python-Game/blob/master/game.py.')
                print('3: Uses from class work: two examples of games we used. Worked with sound from the car game.')
                ch += 1
            pygame.display.update()
            clock.tick(15)
    
def mainGame(score, c, speed):
    print('running main')
    score = 0
    c = 1
    speed = 7
    pygame.mixer.music.load('mortals.wav')
    pygame.mixer.music.play()
    if score == 0: gameOver = False
    checkS = 0
    ePosRight[0] = -50
    ePosLeft[0] = WIDTH
    ePosUp[1] = HEIGHT
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    if pPos[0] >= 50: pPos[0] -= 50
                elif event.key == pygame.K_RIGHT: 
                    if pPos[0] <= WIDTH-100: pPos[0] += 50
                elif event.key == pygame.K_UP: 
                    if pPos[1] >= 50: pPos[1] -= 50
                elif event.key == pygame.K_DOWN: 
                    if pPos[1] <= HEIGHT-100: pPos[1] += 50
                elif event.key == pygame.K_a:
                    if pPos[0] >= 50: pPos[0] -= 50
                elif event.key == pygame.K_d:
                    if pPos[0] <= WIDTH-100: pPos[0] += 50
                elif event.key == pygame.K_w:
                    if pPos[1] >= 50: pPos[1] -= 50
                elif event.key == pygame.K_s:
                    if pPos[1] <= HEIGHT-100: pPos[1] += 50
        if checkS < 45: screen.fill(black)
        elif checkS < 77: screen.fill(white)
        else: screen.fill(black)
        
        dropEnemies(eList, c)
        score = updateEnemyPositions(eList, score)
        text = "Score:" + str(score)
        if checkS < 45: label = myFont.render(text, 1, yellow) #1 horiziontal 0 for vertical?
        elif checkS < 77: label = myFont.render(text, 1, black)
        else: label = myFont.render(text, 1, yellow)
        screen.blit(label, (0, HEIGHT-40)) #actually put text to screen
        c = addEnemies(score, c, checkS)
        speed = addSpeed(score, speed)
        drawEnemies(eList)
        # rect: (surface, color, (x, y, width, height))
        timeCheck[1] += 10
        if timeCheck[1] >= HEIGHT: 
            timeCheck[1] = 0
            timeCheck[0] = 900
            checkS += 1 #timer for song
            print(checkS)
        if checkS >= 65 and checkS <= 100: #end
            ePosRight[0] += 7
            ePosLeft[0] -= 8
            ePosUp[1] -= 9
        if ePosRight[0] >= WIDTH: 
            ePosRight[1] = random.randint(0, HEIGHT-50)
            ePosRight[0] = -50
            score += 1
        if ePosLeft[0] <= 0: 
            ePosLeft[0] = WIDTH
            ePosLeft[1] = random.randint(0, HEIGHT-50)
            score += 1
        if ePosUp[1] <= 0: 
            ePosUp[1] = HEIGHT
            ePosUp[0] = random.randint(0, WIDTH-50)
            score += 1
        if checkS > 100:
            ePosRight[0] = -50
            ePosLeft[0] = WIDTH
            ePosUp[1] = HEIGHT
        if checkS >= 110:
            gameOver = True
            pPos[0] = WIDTH/2
            pPos[1] = HEIGHT/2
            break
        if collisionCheck(pPos, ePosRight) and score > 0:
            gameOver = True
            pPos[0] = WIDTH/2
            pPos[1] = HEIGHT/2
            break
        if collisionCheck(pPos, ePosLeft) and score > 0:
            gameOver = True
            pPos[0] = WIDTH/2
            pPos[1] = HEIGHT/2
            break
        if collisionCheck(pPos, ePosUp) and score > 0:
            gameOver = True
            pPos[0] = WIDTH/2
            pPos[1] = HEIGHT/2
            break
        if detectCollision(eList, pPos) and score > 0:
            gameOver = True
            pPos[0] = WIDTH/2
            pPos[1] = HEIGHT/2
            break
        pygame.draw.rect(screen, blue, (ePosRight[0], ePosRight[1], pSize, pSize))
        pygame.draw.rect(screen, blue, (ePosLeft[0], ePosLeft[1], pSize, pSize))
        pygame.draw.rect(screen, blue, (ePosUp[0], ePosUp[1], pSize, pSize))
        pygame.draw.rect(screen, red, (pPos[0], pPos[1], pSize, pSize))
        
        pygame.draw.rect(screen, blue, (timeCheck[0], timeCheck[1], pSize, pSize))
        
        clock.tick(30) #FPS: 30
        pygame.display.update()
    
    pygame.mixer.music.stop()
    ending(checkS)

introToGame()