import pygame
import os

pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "Caçador de Deuses"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
ICON_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))
RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

SHIELD_SOUND= pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/dead.wav'))
HAMMER_SOUND= pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/HammerSound.wav'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/jump.wav'))
END_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/dead.wav'))
HIT_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/hit.wav'))
BACKGROUND_SOUND = pygame.mixer.music.load(os.path.join(IMG_DIR, 'Sounds/moonleap.mp3'))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")).convert_alpha(),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png")).convert_alpha()
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png")).convert_alpha()
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png")).convert_alpha()

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")).convert_alpha(),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")).convert_alpha(),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")).convert_alpha(),
]

BIRD_SPRITE = pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird.png")).convert_alpha()
BIRD = []
for i in range(4):
    img = BIRD_SPRITE.subsurface((i * 45, 0),(45, 30))
    img = pygame.transform.scale(img, (45 * 2, 30* 2))
    BIRD.append(img)

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')).convert_alpha()
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png')).convert_alpha()
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')).convert_alpha()
DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png")).convert_alpha()

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png')).convert_alpha()
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax.png')).convert_alpha()
BG3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax2.png')).convert_alpha()
BG4 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax3.png')).convert_alpha()
BG5 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax4.png')).convert_alpha()

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/MenuGame.png')).convert_alpha()

DEFAULT_TYPE = "default"

SHIELD_TYPE = "shield"

HAMMER_TYPE = "martelo divino"

SHIELD_TYPE = "poder divino"

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
AQUAMARINE = (127,255,212)
CHOCOLATE = (210,105,30)
RED = (255,0,0)