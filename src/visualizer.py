import pygame
from pygame_menu import Menu, themes, events
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
FPS = 30
sorter = BubbleSort
rects = []
#defines sorting algorithm and dataset status
initialized = False


#colors
BLACK = (0, 0, 0)
GREY = (170, 170, 170)


#MENU
#handlers
def set_sorting_generator(selected, index): 
    globals()['initialized'] = False
    globals()['sorter'] = selected[0][1]
    
    

def handle_start(menu):
    menu.disable()
    menu.full_reset()

#menu items
menu = Menu('MENU', WINDOW_SIZE, WINDOW_SIZE, theme=themes.THEME_DARK)
menu.add.dropselect('Algorithm', algoritms_list, 0, onchange=set_sorting_generator)
menu.add.button('Start', handle_start, menu)
menu.add.button('Exit', events.EXIT)
menu.enable()


#dataset creater
def create_rects() -> list[Rectangle]:
    num_rects = WINDOW_SIZE // RECT_WIDTH - 5
    rects = []
    heights = []
    
    for i in range(5, num_rects):
        height = random.randint(20, 500)
        heights.append(height)
        rects.append(Rectangle(i*RECT_WIDTH, RECT_WIDTH, height))       
    return rects


#visuals
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
    run = True
    sorting = False
    global initialized
     
    while run:
        events = pygame.event.get()
        
        if menu.is_enabled():
            menu.draw(WINDOW)
            menu.update(events)
            
        else:
            if not initialized:
                rects = create_rects()
                draw_rects(rects)
                sorting_generator = sorter(draw_rects).algorithm(rects)
                initialized = True
                
            if sorting:
                clock.tick(FPS)
                try:
                    next(sorting_generator)
                except StopIteration:
                    sorting = False        
            else:
                draw_rects(rects)
                display_text('Press SPACE to start or pause, m to open menu', 70, 30)

            for event in events:
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sorting = not sorting
                        
                    if event.key == pygame.K_m:
                        menu.enable()

                    if event.key == pygame.K_q:
                        run = False
            
                
        pygame.display.update()
    pygame.quit()
    
main()