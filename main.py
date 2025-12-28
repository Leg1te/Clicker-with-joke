import pygame

pygame.init()

#mixer
pygame.mixer.pre_init(44100, -16, 1, 512)

#music
sound_1 = pygame.mixer.music.load("data/sounds/1.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.mixer.music.queue("data/sounds/3.mp3")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Clicker")
pygame.display.set_icon(click_png)


#Class of button
class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):

        # pos mouse
        pos = pygame.mouse.get_pos()
        
        # checker
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                clikc_sound = pygame.mixer.Sound("data/sounds/Click.mp3")
                clikc_sound.play()
                global Score
                Score += 1

            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
                

        # рисуем кнопки
        screen.blit(self.image, (self.rect.x, self.rect.y))


# buttons
buttons_click = button(335, 150, click_me, 0.1)

# dont touch
running = True
while running:

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.queue("data/sounds/3.mp3")

    screen.fill((255, 255, 255))

    buttons_click.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clikc_sound = pygame.mixer.Sound("data/sounds/Click.mp3")
                clikc_sound.play()
                Score += 1
    
    text_surface = font.render(f"Очков: {Score}", True, (0, 0, 0))
    screen.blit(text_surface, (290, 30))
    
    text_surface_1 = font_1.render("P.s space - что-бы кликать", True, (0, 0, 0))
    screen.blit(text_surface_1, (220, 360))

    text = font_1.render("Цель: 15000 очков", True, (0, 0, 0))
    screen.blit(text, (270, 400))

    clock.tick(60)
    pygame.display.update()

pygame.quit()

