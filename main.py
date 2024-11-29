#!/usr/bin/python3

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

ONE_SECOND = 1000

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # setup
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # allows the close button to work
        
        screen.fill(color=(0,0,0))        
        pygame.display.flip() #last to update screen
        delta_time = clock.tick(TARGET_FPS) / ONE_SECOND


if __name__ == "__main__":
    main()
