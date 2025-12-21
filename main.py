import pygame

pygame.init()


num = 0

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 45)

click_png = pygame.image.load("png\click.png").convert()
pygame.display.set_caption("Clicker")
pygame.display.set_icon(click_png)

# цикл
running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    text_surface = font.render(f"Вы кликнули {num} раз", True, (0, 0, 0))
    screen.blit(text_surface, (250, 25))

    clock.tick(60)
    pygame.display.update()

pygame.quit()