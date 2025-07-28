import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Player's rotation angle
        self.timer = 0  # Cooldown timer for shooting
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
    def draw(self, screen, invincible=False):
    # Draw shield first (under the ship)
        if invincible:
            pygame.draw.circle(
                screen,
                (0, 150, 255),  # Blue shield color
                (int(self.position.x), int(self.position.y)),
                int(self.radius * 1.5),
                2  # Thin outline
            )

        # Always draw the ship in white
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()      
    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += direction * PLAYER_SPEED * dt
        elif keys[pygame.K_s]:
            direction = pygame.Vector2(0, -1).rotate(self.rotation)
            self.position += direction * PLAYER_SPEED * dt
        self.position.x = max(0, min(SCREEN_WIDTH, self.position.x))
        self.position.y = max(0, min(SCREEN_HEIGHT, self.position.y))
    def shoot(self):
        if self.timer > 0:
            return # Cooldown not finished
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        Shot(self.position.x, self.position.y, velocity)
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        
                  