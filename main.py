import pygame as pg
import time,os
import CA_func as c 
import pgset


x = int(input("width"))
y = int(input("height"))

if x >= 97:
    x = 96
if y >= 50:
    y = 50
if(x<11 or y <11):
    x, y =10, 10

temp = pgset.Init(x,y)
bg,screen = temp[0],temp[1]



clock = pg.time.Clock()
root = True
cell1 = c.cell(x,y)

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
                cell2 = pgset.clicked(cell1,x,y)
                btemp = pgset.button(x,y,root,sub1,sub2,1,reset)
                root, sub1,sub2 = btemp[0],btemp[1],btemp[2]
        for i in range(x):
            for j in range(y):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[20*i,20*j, 19, 19], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[20*i,20*j, 19, 19], 0)

        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()
    sub1 = True
    while sub2 and root:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                   sub2 = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   sub2 = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                btemp = pgset.button(x,y,root,sub1,sub2,2,reset)
                root, sub1,sub2,reset = btemp[0],btemp[1],btemp[2],btemp[3]
        for i in range(x):
            for j in range(y):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[20*i,20*j, 19, 19], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[20*i,20*j, 19, 19], 0)

        cell2 = c.evolve(cell1,x,y)
        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()
    if reset:
        cell1 = c.cell(x,y)
    if root:
        sub1 ,sub2 = True, True
pg.quit()   
