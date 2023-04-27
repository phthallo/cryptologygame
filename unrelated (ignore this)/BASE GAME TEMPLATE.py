import pygame
pygame.init()

##### Colours #####
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

##### Screen Initialisation #####
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Title")


done = False              
clock = pygame.time.Clock()

##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ##### Game logic #####
    
    ##### Drawing code #####
    screen.fill(BLACK)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
