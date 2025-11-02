import pygame
import random

# Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cashflow Runner")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Игрок
player_img = pygame.Surface((50, 50))
player_img.fill(GREEN)
player_rect = player_img.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_speed = 5

# Монеты
coin_img = pygame.Surface((20, 20))
coin_img.fill((255, 215, 0))
coins = [pygame.Rect(random.randint(0, WIDTH-20), random.randint(0, HEIGHT-20), 20, 20) for _ in range(5)]

# Счёт
score = 0
font = pygame.font.SysFont(None, 36)

# Игровой цикл
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    win.fill(WHITE)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Движение
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]: player_rect.x += player_speed
    if keys[pygame.K_UP]: player_rect.y -= player_speed
    if keys[pygame.K_DOWN]: player_rect.y += player_speed

    # Столкновение с монетами
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 10

    # Отрисовка
    win.blit(player_img, player_rect)
    for coin in coins:
        win.blit(coin_img, coin)
    score_text = font.render(f"Капитал: ${score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
