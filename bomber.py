import pygame
import os
# çalıştırmak için textureları eklemen lazım


pygame.init()


def x_checker(start, end, current_x):
    if start <= current_x and end >= current_x:
        return True
    else:
        return False


def y_checker(start, end, current_y):
    if start <= current_y and end >= current_y:
        return True
    else:
        return False


def rect_hitbox(start_x, end_x, start_y, end_y, target_x, target_y, mode, game_screen):
    mode = int(mode)
    if mode == 1:
        # filled
        pygame.draw.rect(game_screen, (255, 255, 255), (start_x, start_y, (end_x - start_x), (end_y - start_y)), 0)
    elif mode == 2:
        # not filled
        pygame.draw.rect(game_screen, (255, 255, 255), (start_x, start_y, (end_x - start_x), (end_y - start_y)), 1)

    if x_checker(start_x, end_x, target_x) and y_checker(start_y, end_y, target_y):
        return True
    else:
        return False


def message(msg, screen, bg_color, msg_color, loc, font_size):  # bg = background
    message_font = pygame.font.SysFont("Arial", font_size)
    message_text = message_font.render(msg, False, msg_color)
    for wait in range(4000):
        screen.fill(bg_color)
        screen.blit(message_text, loc)
        pygame.display.update()


main = os.getcwd()

char_img = pygame.image.load(f"{main}\\bomber.png")
build1_img = pygame.image.load(f"{main}\\building1.png")
build2_img = pygame.image.load(f"{main}\\building2.png")
park_img = pygame.image.load(f"{main}\\park.png")

window = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Bomber")
clock = pygame.time.Clock()
run = True

# character
char_x = -10
char_y = 0
char_width = 140
char_length = 32
speed = 3

# bombs
# bomb1
gravity = 3
bomb1X = 0
bomb1Y = 0
bomb1_fired = False
# bomb2
bomb2X = 0
bomb2Y = 0
bomb2_fired = False
# bomb3
bomb3X = 0
bomb3Y = 0
bomb3_fired = False

light_green = (99, 255, 45)
green = (0, 142, 15)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (100, 100, 100)
light_blue = (0, 142, 234)

score = 0

building1 = 8
building2 = 6
building3 = 7
building4 = 5
building5 = 7

bomb_amount = 3
win = False
park = True

message("Game by Overload Inc.", window, black, white, (300, 270), 35)

