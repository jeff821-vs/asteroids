import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        fps.tick(60)
        dt = (fps.get_time() / 1000)
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
