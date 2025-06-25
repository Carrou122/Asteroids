import pygame
import sys
import time
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont("monospace", 75)
    game_over_text = my_font.render("Game Over", True, (255, 0, 0))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    x_centered = x - (game_over_text.get_width()/2)
    y_centered = y - (game_over_text.get_height()/2)

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            
        dt = (clock.tick(60)/1000)
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid) is True:
                screen.blit(game_over_text, (x_centered, y_centered))
                pygame.display.flip()
                time.sleep(1/2)
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        
    
    
if __name__ == "__main__":
    
    main()
