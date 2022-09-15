import pygame
import time
import random

pygame.init()

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

display_width = 600
display_height = 400

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_size, snake_list):
    for mun in snake_list:
        pygame.draw.rect(dis, red, [mun[0], mun[1], snake_size, snake_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width/20, display_height/3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2

    x_change = 0
    y_change = 0
    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(
        0, display_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(
        0, display_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            message("You Lost! Press Q - Quit or C - Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x_change
        y1 += y_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)

        if len(snake_List) > length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_head:
                print("here")
                game_close = True
        our_snake(snake_size, snake_List)
        display_score(length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, display_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(
                0, display_height - snake_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop()
