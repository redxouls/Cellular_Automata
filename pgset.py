import pygame as pg
def Init(x,y):
    global bg,screen
    pg.init()
    width, height = 20*x,20*(y+1)
    screen = pg.display.set_mode((width,height))
    pg.display.set_caption("Celluar Automata")
    
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
    for i in range(x):
        for j in range(y):
            pg.draw.rect(bg,(255,255,255),[i*20,j*20,19,19],0)
            pg.draw.rect(bg,(211,211,211),[i*20,j*20,20,20],1)
    l = int(x*20/3)
    pg.draw.rect(bg,(205,92,92),[0,y*20,l,20],0) 
    pg.draw.rect(bg,(255,255,0),[l,y*20,l,20],0)
    pg.draw.rect(bg,(50,205,50),[l*2,y*20,l,20],0)
    return bg,screen

def clicked(cell,x,y):
    mouse = pg.mouse.get_pos()
    x1 = mouse[0]//20
    y1 = mouse[1]//20
    if not(y1>=y):
        if cell[x1][y1]:
            cell[x1][y1] = 0
        else:
            cell[x1][y1] = 1
    return cell

def button(x,y,root,sub1,sub2,order,reset):
    mouse = pg.mouse.get_pos()
    if(mouse[1] >=20*y):
        x1 = mouse[0] //int(20*x/3)
        if x1 == 0 and order == 1:
            sub1 = False
        elif order == 2:
            sub2 = False
        if x1 == 1:
            reset = True
            sub2 = False
        if x1 == 2 :
            sub1 = False
            sub2 = False
            root = False
    return root,sub1,sub2,reset