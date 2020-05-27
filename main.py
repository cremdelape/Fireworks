import pygame
import os
import random
from conf import *
import math
from firework import *

# Initialize
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fireworks')
clock = pygame.time.Clock()
fade = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
fade.fill(BLACK_FADED)


fireworks = []


def spawn(pos, button):
    if button == 'left':
        vel = -math.sqrt(2 * G * (HEIGHT - pos[1]))
        fireworks.append(Firework(screen, (pos[0], HEIGHT), vel, True))

    if button == 'right':
        fireworks.append(Firework(screen, pos, random.randrange(-20, -15)))


while True:
    screen.blit(fade, (0, 0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                spawn(mouse_pos, 'left')
            if event.button == 3:
                spawn(mouse_pos, 'right')

    chance = random.random()
    if chance < 0.01:
        fireworks.append(Firework(screen, (random.randrange(0, WIDTH), HEIGHT), random.randrange(-20, -15)))

    for firework in fireworks:
        firework.explode()
        firework.update()
        firework.draw()
        if firework.finished:
            fireworks.remove(firework)
            del firework

    pygame.display.flip()
