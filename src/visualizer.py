import pygame
import random
from algorithms import *
from rectangle import Rectangle

pygame.init()

#window settings
WINDOW_SIZE = 600
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sort Visualizer")

#variables
RECT_WIDTH = 20
clock = pygame.time.Clock()
FPS = 10

#colors
BLACK = (0, 0, 0)
GREY = (170, 170, 170)
        

def create_rects() -> list[Rectangle]:
    num_rects = WINDOW_SIZE // RECT_WIDTH - 5
    rects = []
    heights = []
    
    for i in range(5, num_rects):
        height = random.randint(20, 500)
        heights.append(height)
        rects.append(Rectangle(i*RECT_WIDTH, RECT_WIDTH, height))
        
    return rects


def draw_rects(rects: list[Rectangle]):
    WINDOW.fill(GREY)
    
    for rect in rects:
        pygame.draw.rect(WINDOW, rect.color, (rect.x, WINDOW_SIZE - rect.height, rect.width, rect.height))
        #rect border
        pygame.draw.line(WINDOW, BLACK, (rect.x, WINDOW_SIZE), (rect.x, WINDOW_SIZE-rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x + rect.width, WINDOW_SIZE), (rect.x+rect.width, WINDOW_SIZE-rect.height))
        pygame.draw.line(WINDOW, BLACK, (rect.x, WINDOW_SIZE-rect.height), (rect.x+rect.width, WINDOW_SIZE-rect.height))
        

def display_text(txt, y, size):
    FONT = pygame.font.SysFont('Futura', size)
    
    text = FONT.render(txt, True, BLACK)
    text_rect = text.get_rect(center=(WINDOW_SIZE/2, y))
    WINDOW.blit(text, text_rect)


def main():
    rects = create_rects()
    draw_rects(rects)
    sorting_generator = SelectSort(draw_rects).algorithm(rects)
    
    run = True
    sorting = False
    while run:
        clock.tick(FPS)
        
        if sorting:
            try:
                next(sorting_generator)
            except StopIteration:
                sorting = False        
        else:
            draw_rects(rects)
        
        display_text('Press SPACE to start sorting or pause or q to quite', 70, 30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sorting = not sorting
                    
                if event.key == pygame.K_q:
                    run = False
                
        pygame.display.update()
        
    pygame.quit()
    
main()