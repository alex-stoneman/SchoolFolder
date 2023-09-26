import datetime
from time import sleep
import pygame


def convert(num):
    numbers = []
    for x in range(6):
        current = num // 2 ** (5 - x)
        num -= current * 2 ** (5 - x)
        numbers.append(current)
    final = ""
    for i in numbers:
        final += str(i)

    return final


def binary_clock():
    time = datetime.datetime.now()
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    micro = (time.microsecond // 10000)
    clock = [convert(hours), convert(minutes), convert(seconds), micro]
    return clock


def draw():
    pygame.init()
    screen = pygame.display.set_mode([970, 500])
    running = True
    rgb = 0
    swap = 1
    other = 0
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            values = binary_clock()
            # print(values)
            other += 1
            if other % 4 == 0:
                if rgb == 255:
                    swap = -1
                elif rgb == 30:
                    swap = 1

                rgb += swap

            for x in range(6):
                for y in range(3):
                    do = True
                    d = 0
                    if y == 0:
                        colour = [255, 20 + rgb // 2, rgb]
                        d = 75
                        if x == 0:
                            do = False
                    elif y == 1:
                        colour = [255, 255 - rgb // 2, rgb]
                    else:
                        colour = [0, 255 - rgb // 2, rgb]
                    # print(values[y][x])
                    if do:
                        pygame.draw.circle(screen, (colour[0], colour[1], colour[2]), (85 + x * 160 - d, 85 + y * 160),
                                           75)
                        try:
                            if (values[y])[x] == "0":
                                pygame.draw.circle(screen, (0, 0, 0), (85 + x * 160 - d, 85 + y * 160), 60)
                        except IndexError:
                            print("PROBLEM")
                            colour = [255, 0, 0]

            pygame.display.flip()
        pygame.quit()
    except KeyboardInterrupt:
        print("Closing...")


while True:
    draw()
