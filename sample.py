import pygame,sys
pygame.init()
screen=pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris advance version")
clock=pygame.time.Clock()

dark_blue=(44,44,127)

while(True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(dark_blue)
    pygame.display.update()
    clock.tick(60)
