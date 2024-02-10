import pygame
import random
pygame.init()
SIZE=(600,600)
FPS=60
SEPARATION=3

Tile=int(SIZE[0]/SEPARATION)
line_width=10
Field=[[0]*SEPARATION]*SEPARATION#переделать


Black=(0, 0, 0)
Grey=(169, 169, 169)
Maroon=(128, 0, 0)
Navy=(0, 0, 128)


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GLS")
clock = pygame.time.Clock()
done = False

def filling():
        Count=0
        for i in range(0,SEPARATION):
                
                for j in range(0,SEPARATION):
                        Count+=1
                        Field[j][i]=Count


def Draw():
    screen.fill(Grey) 
    for i in range(1, SEPARATION):
            pygame.draw.line(screen, Black, (0, i * Tile), (SIZE[0], i * Tile),line_width) 
            pygame.draw.line(screen,Black,(i*Tile,0),(i*Tile,SIZE[0]),line_width)  

filling()
print(Field)   

            


while  not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        Draw()
        
        pygame.display.flip()
        clock.tick(60)
pygame.quit()