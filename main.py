# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def starting():
    print("Starting Asteroids!")

def main():
    # Initialize the game
    pygame.init()

    #Initialize the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

