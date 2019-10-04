import pygame as pg
def Init(n):
    global bg,screen
    pg.init()
    width, height = 20*n,20*(n+1)
    screen = pg.display.set_mode((width,height))
    pg.display.set_caption("Celluar Automata")
    
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
    for i in range(n):
        for j in range(n):
            pg.draw.rect(bg,(255,255,255),[i*20,j*20,19,19],0)
            pg.draw.rect(bg,(211,211,211),[i*20,j*20,20,20],1)
    l = int(n*20/3)
    pg.draw.rect(bg,(205,92,92),[0,n*20,l,20],0) 
    pg.draw.rect(bg,(255,255,0),[l,n*20,l,20],0)
    pg.draw.rect(bg,(50,205,50),[l*2,n*20,l,20],0)
    return bg,screen

def clicked(cell):
    mouse = pg.mouse.get_pos()
    x = mouse[0]//20
    y = mouse[1]//20
    if not(y==len(cell)):
        if cell[x][y]:
            cell[x][y] = 0
        else:
            cell[x][y] = 1
    return cell

def button(n,root,sub1,sub2,order,reset):
    mouse = pg.mouse.get_pos()
    if(mouse[1] >=20*(n-1)):
        x = mouse[0] //int(20*n/3)
        if x == 0 and order == 1:
            sub1 = False
        elif order == 2:
            sub2 = False
        if x == 1:
            reset = True
            sub2 = False
        if x == 2 :
            sub1 = False
            sub2 = False
            root = False
    return root,sub1,sub2,reset