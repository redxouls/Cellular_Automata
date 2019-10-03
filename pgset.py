import pygame as pg
def Init(n):
    global bg,screen
    pg.init()
    width, height = 1920,1080
    screen = pg.display.set_mode((width,height))
    pg.display.set_caption("Celluar Automata")
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((255,255,255))
    print(type(bg))
    for i in range(n):
        for j in range(n):
            pg.draw.rect(bg,(211,211,211),[i*20,j*20,20,20],1)
    return bg,screen

def clicked(cell):
    mouse = pg.mouse.get_pos()
    x = mouse[0]//20
    y = mouse[1]//20
    if cell[x][y]:
        cell[x][y] = 0
    else:
        cell[x][y] = 1
    return cell

