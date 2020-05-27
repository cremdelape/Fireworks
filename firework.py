import pygame
import math
import random
from conf import *

vec = pygame.math.Vector2

unit = vec(1, 0)
heart_vectors = []
for i in range(360):
    x = 16 * (math.sin(i) ** 3)
    y = -1 * (13 * math.cos(i) - 5 * math.cos(2 * i) - 2 * math.cos(3 * i) - math.cos(4 * i))
    heart_vectors.append(vec(x, y) * 0.25)


class Particle:
    def __init__(self, screen, pos, vel, size, colour):
        self.pos = pos
        self.vel = vel
        self.size = size
        self.screen = screen
        self.colour = colour

    def update(self, acc):
        self.vel += acc
        self.pos += self.vel

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.pos.x), int(self.pos.y)), self.size)


class Firework:
    def __init__(self, screen, pos, vel, heart=False):
        self.g = vec(0, G)
        self.screen = screen
        self.colour = random.choice(COLOURS)
        self.seed = Particle(self.screen, vec(pos), vec(0, vel), SEED_SIZE, self.colour)
        self.particles = []
        self.exploded = False
        self.explode_time = 0
        self.finished = False
        self.heart = heart
        random.choice((launch1, launch2)).play()

    def update(self):
        if not self.exploded:
            self.seed.update(self.g)
        else:
            now = pygame.time.get_ticks()
            if now - self.explode_time > COOLDOWN:
                self.finished = True
        for particle in self.particles:
            if self.heart:
                particle.update(vec(0, 0))
            else:
                particle.update(self.g)

    def draw(self):
        if not self.exploded:
            self.seed.draw()
        for particle in self.particles:
            particle.draw()

    def explode(self):
        if not self.exploded:
            if self.seed.vel.y >= 0:
                for j in range(PARTICLE_NUM):
                    velocity = unit.rotate(random.randrange(0, 360)) * random.randrange(0, 300, 10) / 100
                    if self.heart:
                        velocity = random.choice(heart_vectors)
                    self.particles.append(
                        Particle(self.screen, vec(self.seed.pos.x, self.seed.pos.y), velocity, PARTICLE_SIZE,
                                 self.colour))
                del self.seed
                self.exploded = True
                self.explode_time = pygame.time.get_ticks()
                random.choice((explode1, explode2)).play()
