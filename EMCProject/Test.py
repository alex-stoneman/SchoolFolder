import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((100, 100, 0))
font = pygame.font.SysFont("freesansbold.ttf", 50)
pygame.display.flip()
while True:
    needed = False
    for event in pygame.event.get():
        # print(event)
        # print(event.type)
        # print()
        if event.type == 771:
            pygame.draw.rect(screen, (100, 100, 0), (100, 100, 50, 50))
            print(event.text)
            text = font.render(event.text, False, (0,0,0))
            screen.blit(text, (100, 100))
            needed = True

    if needed:
        pygame.display.update((200, 200, 10, 10))


# While key held - 771 = TextInput
# Key down - 768 = KeyDown
# key down - 769 = KeyUp
# pygame.display.update(rect)
# - rect argument for the area of the display which needs to be updated
# only need to run this when something is changed
# This Should run much more efficiently