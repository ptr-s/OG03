import pygame
import random
from config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/shooter-art.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

target_image = pygame.image.load("images/apple70.png")
target_width = 70
target_height = 70
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
# Начальные параметры движения
velocity_x = random.choice([-3, 3])  # Случайная скорость по оси X
velocity_y = random.choice([-3, 3])  # Случайная скорость по оси Y

# Загрузка изображения прицела
crosshair_image = pygame.image.load("images/crosshair70b.png")
crosshair_width = 70
crosshair_height = 70
pygame.mouse.set_visible(False)

screen_color = (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))
pygame.font.init()
score_font = pygame.font.Font(None, 36)

score = 0  # Переменная для хранения очков

running = True
while running:
    clock.tick(FPS)

    screen.fill(screen_color)

    # Отображение цели
    target_x += velocity_x
    target_y += velocity_y

    # Проверка на границы экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        velocity_x *= -1  # Изменяем направление по оси X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        velocity_y *= -1  # Изменяем направление по оси Y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет при попадании
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                velocity_x = random.choice([-3, 3])  # Сброс скорости
                velocity_y = random.choice([-3, 3])  # Сброс скорости

    # Отрисовка цели
    screen.blit(target_image, (int(target_x), int(target_y)))

    # Отображение счета в правом верхнем углу
    score_text = score_font.render(f'Счет: {score}', True, (255, 255, 255))  # Белый цвет текста
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))  # Отображаем текст с отступом

    # Отображаем прицел
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем текущие координаты мыши
    screen.blit(crosshair_image, (mouse_x - crosshair_width // 2, mouse_y - crosshair_height // 2))

    pygame.display.update()

pygame.quit()
