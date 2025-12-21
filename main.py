import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
click_png = pygame.image.load("click.png").convert()

pygame.display.set_caption("Clicker")
pygame.display.set_icon(click_png)

running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.update()

pygame.quit()