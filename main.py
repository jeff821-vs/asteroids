import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

# Things I want to add: ship acceleration, power-ups (shield, different weapon(s)), sound effects

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    GAME_FONT = pygame.font.SysFont("comicsansms.ttf", 40)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    
    score = 0
    lives = 3
    timer = TIMER_COOLDOWN
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))
        fps.tick(60)
        dt = (fps.get_time() / 1000)
        score_text = GAME_FONT.render(f"Score: {score}", True, (25, 10, 245))
        lives_text = GAME_FONT.render(f"Lives left: {lives}", True, (227, 9, 9))
        screen.blit(score_text, (35, 40))
        screen.blit(lives_text, (35, 80))
        timer -= dt
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collisions(player) == True:
                if timer <= 0:
                    lives -= 1
                    timer = TIMER_COOLDOWN
                if lives == 0:
                    exit("Game over!")
            for shot in shots:
                if shot.collisions(asteroid) == True:
                    shot.kill()
                    asteroid.split()
                    score += 50

        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
