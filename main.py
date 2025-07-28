import pygame

from constants import *
from player import Player
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
    score = 0
    lives = 3
    respawn_timer = 0  # Time left for invincibility
    RESPAWN_INVINCIBILITY = 2.0  # seconds
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    AsteroidField()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        dt = clock.tick(60) / 1000.0
        if respawn_timer > 0:
            respawn_timer -= dt

        screen.fill((0, 0, 0))  # Fill the screen with black
        updatable.update(dt)
        
        for thing in drawable:
            if isinstance(thing, Player):
                thing.draw(screen, invincible=respawn_timer > 0)
            else:
                thing.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
                    
                    if asteroid.radius > 30:
                        score += 10
                    elif asteroid.radius > 20:
                        score += 25
                    else:
                        score += 50
        if respawn_timer <= 0:
            for asteroid in asteroids:
                if player.check_collision(asteroid):
                    lives -= 1
                    if lives <= 0:
                        print("Game over!")
                        print(f"Final Score: {score}")
                        running = False
                        break
                    else:
                        # Reset player position and give temporary invincibility
                        player.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                        player.velocity = pygame.Vector2(0, 0)
                        respawn_timer = RESPAWN_INVINCIBILITY
                        break

         # Draw the player on the screen
        font = pygame.font.SysFont(None, 36)
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_text, (10, 40))  # Slightly lower than the score

        pygame.display.flip()  # Update the display
    
    

    pygame.quit()
    

   

if __name__ == "__main__":
    main()
