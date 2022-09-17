"""
https://www.youtube.com/watch?v=PJl4iabBEz0&list=RDCMUCbXgNpp0jedKWcQiULLbDTA&index=2&ab_channel=PythonEngineer
"""

from os import system as sys
import pygame as pg
import random as rd
import time
#%% Input Data:

pg.init()    

loser_status = \
    """
▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄    
▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
▀▄▀▄                                            ▀▄▀▄
▀▄▀▄                                            ▀▄▀▄
▀▄▀▄    ███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀    ▀▄▀▄
▀▄▀▄    ██    ██ ██     ██ ██   █   ██ ██       ▀▄▀▄
▀▄▀▄    ██   ▄▄▄ ██▄▄▄▄▄██ ██   ▀   ██ ██▀▀▀    ▀▄▀▄
▀▄▀▄    ██    ██ ██     ██ ██       ██ ██       ▀▄▀▄
▀▄▀▄    ███▄▄▄██ ██     ██ ██       ██ ██▄▄▄    ▀▄▀▄
▀▄▀▄                                            ▀▄▀▄ 
▀▄▀▄    ███▀▀▀███ ▀███  ██▀ ██▀▀▀ ██▀▀▀▀██▄     ▀▄▀▄
▀▄▀▄    ██     ██   ██  ██  ██    ██     ██     ▀▄▀▄ 
▀▄▀▄    ██     ██   ██  ██  ██▀▀▀ ██▄▄▄▄▄▀▀     ▀▄▀▄ 
▀▄▀▄    ██     ██   ██  █▀  ██    ██    ██      ▀▄▀▄
▀▄▀▄    ███▄▄▄███    ▀█▀    ██▄▄▄ ██     ██▄    ▀▄▀▄
▀▄▀▄                                            ▀▄▀▄
▀▄▀▄            ██               ██             ▀▄▀▄
▀▄▀▄          ████▄  ▄▄▄▄▄▄▄   ▄████            ▀▄▀▄
▀▄▀▄             ▀▀█▄█████████▄█▀▀              ▀▄▀▄
▀▄▀▄               █████████████                ▀▄▀▄
▀▄▀▄               ██▀▀▀███▀▀▀██                ▀▄▀▄
▀▄▀▄               ██   ███   ██                ▀▄▀▄
▀▄▀▄               █████▀▄▀█████                ▀▄▀▄
▀▄▀▄                ███████████                 ▀▄▀▄
▀▄▀▄            ▄▄▄██  █▀█▀█  ██▄▄▄             ▀▄▀▄
▀▄▀▄            ▀▀██           ██▀▀             ▀▄▀▄
▀▄▀▄              ▀▀           ▀▀               ▀▄▀▄
▀▄▀▄                                            ▀▄▀▄
▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄    
▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
    """    

#>> Coloração (segue o padrão RGB):
background = (0, 0, 0)    #-> black
snake_color = (0, 255, 0) #-> green
food_color = (255, 0, 0)  #-> red
score_color = (255, 255, 255) #-> red


#>> Display:
dim = (600, 600)  #-> dimensão da tela: ixj, sendo i,j número de pixels
screen = pg.display.set_mode((dim))
screen.fill(background)
fonte_large = pg.font.SysFont("hack", 25) #-> pg.font.SysFont(name, size)
fonte_small = pg.font.SysFont("hack", 15) #-> pg.font.SysFont(name, size)


clock = pg.time.Clock() #-> frame rate
#%% Game Functions:

#----------------------------------------#
#>> Função para gerar o objeto 'snake':
x, y = int(dim[0]/2),\
       int(dim[1]/2) #-> coordenadas do objeto

size_zero = 10    #-> tamanho inicial do objeto

snake_list = [[x, y]]

dx = 0
dy = 0

def draw_snake(snake_list):
    screen.fill(background)
    
    for unity in snake_list:
        pg.draw.rect(screen, snake_color, [  unity[0], unity[1],
                                            size_zero, size_zero]) #-> pygame.draw.rect(surface, color, rect): gera um retângulo; 'rect' é a lista das coordenadas 'x' e 'y'