while run is True:
    main_font = pygame.font.SysFont("Arial", 11)
    score_text = main_font.render("Score: {0}".format(score), False, white)
    alt_text = main_font.render("Altitude: {0}ft".format(600 - (char_y + 16)), False, white)
    nose_pointX = char_x + char_width
    nose_pointY = char_y + (char_length / 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bomb1_fired is True and bomb2_fired is True and bomb3_fired is False\
                    and bomb_amount != 0:
                bomb3X = char_x + (char_width / 2)
                bomb3Y = char_y + char_length
                bomb3_fired = True
                bomb_amount -= 1
            if event.key == pygame.K_SPACE and bomb1_fired is True and bomb2_fired is False and bomb_amount != 0:
                bomb2X = char_x + (char_width / 2)
                bomb2Y = char_y + char_length
                bomb2_fired = True
                bomb_amount -= 1
            if event.key == pygame.K_SPACE and bomb1_fired is False and bomb_amount != 0:
                bomb1X = char_x + (char_width / 2)
                bomb1Y = char_y + char_length
                bomb1_fired = True
                bomb_amount -= 1
            if event.key == pygame.K_ESCAPE:
                run = False

    # display
    window.fill(light_blue)
    pygame.draw.rect(window, green, (0, 500, 905, 105), 0)
    window.blit(char_img, (char_x, char_y))
    char_x += speed

    # bombs
    if bomb1_fired is True:
        bomb1Y += gravity
        pygame.draw.circle(window, black, (int(bomb1X), int(bomb1Y)), 4, 0)
    if bomb2_fired is True:
        bomb2Y += gravity
        pygame.draw.circle(window, black, (int(bomb2X), int(bomb2Y)), 4, 0)
    if bomb3_fired is True:
        bomb3Y += gravity
        pygame.draw.circle(window, black, (int(bomb3X), int(bomb3Y)), 4, 0)

    # skybox
    if rect_hitbox(0, 900, 500, 600, bomb1X, bomb1Y, 0, window):
        bomb1_fired = False
        bomb1X = 0
        bomb1Y = 0
    if rect_hitbox(0, 900, 500, 600, bomb2X, bomb2Y, 0, window):
        bomb2_fired = False
        bomb2X = 0
        bomb2Y = 0
    if rect_hitbox(0, 900, 500, 600, bomb3X, bomb3Y, 0, window):
        bomb3_fired = False
        bomb3X = 0
        bomb3Y = 0

    if rect_hitbox(900, 1000, 0, 600, char_x, char_y, 0, window):
        char_x = -10
        char_y += 30
        bomb_amount = 3

    # building1
    if building1 > 0:
        if building1 >= 1:
            window.blit(build1_img, (100, 476))
        if building1 >= 2:
            window.blit(build1_img, (100, 452))
        if building1 >= 3:
            window.blit(build1_img, (100, 428))
        if building1 >= 4:
            window.blit(build1_img, (100, 404))
        if building1 >= 5:
            window.blit(build1_img, (100, 380))
        if building1 >= 6:
            window.blit(build1_img, (100, 356))
        if building1 >= 7:
            window.blit(build1_img, (100, 332))
        if building1 == 8:
            window.blit(build1_img, (100, 308))

    if rect_hitbox(98, 174, 476 - ((building1 - 1) * 24), 500, bomb1X, bomb1Y, 0, window):
        building1 -= 1
        bomb1_fired = False
        bomb1X = 0
        bomb1Y = 0
        score += 200
    if rect_hitbox(98, 174, 476 - ((building1 - 1) * 24), 500, bomb2X, bomb2Y, 0, window):
        building1 -= 1
        bomb2_fired = False
        bomb2X = 0
        bomb2Y = 0
        score += 200
    if rect_hitbox(98, 174, 476 - ((building1 - 1) * 24), 500, bomb3X, bomb3Y, 0, window):
        building1 -= 1
        bomb3_fired = False
        bomb3X = 0
        bomb3Y = 0
        score += 200

    # building2
    if building2 > 0:
        if building2 >= 1:
            window.blit(build1_img, (220, 476))
        if building2 >= 2:
            window.blit(build1_img, (220, 452))
        if building2 >= 3:
            window.blit(build1_img, (220, 428))
        if building2 >= 4:
            window.blit(build1_img, (220, 404))
        if building2 >= 5:
            window.blit(build1_img, (220, 380))
        if building2 == 6:
            window.blit(build1_img, (220, 356))

    if rect_hitbox(218, 294, 476 - ((building2 - 1) * 24), 500, bomb1X, bomb1Y, 0, window):
        building2 -= 1
        bomb1_fired = False
        bomb1X = 0
        bomb1Y = 0
        score += 200
    if rect_hitbox(218, 294, 476 - ((building2 - 1) * 24), 500, bomb2X, bomb2Y, 0, window):
        building2 -= 1
        bomb2_fired = False
        bomb2X = 0
        bomb2Y = 0
        score += 200
    if rect_hitbox(218, 294, 476 - ((building2 - 1) * 24), 500, bomb3X, bomb3Y, 0, window):
        building2 -= 1
        bomb3_fired = False
        bomb3X = 0
        bomb3Y = 0
        score += 200

    # building3
    if building3 > 0:
        if building3 >= 1:
            window.blit(build2_img, (340, 476))
        if building3 >= 2:
            window.blit(build2_img, (340, 452))
        if building3 >= 3:
            window.blit(build2_img, (340, 428))
        if building3 >= 4:
            window.blit(build2_img, (340, 404))
        if building3 >= 5:
            window.blit(build2_img, (340, 380))
        if building3 >= 6:
            window.blit(build2_img, (340, 356))
        if building3 == 7:
            window.blit(build2_img, (340, 332))

    if rect_hitbox(338, 414, 476 - ((building3 - 1) * 24), 500, bomb1X, bomb1Y, 0, window):
        building3 -= 1
        bomb1_fired = False
        bomb1X = 0
        bomb1Y = 0
        score += 200
    if rect_hitbox(338, 414, 476 - ((building3 - 1) * 24), 500, bomb2X, bomb2Y, 0, window):
        building3 -= 1
        bomb2_fired = False
        bomb2X = 0
        bomb2Y = 0
        score += 200
    if rect_hitbox(338, 414, 476 - ((building3 - 1) * 24), 500, bomb3X, bomb3Y, 0, window):
        building3 -= 1
        bomb3_fired = False
        bomb3X = 0
        bomb3Y = 0
        score += 200

    # building4
    if building4 > 0:
        if building4 >= 1:
            window.blit(build1_img, (460, 476))
        if building4 >= 2:
            window.blit(build1_img, (460, 452))
        if building4 >= 3:
            window.blit(build1_img, (460, 428))
        if building4 >= 4:
            window.blit(build1_img, (460, 404))
        if building4 == 5:
            window.blit(build1_img, (460, 380))

    if rect_hitbox(458, 534, 476 - ((building4 - 1) * 24), 500, bomb1X, bomb1Y, 0, window):
        building4 -= 1
        bomb1_fired = False
        bomb1X = 0
        bomb1Y = 0
        score += 200
    if rect_hitbox(458, 534, 476 - ((building4 - 1) * 24), 500, bomb2X, bomb2Y, 0, window):
        building4 -= 1
        bomb2_fired = False
        bomb2X = 0
        bomb2Y = 0
        score += 200
    if rect_hitbox(458, 534, 476 - ((building4 - 1) * 24), 500, bomb3X, bomb3Y, 0, window):
        building4 -= 1
        bomb3_fired = False
        bomb3X = 0
        bomb3Y = 0
        score += 200

    # building5
    if building5 > 0:
        if building5 >= 1:
            window.blit(build2_img, (580, 476))
        if building5 >= 2:
            window.blit(build2_img, (580, 452))
        if building5 >= 3:
            window.blit(build2_img, (580, 428))
        if building5 >= 4:
            window.blit(build2_img, (580, 404))
        if building5 >= 5:
            window.blit(build2_img, (580, 380))
        if building5 >= 6:
            window.blit(build2_img, (580, 356))
        if building5 == 7:
            window.blit(build2_img, (580, 332))

    if rect_hitbox(578, 654, 476 - ((building5 - 1) * 24), 500, bomb1X, bomb1Y, 0, window):
        building5 -= 1
        bomb1_fired = False
        bomb1X = 0
        bomb1Y = 0
        score += 200
    if rect_hitbox(578, 654, 476 - ((building5 - 1) * 24), 500, bomb2X, bomb2Y, 0, window):
        building5 -= 1
        bomb2_fired = False
        bomb2X = 0
        bomb2Y = 0
        score += 200
    if rect_hitbox(578, 654, 476 - ((building5 - 1) * 24), 500, bomb3X, bomb3Y, 0, window):
        building5 -= 1
        bomb3_fired = False
        bomb3X = 0
        bomb3Y = 0
        score += 200

    # park
    if park is True:
        window.blit(park_img, (660, 458))
        if rect_hitbox(660, 777, 459, 500, bomb1X, bomb1Y, 0, window):
            park = False
            bomb1_fired = False
            bomb1X = 0
            bomb1Y = 0
            score += 500
        if rect_hitbox(660, 777, 459, 500, bomb2X, bomb2Y, 0, window):
            park = False
            bomb2_fired = False
            bomb2X = 0
            bomb2Y = 0
            score += 500
        if rect_hitbox(660, 777, 459, 500, bomb3X, bomb3Y, 0, window):
            park = False
            bomb3_fired = False
            bomb3X = 0
            bomb3Y = 0
            score += 500

    if bomb_amount >= 3:
        pygame.draw.rect(window, grey, (70, 530, 15, 15), 0)
    if bomb_amount >= 2:
        pygame.draw.rect(window, grey, (45, 530, 15, 15), 0)
    if bomb_amount >= 1:
        pygame.draw.rect(window, grey, (20, 530, 15, 15), 0)

    window.blit(score_text, (830, 10))
    window.blit(alt_text, (830, 20))
    pygame.display.update()
    clock.tick(60)

    # Death
    if rect_hitbox(98, 174, 476 - ((building1 - 1) * 24), 500, nose_pointX, nose_pointY, 0, window):
        run = False
    if rect_hitbox(218, 294, 476 - ((building2 - 1) * 24), 500, nose_pointX, nose_pointY, 0, window):
        run = False
    if rect_hitbox(338, 414, 476 - ((building3 - 1) * 24), 500, nose_pointX, nose_pointY, 0, window):
        run = False
    if rect_hitbox(458, 534, 476 - ((building4 - 1) * 24), 500, nose_pointX, nose_pointY, 0, window):
        run = False
    if rect_hitbox(578, 654, 476 - ((building5 - 1) * 24), 500, nose_pointX, nose_pointY, 0, window):
        run = False

    if rect_hitbox(98, 174, 476 - ((building1 - 1) * 24), 500, char_x + (char_width / 2), char_y + char_length, 0,
                   window):
        run = False
    if rect_hitbox(218, 294, 476 - ((building2 - 1) * 24), 500, char_x + (char_width / 2), char_y + char_length, 0,
                   window):
        run = False
    if rect_hitbox(338, 414, 476 - ((building3 - 1) * 24), 500, char_x + (char_width / 2), char_y + char_length, 0,
                   window):
        run = False
    if rect_hitbox(458, 534, 476 - ((building4 - 1) * 24), 500, char_x + (char_width / 2), char_y + char_length, 0,
                   window):
        run = False
    if rect_hitbox(578, 654, 476 - ((building5 - 1) * 24), 500, char_x + (char_width / 2), char_y + char_length, 0,
                   window):
        run = False

    if building1 <= 0 and building2 <= 0 and building3 <= 0 and building4 <= 0 and building5 <= 0 and park is False:
        win = True
    if win is True:
        run = False

for i in range(800):
    if win is True:
        window.fill(black)
        font2 = pygame.font.SysFont("Arial", 50)
        text8 = font2.render("YOU WIN", False, light_green)
        window.blit(text8, (350, 280))
        pygame.display.update()
    else:
        window.fill(black)
        font2 = pygame.font.SysFont("Arial", 50)
        text8 = font2.render("YOU LOSE", False, red)
        window.blit(text8, (340, 280))
        pygame.display.update()
pygame.quit()
quit()
