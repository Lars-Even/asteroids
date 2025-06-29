import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width: "+ str(SCREEN_WIDTH))
    print("Screen height: "+ str(SCREEN_HEIGHT))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    fps = pygame.time.Clock()
    dt = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        dt = fps.tick(60) / 1000

        screen.fill((0,0,0))
        pygame.display.flip()
        





if __name__ == "__main__":
    main()
