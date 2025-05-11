import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #aus constants
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()       # all the objects that can be updated
    drawable = pygame.sprite.Group()        # all the objects that can be drawn
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()           # Initialization code that contains all of your shots.

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()        # Wo kommt das her?!
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        
        updatable.update(dt)                # Wo kommt das her?!

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:           
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))              # Black Screen
        
        for obj in drawable:
            obj.draw(screen)                 # re-render the player on the screen each frame
                
        pygame.display.flip()               
        
        dt = clock.tick(60) / 1000          # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()