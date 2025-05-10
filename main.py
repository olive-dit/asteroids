import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #aus constants
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        
        screen.fill((0, 0, 0))              # Black Screen
        player.draw(screen)                 # re-render the player on the screen each frame
        pygame.display.flip()               
        
        dt = clock.tick(60) / 1000          # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")