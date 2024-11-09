import pygame
import random
import math
from static_variables import *
from animations import Animation

class Camera:
    def __init__(self):
        self.offset = pygame.Vector2(0, 0)

    def update(self, target_rect):
        # Calculate the offset to keep the target (player) centered
        self.offset.x = target_rect.centerx - WIDTH // 2
        self.offset.y = target_rect.centery - HEIGHT // 2
        
    def apply(self, rect):
        # Return the adjusted position of any rect based on the camera offset
        return rect.move(-self.offset.x, -self.offset.y)
    
class WorldMap:
    def __init__(self):
        self.background_tiles = self.load_background_tiles()
        self.tile_grid = {}

    def load_background_tiles(self):
        background_tiles = []
        for i in range(1,TOTAL_BG+1):
            image = pygame.image.load(f'images/backgrounds/bg-{i}.png').convert()
            image = pygame.transform.scale(image, (WIDTH, HEIGHT))
            background_tiles.append(image)
        return background_tiles
        
    def select_tile_index(self):
        #Selects random tile based on weights
        tiles = list(range(TOTAL_BG))  # Tile indices from 0 to 9
        return random.choices(tiles, weights=BG_CHANCE, k=1)[0]
    
    def get_background_tiles(self, target_rect, camera_offset):
        # Calculate visible tiles based on the player's position and camera offset
        tiles = []

        start_x = int(target_rect.centerx //WIDTH) * WIDTH
        start_y = int(target_rect.centery //HEIGHT) * HEIGHT

        for x in range(start_x - WIDTH, start_x + 2 * WIDTH, WIDTH):
            for y in range(start_y - HEIGHT, start_y + 2 * HEIGHT, HEIGHT):
                grid_x, grid_y = x // WIDTH, y // HEIGHT

                # If tile at (grid_x, grid_y) isn't generated, add it
                if (grid_x, grid_y) not in self.tile_grid:
                    tile_index = self.select_tile_index()
                    self.tile_grid[(grid_x, grid_y)] = tile_index

                tiles.append((x, y, self.tile_grid[(grid_x, grid_y)]))

        return tiles

    def render(self, screen, tiles, camera_offset):
        for tile in tiles:
            x, y, tile_index = tile
            screen_position = pygame.Vector2(x,y) - camera_offset
            screen.blit(self.background_tiles[tile_index], screen_position)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_pos, damage, projectile_type):
        super().__init__()
        self.scale = PLAYER_SCALE // 2
        self.projectile_type = projectile_type
        self.projectile_sheet = self.load_projectile_sheet(self.projectile_type, self.scale)
        
        # single frame of a projectile facing right
        self.base_image = self.create_projectile_image(self.projectile_sheet, self.scale)
        
        # Determine the angle towards the target
        self.pos = pygame.Vector2(x, y)
        self.target_pos = pygame.Vector2(target_pos)
        self.angle = self.calculate_angle_to_target()
        self.image = pygame.transform.rotate(self.base_image, self.angle)  # Rotate image based on angle
        self.rect = self.image.get_rect(center=(x, y))
        
        # Velocity stuff
        self.speed = PROJECTILE_SPEED
        self.velocity = self.calculate_velocity(self.angle)
        
        self.damage = damage
        self.lifespan = 2000
        self.spawn_time = pygame.time.get_ticks()

    def calculate_angle_to_target(self):
        # First we get delta x and delta y, then we use atan2, that calculates arctan in radians and at last we convert radians to degrees
        dx = self.target_pos.x - self.pos.x
        dy = self.target_pos.y - self.pos.y
        return math.degrees(math.atan2(-dy, dx)) # dy is negative because of pygame. Basically the y coordinates are as if they were upside down

    def calculate_velocity(self, angle):
        # Convert angle to radians and calculate velocity vector
        rad_angle = math.radians(angle)
        vx = math.cos(rad_angle) * self.speed
        vy = -math.sin(rad_angle) * self.speed  # Negative vy for pygame's y-axis
        return pygame.Vector2(vx, vy)

    def load_projectile_sheet(self, projectile_type, scale):
        projectile_sheet = pygame.image.load(PROJECTILE_IMAGES[projectile_type]).convert_alpha()
        
        if scale != 1:
            projectile_width, projectile_height = projectile_sheet.get_size()
            scaled_size = (int(projectile_width * scale), int(projectile_height * scale))
            projectile_sheet = pygame.transform.scale(projectile_sheet, scaled_size)
        return projectile_sheet

    def create_projectile_image(self, projectile_sheet, scale):
        # Extract a single frame to use as the base image
        frame_width, frame_height = 48 * scale, 48 * scale
        return projectile_sheet.subsurface((0, 0, frame_width, frame_height))

    def update(self):
        # Update position based on velocity
        self.pos += self.velocity
        self.rect.center = self.pos
        
        # Check lifespan
        if pygame.time.get_ticks() - self.spawn_time > self.lifespan:
            self.kill()  # Remove projectile from all sprite groups