#----------------------------------------#
#>> Função para mover o objeto 'snake':
def move_snake(dx, dy, snake_list):
    direction = []
    
    #>> leitura dos comandos do teclado:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:    #-> seta esquerda
                direction.append('◀')
                dx = -size_zero
                dy = 0
                pg.display.set_caption(f"ACTUAL COMMAND: {direction[-1]}")
            elif event.key == pg.K_RIGHT: #-> seta direita
                direction.append('▶')
                dx = size_zero
                dy = 0
                pg.display.set_caption(f"ACTUAL COMMAND: {direction[-1]}")
            elif event.key == pg.K_UP:    #-> seta cima
                direction.append('▲')
                dx = 0
                dy = -size_zero
                pg.display.set_caption(f"ACTUAL COMMAND: {direction[-1]}")
            elif event.key == pg.K_DOWN:  #-> seta baixo
                direction.append('▼')
                dx = 0
                dy = size_zero
                pg.display.set_caption(f"ACTUAL COMMAND: {direction[-1]}")
    
    x_new = snake_list[-1][0] + dx
    y_new = snake_list[-1][1] + dy
    
    #>> deslocamento visual:
    snake_list.append([x_new, y_new]) #-> adiciona os elementos ao objeto 'snake' (delocamento da 'cabeça')
    del snake_list[0]                 #-> exclui o elemento do objeto 'snake' (deslocamento da 'cauda')
    
    return dx, dy, snake_list

#----------------------------------------#
#>> Função para gerar o objeto 'food':

#-> coordenadas randômicas do objeto 'food':
x_food = round(rd.randrange(0, dim[0]-size_zero)/size_zero) * size_zero #-> rd.randrange(start, stop, step)
y_food = round(rd.randrange(0, dim[1]-size_zero)/size_zero) * size_zero #-> rd.randrange(start, stop, step)

def verify_food(dx, dy, x_food, y_food, snake_list):
    snake_head = snake_list[-1]
    
    x_new = snake_head[0] + dx 
    y_new = snake_head[1] + dy
    
    if snake_head[0] == x_food and snake_head[1] == y_food:
        snake_list.append([x_new, y_new])
        
        #-> novas coordenadas randômicas de 'food'
        x_food = round(rd.randrange(0, dim[0]-size_zero)/size_zero) * size_zero #-> rd.randrange(start, stop, step)
        y_food = round(rd.randrange(0, dim[1]-size_zero)/size_zero) * size_zero #-> rd.randrange(start, stop, step)
    
    pg.draw.rect(screen, food_color, [   x_food,    y_food,
                                      size_zero, size_zero])
    
    return x_food, y_food, snake_list

#----------------------------------------#
#>> Função para verificar o obstáculo 'wall':
def verify_wall(snake_list):
    snake_head = snake_list[-1]
    x = snake_head[0]
    y = snake_head[1]
    
    #-> Restrição para o espaço passível de deslocamento da cobra:
    if x not in range(dim[0]) or y not in range(dim[1]):
        
        sys('cls')
        txt = loser_status +\
            ('\n') + ('_'*50) +\
            ('\n\n>> CAUSE: PLAYER REACHED WALL BOUNDARIES') +\
            ('\n') + ('_'*50) + ('\n')+\
            (f"\n>> TOTAL SCORE: {str(len(snake_list)-1)}")\
            + ('\n') + ('_'*50) + ('\n')  
        print(txt)
                
        time.sleep(1.5)
        raise Exception #-> Exception é o travamento do programa na condição dada
#----------------------------------------#
#>> Função para verificar o obstáculo 'snake':
def auto_snake(snake_list):
    snake_head = snake_list[-1]
    snake_body = snake_list.copy()
    
    del snake_body[-1]
    for x, y in snake_body:
        if x == snake_head[0] and y == snake_head[1]:
            sys('cls')
            txt = loser_status +\
            ('\n') + ('_'*50) +\
            ('\n\n>> CAUSE: PLAYER AUTO-COLLISION') +\
            ('\n') + ('_'*50) + ('\n') +\
            (f"\n>> TOTAL SCORE: {str(len(snake_list)-1)}")\
            + ('\n') + ('_'*50) + ('\n')    
            print(txt)            
            
            time.sleep(1.5)
            raise Exception

#----------------------------------------#
#>> Função para atualizar o placar:
def update_score(snake_list):
    #-> retorna no display a pontuação do jogador:
    pts = str(len(snake_list)-1)
    score = fonte_large.render("SCORE: " + pts, True, score_color)
    screen.blit(score, [0,0]) #-> .blit(source, dest)
    
    
#%% Run Game:
tic = time.perf_counter()
while True:
    
    pg.display.update()
    
    draw_snake(snake_list)
    dx, dy, snake_list = move_snake(dx, dy, snake_list)
    
    x_food, y_food, snake_list = verify_food(dx, dy, x_food, y_food, snake_list)
    
    verify_wall(snake_list)
    auto_snake(snake_list)
    update_score(snake_list)
    
    #print(snake_list)
    
    clock.tick(20)
    
    pg.display.update()
    
    toc = time.perf_counter()
    
    t_diff = str(toc-tic)
    
    t_text = fonte_small.render("Elapsed Time: " + t_diff + ' seconds', True, score_color)
    screen.blit(t_text, [0,590]) #-> .blit(source, dest)