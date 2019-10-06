import pygame as pg
import time,os
import CA_func as c 
import pgset
k = input("File name:")
initial_pos=[int(input("Iitial x:")),int(input("Initial y:"))]
csize = int(input("cell size"))
x = int(input("width:"))
y = int(input("height:"))
if csize <5:
    csize = 5
elif csize>50:
    csize = 20
if csize*x >= 1600:
    x = int(1600/csize)
if csize*y >= 900:
    y = int(900/csize)
if(csize*x<100 or csize*y <100):
    x, y ,csize =20, 20 ,20

temp = pgset.Init(csize,x,y)
bg,screen = temp[0],temp[1]



clock = pg.time.Clock()
root = True
cell1 = c.cell(x,y,k,initial_pos)
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
                cell2 = pgset.clicked(cell1,x,y,csize)
                btemp = pgset.button(x,y,root,cell1,sub1,sub2,1,reset,csize)
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
                btemp = pgset.button(x,y,cell1,root,sub1,sub2,2,reset,csize)
                root, sub1,sub2,reset = btemp[0],btemp[1],btemp[2],btemp[3]
        for i in range(x):
            for j in range(y):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[csize*i,csize*j, csize-1, csize-1], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[csize*i,csize*j, csize-1, csize-1], 0)

        cell2 = c.evolve(cell1,x,y)
        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()
    if reset:
        cell1 = c.cell(x,y,"0",[])
    if root:
        sub1 ,sub2 = True, True
pg.quit()   
