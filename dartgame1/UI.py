import pygame
import sys

pygame.init()

screen_w = 612
screen_h = 458

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Menu")

dart_bg = pygame.image.load("images/dart_background.png").convert_alpha()
play_button = pygame.image.load("images/play_button.png").convert_alpha()
exit_button_image = pygame.image.load("images/exit_button.png").convert_alpha()
font = pygame.font.Font("fonts/bayern/BAYERN__.TTF", 120)
text_surface = font.render("Darts", True, (186, 20, 7))
text_rect = text_surface.get_rect()

text_rect.topleft = (170, 70)


new_w_for_play_b = 125
new_h_for_play_b = 125

new_w_for_exit_b = 150
new_h_for_exit_b = 150


new_play_button = pygame.transform.scale(play_button, (new_w_for_play_b, new_h_for_play_b))
new_exit_button = pygame.transform.scale(exit_button_image, (new_w_for_exit_b, new_h_for_exit_b))

pygame.mixer.music.load("sounds/bg_music.mp3")
pygame.mixer.music.play(-1)

class UI:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

new_play_button = UI(243, 200, new_play_button)
new_exit_button = UI(231, 320, new_exit_button)

run = True
while run:
    screen.blit(dart_bg, (0, 0))
    screen.blit(text_surface, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if new_play_button.rect.collidepoint(event.pos):
                run = False
                print("Play button clicked!")
            elif new_exit_button.rect.collidepoint(event.pos):
                pygame.quit()

    new_play_button.draw()
    new_exit_button.draw()

    pygame.display.update()

pygame.quit()
