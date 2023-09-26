import pygame
import time
def find(number):
    return ((number/10) * 16) ** 2


while True:
    pygame.init()
    screen = pygame.display.set_mode([750, 750])
    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            colour = 0
            num = 10
            for x in range(num):
                print(colour)
                #pygame.draw.circle(screen, (255, colour, 0), (125, 125), 80)
                pygame.draw.circle(screen, (0, colour, 255), (375, 125), 80)
                #pygame.draw.circle(screen, (0, colour, 00), (625, 125), 80)

                #pygame.draw.circle(screen, (colour, 0, 255), (125, 375), 80)
                pygame.draw.circle(screen, (colour, 255, 0), (375, 375), 80)
                #pygame.draw.circle(screen, (colour, 0, 0), (625, 375), 80)

                #pygame.draw.circle(screen, (0, 255, colour), (375, 625), 80)
                #pygame.draw.circle(screen, (255, 0, colour), (625, 625), 80)
                #pygame.draw.circle(screen, (0, 0, colour), (125, 625), 80)

                colour += 255 // num
                time.sleep(0.3)

                pygame.display.flip()
        pygame.quit()


    except KeyboardInterrupt:
        print("Closing...")
