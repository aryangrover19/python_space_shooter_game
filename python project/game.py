import random
from typing import Union
import pygame
from pygame import Surface, SurfaceType
pygame.init()
SIZE = width,height= 1080,720
SCREEN: Union[Surface, SurfaceType] = pygame.display.set_mode(SIZE)

#rgb code
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
BLACK = 0,0,0

bulletsound = pygame.mixer.Sound("assests/sound/mixkit-arcade-mechanical-bling-210.wav")
enemysound = pygame.mixer.Sound("assests/sound/mixkit-arcade-retro-changing-tab-206.wav")

def homescreen():
    font = pygame.font.SysFont(None, 200)
    text = font.render(f"Space Shooter", True, WHITE)

    font_2 = pygame.font.SysFont(None, 100)
    text_2 = font_2.render(f"Press Space to Start Game", True, WHITE)
    while True:
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        SCREEN.blit(text, (50, 250))
        SCREEN.blit(text_2, (100, 550))
        pygame.display.flip()

def playerhealth(count):
    font = pygame.font.SysFont(None,80)
    text = font.render(f"Health : {count}",True,BLACK)
    SCREEN.blit(text,(10,500))

def gameover():
    font = pygame.font.SysFont(None, 100)
    text = font.render(f"Game Over", True, BLACK)
    while True:
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.blit(text, (300, 300))
        pygame.display.flip()

def main():
    move_x = 0

    ship= pygame.image.load("assests/images/spaceship.pod.1.small.blue.png")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = width//2 -ship_w//2
    ship_y = height - ship_h

    enemyship= pygame.image.load("assests/images/spaceship.pod.1.small.red.png")
    eship_w = enemyship.get_width()
    eship_h = enemyship.get_height()

    enemylist = []
    nrow = 3
    ncol = width//eship_w

    #bullet code
    bullet_y = ship_y
    bullet_w = 5
    bullet_h = 10
    movebullet = 0

    for i in range(nrow):
        for j in range(ncol):
            enemyX = eship_w * j
            enemyY = eship_h * i
            enemyRect = pygame.Rect(enemyX ,enemyY,eship_w, eship_h)
            enemylist.append(enemyRect)
            #enemylist.append([enemyX,enemyY])

    random_enemy = random.choice(enemylist)
    enemy_bullet_w = 5
    enemy_bullet_h = 10
    enemy_bullet_y = random_enemy.bottom - 10
    enemy_bullet_x = random_enemy.x + eship_w // 2

    playerhealthcount = 100

    while True:
        bullet_x = ship_x + ship_w // 2 - 2
        eventlist =pygame.event.get()
        for event in eventlist:
        #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit python
                quit()
            #keydown pressing a key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 2
                elif event.key == pygame.K_LEFT:
                     move_x = -2
                elif event.key == pygame.K_SPACE:
                     movebullet = -7
                     bulletsound.play()
            else:
                move_x = 0

        SCREEN.fill(WHITE)

        bullet_rect = pygame.draw.rect(SCREEN,RED, [bullet_x, bullet_y, bullet_w, bullet_h])
        bullet_y += movebullet

        SCREEN.blit(ship,(ship_x, ship_y))
        ship_x += move_x
        ship_rect = pygame.Rect(ship_x,ship_y,ship_w,ship_h)
        enemybullet = pygame.draw.rect(SCREEN,BLUE, [enemy_bullet_x,enemy_bullet_y,enemy_bullet_w,enemy_bullet_h])
        enemy_bullet_y += 7


        for i in range(len(enemylist)-1):
            #SCREEN.blit(enemyship, (enemylist[i][0], enemylist[i][1]))
            SCREEN.blit(enemyship,(enemylist[i].x,enemylist[i].y))

            for i in range(len(enemylist)):
                if bullet_rect.colliderect(enemylist[i]):
                    del enemylist[i]
                    bullet_y = ship_y
                    movebullet = 0
                    break

        if bullet_y<0:
            bullet_y = ship_y
            movebullet = 0

        if enemy_bullet_y > height:
            random_enemy = random.choice(enemylist)
            enemy_bullet_y = random_enemy.bottom - 10
            enemy_bullet_x = random_enemy.x + eship_w // 2
            enemysound.play()
        if enemybullet.colliderect(ship_rect):
            playerhealthcount -= 1
        if playerhealthcount == 0:
            gameover()
        playerhealth(playerhealthcount)
        #update the screen
        pygame.display.flip()
#main()
homescreen()