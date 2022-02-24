import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pong Game")

"""
def ShowScore(text, x, y):
    font = pygame.font.SysFont('freesans', 32)
    msg = font.render(text, True, (255, 0, 0))
    screen.blit(msg, (x, y))
"""


class Ball:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.color = (255, 0, 0)
        self.radius = 20
        self.xmovement = 5
        self.ymovement = 5

    def Display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


ball = Ball()


class Paddle:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.width = 20
        self.height = 200
        self.up = False
        self.down = False
        self.score = 0
        self.speed = 10

    def Display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


p1 = Paddle((0, 255, 0), 10, 200)
p2 = Paddle((0, 0, 255), 570, 200)
direction = random.randint(1, 3)
way = random.randint(1, 2)
while True:
    screen.fill((0, 0, 0))
    ball.Display()
    if ball.y in range(p1.y, p1.y + 200) and ball.x in range(p1.x + 20, p1.x + 40):
        ball.xmovement = -ball.xmovement
    if ball.y in range(p2.y, p2.y + 200) and ball.x + 20 in range(p2.x, p2.x + 20):
        ball.xmovement = -ball.xmovement
    if way == 1:
        if direction == 1:
            ball.x = ball.x + ball.xmovement
            ball.y = ball.y - ball.ymovement
        if direction == 2:
            ball.x = ball.x + ball.xmovement
        if direction == 3:
            ball.x = ball.x + ball.xmovement
            ball.y = ball.y + ball.ymovement
    if way == 2:
        if direction == 1:
            ball.x = ball.x - ball.xmovement
            ball.y = ball.y - ball.ymovement
        if direction == 2:
            ball.x = ball.x - ball.xmovement
        if direction == 3:
            ball.x = ball.x + ball.xmovement
            ball.y = ball.y + ball.ymovement
    if ball.x - 20 <= 0:
        ball.x = 300
        ball.y = 300
        p2.score = p2.score + 1
        print(p1.score, ":", p2.score)
    if ball.x + 20 >= 600:
        ball.x = 300
        ball.y = 300
        p1.score = p1.score + 1
        print(p1.score, ":", p2.score)
    if ball.y - 20 <= 0:
        ball.ymovement = -ball.ymovement
    if ball.y + 20 >= 600:
        ball.ymovement = -ball.ymovement
    p1.Display()
    p2.Display()
    if p1.y <= 0:
        p1.y = 0
    if p1.y + 200 >= 600:
        p1.y = 400
    if p2.y <= 0:
        p2.y = 0
    if p2.y + 200 >= 600:
        p2.y = 400
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                p2.up = True
            if event.key == K_DOWN:
                p2.down = True
            if event.key == K_w:
                p1.up = True
            if event.key == K_s:
                p1.down = True
        elif event.type == KEYUP:
            if event.key == K_UP:
                p2.up = False
            if event.key == K_DOWN:
                p2.down = False
            if event.key == K_w:
                p1.up = False
            if event.key == K_s:
                p1.down = False
    if p2.up == True:
        p2.y = p2.y - p2.speed
    if p2.down == True:
        p2.y = p2.y + p2.speed
    if p1.up == True:
        p1.y = p1.y - p1.speed
    if p1.down == True:
        p1.y = p1.y + p1.speed
        """
    ShowScore(str(p1.score), 20, 20)
    ShowScore(str(p2.score), 560, 20)
    """
    pygame.display.update()
