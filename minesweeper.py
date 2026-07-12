import random
import pygame
import sys
import time
from pygame.constants import MOUSEBUTTONDOWN
import asyncio
on = True
pygame.display.set_caption('Minesweeper')
while True:
    nada = True
    clock = pygame.time.Clock()
    game_time = 0
    next_tick = pygame.time.get_ticks() + 1000
    flags = 20
    if not on:
        time.sleep(2)
    flag_image = pygame.image.load('flag.png')
    flag_image = pygame.transform.scale(flag_image, (58,58))
    pygame.init()
    bombes = ['■'] * 20 + ['□'] * 80
    random.shuffle(bombes)
    cords_if_bomb = {}
    for y in range(10):
        for x in range(10):
            cords_if_bomb[str(x) + '_' + str(y)] = bombes[y*10 + x]
    for cords in cords_if_bomb.keys():
        current_cell_bomb_count = 0
        if cords_if_bomb[cords] == '■':continue
        cord = list(cords)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if -1 < (int(cord[0]) + dx) < 10 and -1 < (int(cord[2]) + dy) < 10:
                    if cords_if_bomb[str(int(cord[0]) + dx) + '_' + str(int(cord[2]) + dy)] == '■': current_cell_bomb_count += 1
        if current_cell_bomb_count == 0:
            cords_if_bomb[cords] = '0'
            continue
        cords_if_bomb[cords] = current_cell_bomb_count
    flagged = {}
    width = 600
    height = 700
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 24)
    num_font = pygame.font.SysFont("Arial", 40)
    dead_font = pygame.font.SysFont("Arial", 80)
    opened_cells = []
    rects = {
        #y0
        'rect0_0':pygame.Rect(1,height-59,58,58),
        'rect1_0':pygame.Rect(61,height-59,58,58),
        'rect2_0':pygame.Rect(121,height-59,58,58),
        'rect3_0':pygame.Rect(181,height-59,58,58),
        'rect4_0':pygame.Rect(241,height-59,58,58),
        'rect5_0':pygame.Rect(301,height-59,58,58),
        'rect6_0':pygame.Rect(361,height-59,58,58),
        'rect7_0':pygame.Rect(421,height-59,58,58),
        'rect8_0':pygame.Rect(481,height-59,58,58),
        'rect9_0':pygame.Rect(541,height-59,58,58),
        #y1
        'rect0_1':pygame.Rect(1,height-119,58,58),
        'rect1_1':pygame.Rect(61,height-119,58,58),
        'rect2_1':pygame.Rect(121,height-119,58,58),
        'rect3_1':pygame.Rect(181,height-119,58,58),
        'rect4_1':pygame.Rect(241,height-119,58,58),
        'rect5_1':pygame.Rect(301,height-119,58,58),
        'rect6_1':pygame.Rect(361,height-119,58,58),
        'rect7_1':pygame.Rect(421,height-119,58,58),
        'rect8_1':pygame.Rect(481,height-119,58,58),
        'rect9_1':pygame.Rect(541,height-119,58,58),
        #y2
        'rect0_2':pygame.Rect(1,height-179,58,58),
        'rect1_2':pygame.Rect(61,height-179,58,58),
        'rect2_2':pygame.Rect(121,height-179,58,58),
        'rect3_2':pygame.Rect(181,height-179,58,58),
        'rect4_2':pygame.Rect(241,height-179,58,58),
        'rect5_2':pygame.Rect(301,height-179,58,58),
        'rect6_2':pygame.Rect(361,height-179,58,58),
        'rect7_2':pygame.Rect(421,height-179,58,58),
        'rect8_2':pygame.Rect(481,height-179,58,58),
        'rect9_2':pygame.Rect(541,height-179,58,58),
        #y3
        'rect0_3':pygame.Rect(1,height-239,58,58),
        'rect1_3':pygame.Rect(61,height-239,58,58),
        'rect2_3':pygame.Rect(121,height-239,58,58),
        'rect3_3':pygame.Rect(181,height-239,58,58),
        'rect4_3':pygame.Rect(241,height-239,58,58),
        'rect5_3':pygame.Rect(301,height-239,58,58),
        'rect6_3':pygame.Rect(361,height-239,58,58),
        'rect7_3':pygame.Rect(421,height-239,58,58),
        'rect8_3':pygame.Rect(481,height-239,58,58),
        'rect9_3':pygame.Rect(541,height-239,58,58),
        #y4
        'rect0_4':pygame.Rect(1,height-299,58,58),
        'rect1_4':pygame.Rect(61,height-299,58,58),
        'rect2_4':pygame.Rect(121,height-299,58,58),
        'rect3_4':pygame.Rect(181,height-299,58,58),
        'rect4_4':pygame.Rect(241,height-299,58,58),
        'rect5_4':pygame.Rect(301,height-299,58,58),
        'rect6_4':pygame.Rect(361,height-299,58,58),
        'rect7_4':pygame.Rect(421,height-299,58,58),
        'rect8_4':pygame.Rect(481,height-299,58,58),
        'rect9_4':pygame.Rect(541,height-299,58,58),
        #y5
        'rect0_5':pygame.Rect(1,height-359,58,58),
        'rect1_5':pygame.Rect(61,height-359,58,58),
        'rect2_5':pygame.Rect(121,height-359,58,58),
        'rect3_5':pygame.Rect(181,height-359,58,58),
        'rect4_5':pygame.Rect(241,height-359,58,58),
        'rect5_5':pygame.Rect(301,height-359,58,58),
        'rect6_5':pygame.Rect(361,height-359,58,58),
        'rect7_5':pygame.Rect(421,height-359,58,58),
        'rect8_5':pygame.Rect(481,height-359,58,58),
        'rect9_5':pygame.Rect(541,height-359,58,58),
        #y6
        'rect0_6':pygame.Rect(1,height-419,58,58),
        'rect1_6':pygame.Rect(61,height-419,58,58),
        'rect2_6':pygame.Rect(121,height-419,58,58),
        'rect3_6':pygame.Rect(181,height-419,58,58),
        'rect4_6':pygame.Rect(241,height-419,58,58),
        'rect5_6':pygame.Rect(301,height-419,58,58),
        'rect6_6':pygame.Rect(361,height-419,58,58),
        'rect7_6':pygame.Rect(421,height-419,58,58),
        'rect8_6':pygame.Rect(481,height-419,58,58),
        'rect9_6':pygame.Rect(541,height-419,58,58),
        #y7
        'rect0_7':pygame.Rect(1,height-479,58,58),
        'rect1_7':pygame.Rect(61,height-479,58,58),
        'rect2_7':pygame.Rect(121,height-479,58,58),
        'rect3_7':pygame.Rect(181,height-479,58,58),
        'rect4_7':pygame.Rect(241,height-479,58,58),
        'rect5_7':pygame.Rect(301,height-479,58,58),
        'rect6_7':pygame.Rect(361,height-479,58,58),
        'rect7_7':pygame.Rect(421,height-479,58,58),
        'rect8_7':pygame.Rect(481,height-479,58,58),
        'rect9_7':pygame.Rect(541,height-479,58,58),
        #y8
        'rect0_8':pygame.Rect(1,height-539,58,58),
        'rect1_8':pygame.Rect(61,height-539,58,58),
        'rect2_8':pygame.Rect(121,height-539,58,58),
        'rect3_8':pygame.Rect(181,height-539,58,58),
        'rect4_8':pygame.Rect(241,height-539,58,58),
        'rect5_8':pygame.Rect(301,height-539,58,58),
        'rect6_8':pygame.Rect(361,height-539,58,58),
        'rect7_8':pygame.Rect(421,height-539,58,58),
        'rect8_8':pygame.Rect(481,height-539,58,58),
        'rect9_8':pygame.Rect(541,height-539,58,58),
        #y9
        'rect0_9':pygame.Rect(1,height-599,58,58),
        'rect1_9':pygame.Rect(61,height-599,58,58),
        'rect2_9':pygame.Rect(121,height-599,58,58),
        'rect3_9':pygame.Rect(181,height-599,58,58),
        'rect4_9':pygame.Rect(241,height-599,58,58),
        'rect5_9':pygame.Rect(301,height-599,58,58),
        'rect6_9':pygame.Rect(361,height-599,58,58),
        'rect7_9':pygame.Rect(421,height-599,58,58),
        'rect8_9':pygame.Rect(481,height-599,58,58),
        'rect9_9':pygame.Rect(541,height-599,58,58)

    }
    for numb in range(100):
        cur_num = f'{numb:02}'
        col_num = int(cur_num[0]) * 9 + int(cur_num[1])
        color = (0, 130, 0) if col_num % 2 == 0 else (0, 180, 0)
        cur_rect = 'rect' + cur_num[1] + '_' + cur_num[0]
        if cur_rect in rects:
            pygame.draw.rect(screen, color, rects[cur_rect])
    def chek_around(cell):
        x, y = cell.split('_')
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                cx,cy = int(x)+dx, int(y)+dy
                if -1 < cx < 10 and -1 < cy < 10:
                    if f'{cx}_{cy}' not in opened_cells:
                        opened_cells.append(f'{cx}_{cy}')
    on = True
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, 100))
    screen.blit(font.render(f'There are {flags} flags left',True,(255,255,255)),(20,50))
    screen.blit(font.render(f'Game time: {game_time}', True, (255, 255, 255)), (300, 50))
    while on:
        current_time = pygame.time.get_ticks()
        if current_time >= next_tick:
            game_time += 1
            pygame.draw.rect(screen,(0,0,0),(300,0,300,100))
            screen.blit(font.render(f'Game time: {game_time}',True,(255,255,255)),(300,50))
            next_tick = current_time + 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mouse.get_pos()
                    for key in rects:#key = rectx_y
                        if rects[key].collidepoint(event.pos):
                            if key not in flagged:
                                cordinata = f'{key.strip('rect'):02}'#cordinata = x_y
                                if cords_if_bomb[cordinata] == '■':
                                    for numb in range(100):
                                        cur_num = f'{numb:02}'
                                        col_num = int(cur_num[0]) * 9 + int(cur_num[1])
                                        color = (0, 130, 0) if col_num % 2 == 0 else (0, 180, 0)
                                        cur_rect = 'rect' + cur_num[1] + '_' + cur_num[0]
                                        if cur_rect in rects:
                                            pygame.draw.rect(screen, color, rects[cur_rect])
                                    for x in range(0, width + 1, 60):
                                        pygame.draw.line(screen, (0, 0, 0), (x, 100), (x, height), 3)
                                    for y in range(0, height, 60):
                                        pygame.draw.line(screen, (0, 0, 0), (0, 100 + y), (width, 100 + y), 3)
                                    pygame.draw.rect(screen, (0,0,0), (60, 160, width - 120, height - 220))
                                    screen.blit(dead_font.render("You are dead", True, (255, 0, 0)), (60, height/2-40))
                                    screen.blit(dead_font.render(f'Game time: {game_time}', True, (255, 0, 0)),(60,height/2 + 40))
                                    on = False
                                    nada = False
                                    break
                                if cords_if_bomb[cordinata] == '0':
                                    if cords_if_bomb[cordinata] not in opened_cells:
                                       chek_around(cordinata)
                                if cords_if_bomb[cordinata]:
                                    opened_cells.append(cordinata)
                        if opened_cells:
                            for key in opened_cells:
                                if str(cords_if_bomb[key]) == '0':chek_around(key)
                                if str(cords_if_bomb[key]) == '0':color = (0,0,0)
                                elif str(cords_if_bomb[key]) == '1':color = (0,0,100)
                                elif str(cords_if_bomb[key]) == '2':color = (0,100,0)
                                elif str(cords_if_bomb[key]) == '3':color = (100,0,0)
                                elif str(cords_if_bomb[key]) == '4':color = (100,0,100)
                                elif str(cords_if_bomb[key]) == '5':color = (255,238,0)
                                elif str(cords_if_bomb[key]) == '6':color = (0, 255, 230)
                                elif str(cords_if_bomb[key]) == '7':color = (0,0,0)
                                elif str(cords_if_bomb[key]) == '8':color = (107, 30, 30)
                                else:color = (0,0,0)
                                x,y = int(key[0]), int(key[2])
                                color_rec = (125, 75, 0) if (x + y*9) % 2 == 0 else (179, 108, 2)
                                pygame.draw.rect(screen, color_rec, rects['rect' + key])
                                screen.blit(num_font.render(str(cords_if_bomb[key]), True, color),(18 + 60 * int(key[0]),height - 50 - 60 * int(key[2])))
                                flagged['rect' + key] = 'numb'


                if event.button == 3:
                    pygame.mouse.get_pos()

                    for key in rects:
                        # key = rectx_y
                        if rects[key].collidepoint(event.pos):
                            if key in flagged:
                                if flagged[key] != 'numb':
                                    del flagged[key]
                                    col = int(key[4]) * 9 + int(key[6])
                                    color = (0, 130, 0) if col % 2 == 0 else (0, 180, 0)
                                    pygame.draw.rect(screen, color, rects[key])
                                    flags += 1
                                    pygame.draw.rect(screen, (0,0,0), (0, 0, width/2, 100))
                                    screen.blit(font.render(f'There are {flags} flags left',True,(255,255,255)),(20,50))
                            else:
                                if flags > 0:
                                    screen.blit(flag_image, (60 * int(key[4]), height - 60 - 60 * int(key[6])))
                                    flags -= 1
                                    pygame.draw.rect(screen, (0,0,0), (0, 0, width/2, 100))
                                    screen.blit(font.render(f'There are {flags} flags left', True, (255,255,255)), (20, 50))
                                    flagged[key] = True
            if len(set(opened_cells)) == 80:
                for numb in range(100):
                    cur_num = f'{numb:02}'
                    col_num = int(cur_num[0]) * 9 + int(cur_num[1])
                    color = (0, 130, 0) if col_num % 2 == 0 else (0, 180, 0)
                    cur_rect = 'rect' + cur_num[1] + '_' + cur_num[0]
                    if cur_rect in rects:
                        pygame.draw.rect(screen, color, rects[cur_rect])
                for x in range(0, width + 1, 60):
                    pygame.draw.line(screen, (0, 0, 0), (x, 100), (x, height), 3)
                for y in range(0, height, 60):
                    pygame.draw.line(screen, (0, 0, 0), (0, 100 + y), (width, 100 + y), 3)
                pygame.draw.rect(screen, (0, 0, 0), (60, 160, width - 120, height - 220))
                screen.blit(dead_font.render("You've won", True, (0, 255, 0)), (60, height / 2 - 40))
                screen.blit(dead_font.render(f'Game time: {game_time}', True, (0, 255, 0)), (60, height / 2 + 40))
                on = False
                nada = False
                break








        if nada:
            for x in range(0,width+1,60):
                pygame.draw.line(screen, (0, 0, 0), (x, 100), (x, height), 3)
            for y in range(0,height,60):
                pygame.draw.line(screen, (0, 0, 0), (0, 100 + y), (width, 100 + y),3)




        pygame.display.flip()
        clock.tick(60)



