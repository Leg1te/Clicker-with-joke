import pygame
import os

config_file = "configs/main_config.py"
folder_scripts = "configs"

#Create a folder
if not os.path.exists(folder_scripts):
    os.makedirs(folder_scripts, exist_ok=True)

# Создаём файл если его нет
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        f.write("Score = 0")

pygame.init()

#mixer
pygame.mixer.pre_init(44100, -16, 1, 512)

#music
sound_1 = pygame.mixer.music.load("sounds/1.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
pygame.mixer.music.queue("sounds/3.mp3")

#import cfg
import configs.main_config as cfg


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.Font("font/Pixel.ttf", 23)
font_1 = pygame.font.Font("font/Pixel.ttf", 13)

#loading png
click_png = pygame.image.load("png/click.png").convert()
click_me = pygame.image.load("png/Click_me.png").convert_alpha()

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
                clikc_sound = pygame.mixer.Sound("sounds/Click.mp3")
                clikc_sound.play()
                cfg.Score += 1

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
        pygame.mixer.music.queue("sounds/3.mp3")

    screen.fill((255, 255, 255))

    buttons_click.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                clikc_sound = pygame.mixer.Sound("sounds/Click.mp3")
                clikc_sound.play()
                cfg.Score += 1
    
    text_surface = font.render(f"Очков: {cfg.Score}", True, (0, 0, 0))
    screen.blit(text_surface, (290, 30))
    
    text_surface_1 = font_1.render("P.s space - что-бы кликать", True, (0, 0, 0))
    screen.blit(text_surface_1, (220, 360))

    text = font_1.render("Цель: 15000 очков", True, (0, 0, 0))
    screen.blit(text, (270, 400))

    clock.tick(60)
    pygame.display.update()

pygame.quit()

