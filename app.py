from string import whitespace
import pygame

pygame.init()
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')
game_over = False

x = 300
y = 300
x1 = 0
y1 = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -10
                y1 = 0
            elif event.key == pygame.K_RIGHT:
                x1 = 10
                y1 = 0
            elif event.key == pygame.K_UP:
                y1 = -10
                x1 = 0
            elif event.key == pygame.K_DOWN:
                y1 = 10
                x1 = 0
    x += x1
    y += y1
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x, y, 10, 10])

    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()
