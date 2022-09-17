import pygame as pg
import colorsys
import math
import time


pg.init()
#%% Inputs:

#dim = (1920, 1080) #-> screen dimensions (pixels): width x height
dim = (1000, 800) #-> screen dimensions (pixels): width x height
screen = pg.display.set_mode((dim))
display_surface = pg.display.set_mode((dim))
# display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pg.display.set_caption("donut.py")
font = pg.font.SysFont('hack', 15, bold=True, italic = True)


green = (0, 255, 0)
black = (0, 0, 0)
hue = 0

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

columns = dim[0] // x_separator
rows = dim[1] // y_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2


A, B = 0, 0  #-> rotational effect parameters
theta_spacing = 10
phi_spacing = 1 # for faster rotation change to 2, 3 or more, but first change 86, 87 lines as commented

chars = '.,-~:;=!*#$@'  #-> luminance index (from dimmest to brightest)


#%% Functions:

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, green)
    display_surface.blit(text, (x_start, y_start))

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


#%% Run Program:

tic = time.perf_counter()
run = True

while run:

    screen.fill((black))

    z = [0] * screen_size  # Donut. Fills donut space
    b = [' '] * screen_size  # Background. Fills empty space

    for j in range(0, 628, theta_spacing):  # from 0 to 2pi
        for i in range(0, 628, phi_spacing):  # from 0 to 2pi
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)  # 3D z coordinate after rotation
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 2e-5 # for faster rotation change to 0.0002
        B += 1e-5 # for faster rotation change to 0.0001
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator
    
    
    toc = time.perf_counter()
    t_diff = str(toc-tic)
    
    
    font2 = pg.font.SysFont('arial', 12, bold=True)
    
    text1 = 'Elapsed Time:'
    text2 = 'Press ESC to exit program.'
    text3 = 'ASCII Spinning Donut.'
    text4 = 'by: See_0ff'
    
    t1 = font2.render("Elapsed Time: " + t_diff + ' seconds', True, (255, 255, 255))
    screen.blit(t1, [0, 0]) #-> .blit(source, dest)
    
    t2 = font2.render(text2, True, (255, 255, 255))
    screen.blit(t2, [0, 20]) #-> .blit(source, dest)
    
    t3 = font2.render(text3, True, hsv2rgb(hue, 1, 1))
    screen.blit(t3, [0, dim[1]-40]) #-> .blit(source, dest)
    
    t4 = font2.render(text4, True, hsv2rgb(hue, 1, 1))
    screen.blit(t4, [0, dim[1]-20]) #-> .blit(source, dest)
    
    pg.display.update()
    
    hue += 5e-03

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
