import pygame as pg
def Init(csize,x,y):
    global bg,screen
    pg.init()
    width, height = csize*x,csize*y+20
    screen = pg.display.set_mode((width,height))
    pg.display.set_caption("Celluar Automata")
    
    bg = pg.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0,0,0))
    for i in range(x):
        for j in range(y):
            pg.draw.rect(bg,(255,255,255),[i*csize,j*csize,csize-1,csize-1],0)
            pg.draw.rect(bg,(211,211,211),[i*csize,j*csize,csize,csize],1)
    l = int(x*csize/4)
    pg.draw.rect(bg,(205,92,92),[0,y*csize,l,20],0) 
    pg.draw.rect(bg,(255,255,0),[l,y*csize,l,20],0)
    pg.draw.rect(bg,(50,205,50),[l*2,y*csize,l,20],0)
    pg.draw.rect(bg,(30,144,255),[l*3,y*csize,l,20],0)

    return bg,screen

def clicked(cell,x,y,csize):
    mouse = pg.mouse.get_pos()
    x1 = mouse[0]//csize
    y1 = mouse[1]//csize
    if not(y1>=y):
        if cell[x1][y1]:
            cell[x1][y1] = 0
        else:
            cell[x1][y1] = 1
    return cell

def button(x,y,root,cell,sub1,sub2,order,reset,csize):
    mouse = pg.mouse.get_pos()
    if(mouse[1] >=csize*y):
        x1 = mouse[0] //int(csize*x/4)
        if x1 == 0 and order == 1:
            sub1 = False
        elif order == 2:
            sub2 = False
        if x1 == 1:
            reset = True
            sub1 = False
            sub2 = False
        if x1 == 2 :
            sub1 = False
            sub2 = False
            root = False
        if x1 ==3:
            output = input("Ouput file name :") + ".txt"
            print(cell)
            with open(output,"w") as text_file:
                for i in range(x):
                    for j in range(y):
                        if cell[i][j]:
                            text_file.write("O")
                        else:
                            text_file.write(".")
                    text_file.write("\n")
    return root,sub1,sub2,reset