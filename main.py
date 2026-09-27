import pygame
from pygame.locals import * 

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("flappy bird")

ground_scroll = 0
scroll_speed = 49

bg = pygame.image.load('bg.png')
ground_img = pygame.image.load("ground.png")

run = True
while run:
    clock.tick(fps)

    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

