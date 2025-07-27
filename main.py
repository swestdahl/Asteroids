import pygame

from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display

    pygame.quit()
    

   

if __name__ == "__main__":
    main()
