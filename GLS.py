import pygame
import random

pygame.init()
SIZE = (600,600)
FPS = 60
SEPARATION = 5

Tile = int( SIZE[0]/SEPARATION )
line_width = 10

Black= (0, 0, 0)
Grey= (169, 169, 169)
Maroon= (128, 0, 0)
Navy= (0, 0, 128)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GLS")
clock = pygame.time.Clock()
done = False

def is_number_in_array(num,arr):
    #if num in arr.values():return True 
    cods=arr.values()
    if num in cods:return True 
    return False

def get_rand_matr(SEPARATION):
    matr={}
    for i in range(1,SEPARATION+1):
        for j in range(1,SEPARATION+1):
            Flag=True
            while Flag:
                numbers=random.randint(1,SEPARATION*SEPARATION)
                if is_number_in_array(numbers,matr):continue
                matr.update({(i,j):numbers})
                Flag=False
    return matr

Field=get_rand_matr(SEPARATION)
print(Field)

def Draw():
    screen.fill(Grey) 
    for i in range(1, SEPARATION):
            pygame.draw.line(screen, Black, (0, i * Tile), (SIZE[0], i * Tile),line_width) 
            pygame.draw.line(screen,Black,(i*Tile ,0),(i*Tile ,SIZE[0]),line_width)  

while  not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        Draw()
        
        pygame.display.flip()
        clock.tick(60)
pygame.quit()