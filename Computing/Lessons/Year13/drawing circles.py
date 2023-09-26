import pygame

xValue = 1200
yValue = 800
runs = 0
diff = 50
pygame.init()
screen = pygame.display.set_mode([xValue, yValue])
running = True
while True:
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
    except:
        break