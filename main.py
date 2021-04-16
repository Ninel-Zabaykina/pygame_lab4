import pygame
from random import randint
from pygame.locals import (
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,
)

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (255,192,203)
running = True


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.width = 75
        self.height = 25
        self.color = (255, 255, 255)

        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        screen.blit(self.surf, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x += randint(-30, 30)
        self.y += randint(-30, 30)
        self.x = min(max(0, self.x), SCREEN_WIDTH)
        self.y = min(max(0, self.y), SCREEN_HEIGHT)
        screen.blit(self.surf, (self.x, self.y))
        pygame.display.flip()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Создаем “поверхность” и передаем ширину и высоту
surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(SCREEN_COLOR)

# Даем ей цвет, чтобы отделить от фона
#surf.fill((0, 0, 0))
#rect = surf.get_rect()

#screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()

new_player = Player()

while running:

    # Посмотрим на все события в очереди
    for event in pygame.event.get():

        # Нажал ли пользователь на клавишу?
        if event.type == KEYDOWN:
            screen.fill(SCREEN_COLOR)
            new_player.move()

            # Это была клавиша ESCAPE? Если да, то останавливаем игру.
            if event.key == K_ESCAPE:
                running = False

                # Нажал ли пользователь на кнопку закрытия окна?
        elif event.type == QUIT:
            running = False






