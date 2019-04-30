from datetime import date
import json
import requests
import pygame
import math

def getMoonData(MM, YYYY):
    headers = {'Content-Type': 'application/json'}
    api = "http://www.icalendar37.net/lunar/api/?lang=en&month=" + MM + "&year=" + YYYY
    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def main():

    pygame.init()
    dimension = 600
    size = 32
    screen = pygame.display.set_mode((dimension, dimension))
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 20)

    today = date.today()
    MM =  str(today.month)
    YYYY =   str(today.year)
    DD = str(today.day)


    MoonData = getMoonData(MM, YYYY)
    MoonImg = {}
    MoonImg = pygame.image.load("moon.png");
    MoonImg = pygame.transform.scale(MoonImg, (size, size))

    if MoonData is not None:
        length = int(MoonData["daysMonth"])
        for i in range(length):
            day = str(i+1)
            moonphase = MoonData["phase"][day]["phaseName"]
            mX = dimension/2 + math.cos(2*i*math.pi/length)*(dimension/2 - size/2) - size/2
            mY = dimension/2 - math.sin(2*i*math.pi/length)*(dimension/2 - size/2) - size/2
            textsurface = myfont.render(day, True, (255, 255, 255))
            screen.blit(MoonImg, (mX,mY))
            screen.blit(textsurface,(mX+size/2,mY+4))
        pygame.display.update()

    else:
        print('Request failed for some reason ;|')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

main()
