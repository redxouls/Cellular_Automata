import pygame as pg
import time,os


def cell(x,y,k,initial_pos):
    cell=[]
    for i in range(x):
            cell.append([])
            for j in range(y):
                    cell[i].append(0)
    if k!="0":
        ix , iy = initial_pos[0], initial_pos[1]
        print(ix,iy)
        k = k + ".txt"
        f = open(k,'r').readlines()
        inmax = 0
        for i in f:
            if len(i)>inmax:
                inmax = len(i)
        if len(f)+iy>=len(cell)-1 or inmax+ix >(len(cell[0])-1):
            print(len(f)+iy,iy,len(f))
            return cell
        else:
            for i in range(len(f)):
                for j in range(len(f[i])):
                    if f[i][j] == 'O':
                        cell[j+ix][i+iy] = 1
    return cell 

def alive(cell,xi,yi,x,y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            x1 = xi+i
            y1 = yi+j
            if x1<0 or y1<0 or x1>x-1 or y1>y-1 or (i==j and i==0):
                abc=1
            else:
                count += cell[x1][y1]
    if cell[xi][yi]==1:
        if count<2:
            return False
        elif count==2 or count<=3:
            return True
        elif count>3:
            return False
    else:
        if count == 3:
            return True
        else: 
            return False

def evolve(cellin,x,y): 
    cellout = cell(x,y,"0",[])
    cellin = tuple(cellin)
    for i in range(x):
        for j in range(y):
            if alive(cellin,i,j,x,y):
                cellout[i][j] = 1
            else:
                cellout[i][j] = 0
    return cellout
  
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


k = input("File name:")
if k != "0":
    ktemp = k + '.txt'
    f = open(ktemp,'r').readlines() 
    inmax = 0
    for i in f:
        if len(i)>inmax:
            inmax = len(i)
    print("x:",inmax,"y:",len(f),)
initial_pos=[int(input("Initial x:")),int(input("Initial y:"))]
csize = int(input("cell size"))
x = int(input("width:"))
y = int(input("height:"))
if csize <5:
    csize = 5
elif csize>50:
    csize = 20
if csize*x >= 1920:
    x = int(1920/csize)
if csize*y >= 1000:
    y = int(1000/csize)
if(csize*x<100 or csize*y <100):
    x, y ,csize =20, 20 ,20

temp = Init(csize,x,y)
bg,screen = temp[0],temp[1]



clock = pg.time.Clock()
root = True
cell1 = cell(x,y,k,initial_pos)
initial_pos = [0,0]
while(root):
    sub1 = True
    sub2 = True
    reset = False
    while sub1:
        clock.tick(30)
        cell2 = cell1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                   sub1 = False
                   root = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   sub1 = False
            elif event.type == pg.MOUSEBUTTONDOWN and (sub1 or root):
                cell2 = clicked(cell1,x,y,csize)
                btemp = button(x,y,root,cell1,sub1,sub2,1,reset,csize)
                root, sub1,sub2 = btemp[0],btemp[1],btemp[2]
        for i in range(x):
            for j in range(y):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[csize*i,csize*j, csize-1, csize-1], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[csize*i,csize*j, csize-1, csize-1], 0)

        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()
        
    while sub2 and root:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                   sub2 = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   sub2 = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                btemp = button(x,y,cell1,root,sub1,sub2,2,reset,csize)
                root, sub1,sub2,reset = btemp[0],btemp[1],btemp[2],btemp[3]
        for i in range(x):
            for j in range(y):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[csize*i,csize*j, csize-1, csize-1], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[csize*i,csize*j, csize-1, csize-1], 0)

        cell2 = evolve(cell1,x,y)
        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()
    if reset:
        cell1 = cell(x,y,"0",[])
    if root:
        sub1 ,sub2 = True, True
pg.quit()