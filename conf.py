import pygame
pygame.mixer.init()
# General

WIDTH = 800
HEIGHT = 600
G = 0.5

# Firework
SEED_SIZE = 5
PARTICLE_SIZE = 2
PARTICLE_NUM = 100
COOLDOWN = 3000


# Colours

BLACK_FADED = (0, 0, 0, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOURS = [(255, 89, 94), (255, 202, 58), (138, 201, 38), (25, 130, 196), (106, 76, 147)]

launch1 = pygame.mixer.Sound('audio/launch1.wav')
launch2 = pygame.mixer.Sound('audio/launch2.wav')
explode1 = pygame.mixer.Sound('audio/explode1.wav')
explode2 = pygame.mixer.Sound('audio/explode2.wav')
