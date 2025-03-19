import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    
    asteroids = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    field = AsteroidField()
    
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    a.split()
                    s.kill()
        
        for a in asteroids:
            if a.collides_with(player):
                print("Game Over!")
                sys.exit()
        
        screen.fill((0,0,0))
        
        
        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    




if __name__ == "__main__":
    main()