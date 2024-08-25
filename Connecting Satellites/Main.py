import pgzrun
from random import randint
from time import time

WIDTH = 750
HEIGHT = 550

s_time = 0
e_time = 0
t_time = 0

TITLE  = ('Connecting Satellites')

Sats = []
    


def CreateSatellite():
    for S in range(8):
        sateli = Actor('satellite')
        sateli.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40)
        Sats.append(sateli)

def draw():
    screen.blit('space_background',(0,0))
    num = 1
    for D in Sats:
        D.draw()
        num = num + 1


def update():
    pass


CreateSatellite()
pgzrun.go()