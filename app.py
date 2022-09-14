import pygame
import time
pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

display_width = 800
display_height = 600
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
game_over = False

x = display_width/2
y = display_height/2
x_change = 0
y_change = 0
snake_size = 10

clock = pygame.time.Clock()
snake_speed = 20

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width/2, display_height/2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_size

    if x >= display_width or x < 0 or y >= display_height or y < 0:
        game_over = True

    x += x_change
    y += y_change
    dis.fill(black)
    pygame.draw.rect(dis, red, [x, y, snake_size, snake_size])

    pygame.display.update()

    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
