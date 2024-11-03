import pygame
from static_variables import *
from static_classes import *
from playerFile import Player  # Assuming your Player class is in a file named player.py


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roguelike Game")

clock = pygame.time.Clock()
######################################################
font = pygame.font.Font(None, 100)

def draw_fps_counter():
    """
    Renders the current frames per second (FPS) on the screen using
    the specified font and displays it at the top-left corner of the game screendow.
    """
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, WHITE)
    screen.blit(fps_text, (10, 10))


######################################################
player = Player(player_type=1)  # Pass the appropriate player type here
camera = Camera()
map = WorldMap()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_fps_counter()
    player.update()
    camera.update(player.rect)

    visible_tiles = map.get_background_tiles(player.rect, camera.offset)
    map.render(screen, visible_tiles, camera.offset)

    screen.blit(player.image, camera.apply(player.rect))
    pygame.draw.rect(screen, (0, 255, 0), player.hitbox,2)
    player.load_projectile()



    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame
pygame.quit()