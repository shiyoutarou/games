import random
import sys

import pygame
from pygame.math import Vector2

# 初始化 Pygame
pygame.init()

# 定義常數和變數
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)

# 定義 Snake 和 Food 類


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 5)]
        self.direction = RIGHT

    def move(self):
        new_head = self.body[0] + self.direction
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        new_head = self.body[0] + self.direction
        self.body.insert(0, new_head)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment.x * GRID_SIZE,
                             segment.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


class Food:
    def __init__(self):
        self.position = self.randomize()

    def randomize(self):
        return Vector2(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.position.x * GRID_SIZE,
                         self.position.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# 創建 Snake 和 Food 物件
snake = Snake()
food = Food()

# 設定視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# 遊戲迴圈
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = UP
            elif event.key == pygame.K_DOWN:
                snake.direction = DOWN
            elif event.key == pygame.K_LEFT:
                snake.direction = LEFT
            elif event.key == pygame.K_RIGHT:
                snake.direction = RIGHT

    # 更新遊戲邏輯
    snake.move()

    # 檢查是否吃到食物
    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.randomize()

    # 清除畫面
    screen.fill((0, 0, 0))

    # 繪製 Snake 和 Food
    snake.draw()
    food.draw()

    # 更新視窗
    pygame.display.update()

    # 控制遊戲速度
    clock.tick(10)
