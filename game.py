import pygame

class Game:
    def __init__(self, assets):
        self.screen = pygame.display.set_mode((800, 600))
        self.assets = assets
        pygame.display.set_caption("Clicker")
        pygame.display.set_icon(self.assets["ico"])

        self.click = False
        self.mouse_clicked = False
        self.click_sound = assets["click_sound"]

        self.Score = self.assets["score"] # score
        self.clock = pygame.time.Clock()

        # music
        pygame.mixer.music.load("data/sounds/1.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        pygame.mixer.music.queue("data/sounds/3.mp3")

        # Class of button
        class Button:
            def __init__(self, x, y, image, scale, game):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.game = game

            def draw(self):

                # pos mouse
                pos = pygame.mouse.get_pos()

                # checker
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.game.click == False:
                        self.game.click = True
                        self.game.mouse_clicked = True
                        self.game.click_sound.play()
                        self.game.Score += 1

                    if pygame.mouse.get_pressed()[0] == 0:
                        self.game.click = False
                        self.game.mouse_clicked = False

                # drawing
                self.game.screen.blit(self.image, (self.rect.x, self.rect.y))

        # buttons
        self.buttons_click = Button(335, 150, self.assets["click_me"].convert_alpha(), 0.1, self)

        #fonts
        self.font = self.assets["font"]
        self.font_1 = self.assets["font_1"]

    def run(self):
        running = True
        while running:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.queue("data/sounds/2.mp3")

            self.screen.fill((255, 255, 255))

            # draw
            self.buttons_click.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.click == False and not self.mouse_clicked:
                        self.click = True
                        self.click_sound.play()
                        self.Score += 1

            text_surface = self.font.render(f"Очков: {self.Score}", True, (0, 0, 0))
            self.screen.blit(text_surface, (290, 30))

            text_surface_1 = self.font_1.render("P.s space - что-бы кликать", True, (0, 0, 0))
            self.screen.blit(text_surface_1, (220, 360))

            text = self.font_1.render("Цель: 15000 очков", True, (0, 0, 0))
            self.screen.blit(text, (270, 400))

            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()







