#!/usr/bin/python3

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

ONE_SECOND = 1000

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player1 = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    delta_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # allows the close button to work
        
        # update loop
        for obj in updatable:
            obj.update(delta_time)
        
        screen.fill(color=(0,0,0))
        
        # draw loop
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() #last to update screen
        
        # limit to 60 fps
        delta_time = clock.tick(TARGET_FPS) / ONE_SECOND


if __name__ == "__main__":
    main()
