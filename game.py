import pygame
from random import randint
import numpy
import time

def matrix(n):
    return numpy.zeros((n,n));

def randomFill(mtx):
    length = len(mtx)
    for i in range(length):
        for j in range(length):
            mtx[i][j] = randint(0,1)

def renderMatrix(population, screen, resolution, dimension):
    white = (255,255,255)
    black = (0,0,0)
    for i in range( dimension ):
        for j in range ( dimension ):
            topLeft  = [i*resolution, j*resolution]
            botRight = [resolution, resolution]
            color = white
            if population[i][j] == 1 :
                color = black
            pygame.draw.rect(screen, color, topLeft + botRight)
    pygame.display.update()

def sumneigh(population, x, z):
    sum = 0
    length = len(population)
    for i in range(3):
        for j in range(3):
            sum += population[(x+i-1+length)%length][(z+j-1+length)%length]%2
    return sum - population[x][z]

def update(population):
    length = len(population)
    for i in range( length ):
        for j in range ( length ):
            val = population[i][j]
            sum = sumneigh(population, i, j)
            if sum == 3:
                population[i][j] += 2
            elif sum == 2:
                population[i][j] += 2*val
    for i in range( length ):
        for j in range ( length ):
            population[i][j] //=2

def main():
    white = (255,255,255)
    black = (0,0,0)
    resolution = 20
    dimension = 30
    pygame.init()
    screen = pygame.display.set_mode((resolution*dimension, resolution*dimension))
    population = matrix( dimension )
    randomFill(population)

    renderMatrix(population, screen, resolution, dimension)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        screen.fill(black)
        update(population)
        renderMatrix(population, screen, resolution, dimension)
        time.sleep(0.5)

main()
