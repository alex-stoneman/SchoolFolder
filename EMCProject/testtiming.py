import pygame
from time import sleep
xValue = 1200
yValue = 400
runs = 0
diff = 50
pygame.init()
screen = pygame.display.set_mode([xValue, yValue])
running = True
while True:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.fill((0, 0, 0))
            pygame.display.flip()
            sleep(2)




