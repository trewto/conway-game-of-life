import copy
import pygame
from pygame import *
import random
import time 
import sys

# Set window dimensions and block size
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
blockSize = 30  # Size of each grid block

# Calculate the number of rows and columns based on the window size and block size
rows = WINDOW_HEIGHT // blockSize
cols = WINDOW_WIDTH // blockSize

# Colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
CAL = (111,222,178)
SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE = (0, 0, 255)
RED = (200, 0, 0 )
LIGHTRED = (255, 100, 100)
PURPLE = (102, 0, 102)

# Initialize grid arrays
arr = [[0 for i in range(cols)] for j in range(rows)] 
parr = [[0 for i in range(cols)] for j in range(rows)]

# Randomly initialize some grid cells
for _ in range(190):
    x = random.randint(2, rows - 1)
    y = random.randint(2, cols - 1)
    arr[x][y] = 1

def main():
    z = 0
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        z += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                r = event.pos
                arr[int(r[0] / blockSize)][int(r[1] / blockSize)] = 1
                text_surface = font.render(str(int(r[0] / blockSize)), True, RED)
                SCREEN.blit(text_surface, (102, 200))
                    
        drawGrid()
        text_surface = font.render(str(z), True, RED)
        SCREEN.blit(text_surface, (2, 2))
        pygame.display.update()
        time.sleep(0.1)

def drawGrid():
    for x in range(rows):
        for y in range(cols):
            l = arr[x][y]
            if l == 0:
                col = BLACK
            elif l == 1:
                col = CAL
            elif l == 2:
                col = RED
            else:
                col = GREEN 
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, col, rect, 0)
            new(x, y)

    for p in range(rows):
        for q in range(cols):
            if arr[p][q] == parr[p][q] and arr[p][q] > 0:
                arr[p][q] += 1
            else:
                arr[p][q] = parr[p][q]

def new(x, y):
    if x == 0 or y == 0 or x == rows - 1 or y == cols - 1:
        return
    
    i = 0

    # Check surrounding cells
    if arr[x-1][y-1] != 0: i += 1
    if arr[x][y-1] != 0: i += 1
    if arr[x+1][y-1] != 0: i += 1
    if arr[x-1][y] != 0: i += 1
    if arr[x+1][y] != 0: i += 1
    if arr[x-1][y+1] != 0: i += 1
    if arr[x][y+1] != 0: i += 1
    if arr[x+1][y+1] != 0: i += 1
    
    # Update the cell based on neighbor count
    if i < 2 and arr[x][y] != 0:
        parr[x][y] = 0
    elif i > 3 and arr[x][y] != 0:
        parr[x][y] = 0
    elif i == 3 and arr[x][y] == 0:
        parr[x][y] = 1
    else:
        parr[x][y] = arr[x][y]

main()
