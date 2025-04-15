# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from groups import updatables, drawables
from player import Player

def starting():
    print("Starting Asteroids!")

def main():
    # Initialize the game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Setting the FPS
    clock = pygame.time.Clock()
    FPS = 60
    dt = 0

    # Create the player
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Setting up the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update all updatable objects
        updatables.update(dt)
        
        screen.fill("black")
        
        # Draw all drawable objects
        for drawable in drawables:
            drawable.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()

