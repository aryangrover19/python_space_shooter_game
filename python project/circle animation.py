import pygame
pygame.init()
SIZE = width,height= 1080,720
SCREEN = pygame.display.set_mode(SIZE)
WHITE = 255,255,255
RED = 255,0,0
BLUE = 0,0,255
BLACK = 0,0,0
SCREEN.fill(WHITE)
circle_x = 50
circle_y = 50
radius = 50

speed_x = 1
speed_y = 1

while True:
    eventlist =pygame.event.get()
    for event in eventlist:
    #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    SCREEN.fill(WHITE)
    pygame.draw.circle(SCREEN, BLUE, [circle_x,circle_y] ,  radius)
    circle_x += speed_x
    circle_y += speed_y

    if circle_x > width - radius:
        speed_x = -1
    elif circle_y > height - radius:
        speed_y = -1
    elif circle_x < radius:
        speed_x = 1
    elif circle_y < radius:
        speed_y = 1

    #update the screen
    pygame.display.flip()
