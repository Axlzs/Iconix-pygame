import pygame 

WIDTH, HEIGHT = 1000, 700
BACKGROUND_WIDTH, BACKGROUND_HEIGHT = 100, 100 # Black background size (UNUSED!!)
FPS = 60 # Framerate value for game
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
MAX_ARROWS = 10 # Max arrows on screen at a time 
last_shot_time = 0 # Needed to time arrow shots
ARROW_SPEED = 7
enemy_speed_linear = 2
enemy_speed_diagonal = 1.414

############MAP_DATA############
TOTAL_BG = 10
BG_CHANCE = [40] + [10] * 4 + [7] * 2 + [3] * 3 # Change probabilities for each image if needed!
###############################

#############ENEMY#############
ENEMY_SPAWN_AREA = 200 # Density - distance between inner spawn circle and outer spawn circe 
ENEMY_SPAWN_DISTANCE = 200 # How far does the enemy spawn form the player
#ENEMY_HEALTH = {1: 50, 2: 100, 3: 150}  # Health for each enemy type
ENEMY_HEALTH = {1: 29, 2: 29, 3: 29}  # Health for each enemy type
ENEMY_HIT_EVENTS = {1: pygame.USEREVENT + 2, 2: pygame.USEREVENT + 3, 3: pygame.USEREVENT + 4}# hit by enemy 
BASE_ENEMY_EVENT_ID = pygame.USEREVENT + 5

#PLAYER_MELE_HIT = pygame.USEREVENT + 5
ENEMY_SIZE = (48,48)
#ENEMY_HITBOX = (70, 70)
ENEMY_IMAGES = {
    1: 'images/enemies/enemy1.png',
    2: 'images/enemies/enemy2.png',
    3: 'images/enemies/enemy3.png'}
ENEMY_ANIMATION_SPEED = 100  # Milliseconds per frame
ENEMY_DAMAGE = {1: 0, 2: 0, 3: 0 }
#ENEMY_DAMAGE = {1: 1, 2: 1.5, 3: 2 }
###############################

############PLAYER############\
SPEED_LINEAR = 4
SPEED_DIAGONAL = 2.828 # Coefficient 0.707 in regards to linear SPEEDSPEED = 4
PLAYER_SCALE = 2 # Scale player
DEFAULT_PLAYER = (48,48)
PLAYER_IMAGES = {
    1: 'images/players/player1.png',
    2: 'images/players/player1.png',
    3: ''
}

HITBOX_WIDTH = 16
HITBOX_HEIGHT = 28 
COOLDOWNS = {'movement':100,'shoot':100}
PLAYER_HEALTH = {1: 50, 2: 100, 3: 300}
PLAYER_ATTACK = {1:1}
PLAYER_DAMAGE = {1: 0.8, 2: 0.6, 3: 1}
PLAYER_HIT_EVENTS = {1: pygame.USEREVENT + 5, 2: pygame.USEREVENT + 6}
##########ATTACKS##############
PROJECTILE_IMAGES = {
    1:'images/projectiles/iron arrow.png',
    2:'images/projectiles/iron arrow.png'
}
PROJECILE_SPEED = 5
PROJECTILE_COOLDOWN = 600
###############################


###########SOME#COLOURS###########
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
MAGENTA, YELLOW = (255, 0, 255), (255, 255, 0)