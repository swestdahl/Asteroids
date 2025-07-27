import pygame

from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, shots)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    pygame.time.Clock().tick(60)
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    AsteroidField()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        dt = clock.tick(60) / 1000.0
        screen.fill((0, 0, 0))  # Fill the screen with black
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                running = False
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        for thing in drawable:
            thing.draw(screen)  # Draw the player on the screen
        pygame.display.flip()  # Update the display
    
    

    pygame.quit()
    

   

if __name__ == "__main__":
    main()
