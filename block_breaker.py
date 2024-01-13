import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 設定遊戲視窗大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker Game")

# 定義球的屬性
ball_radius = 15
ball_speed = [5, 5]
ball_position = [WIDTH // 2, HEIGHT // 2]

# 定義挡板的屬性
paddle_width, paddle_height = 100, 10
paddle_position = [WIDTH // 2 - paddle_width // 2, HEIGHT - 20]

# 定義方塊的屬性
block_width, block_height = 50, 20
blocks = []
for row in range(5):
    for col in range(WIDTH // block_width):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 設定字體
font = pygame.font.Font(None, 36)

# 遊戲主循環
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_position[0] > 0:
        paddle_position[0] -= 5
    if keys[pygame.K_RIGHT] and paddle_position[0] < WIDTH - paddle_width:
        paddle_position[0] += 5

    # 移動球
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # 碰到左右邊界反彈
    if ball_position[0] <= 0 or ball_position[0] >= WIDTH - ball_radius:
        ball_speed[0] = -ball_speed[0]

    # 碰到上邊界反彈
    if ball_position[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # 球碰到挡板反彈
    if (
        paddle_position[0] < ball_position[0] < paddle_position[0] + paddle_width
        and paddle_position[1] < ball_position[1] + ball_radius < paddle_position[1] + paddle_height
    ):
        ball_speed[1] = -ball_speed[1]

    # 球碰到方塊
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_position[0], ball_position[1], ball_radius * 2, ball_radius * 2)):
            ball_speed[1] = -ball_speed[1]
            blocks.remove(block)

    # 清除畫面
    screen.fill(BLACK)

    # 畫球
    pygame.draw.circle(screen, WHITE, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # 畫挡板
    pygame.draw.rect(screen, WHITE, pygame.Rect(paddle_position[0], paddle_position[1], paddle_width, paddle_height))

    # 畫方塊
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # 繪製得分
    score_text = font.render("Score: {}".format(len(blocks)), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
