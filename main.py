import pygame as pg
import time,os
import CA_func as c 
import pgset


n = int(input("size"))
temp = pgset.Init(n)
bg,screen = temp[0],temp[1]



clock = pg.time.Clock()
root = True
cell1 = c.cell(n)

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
                cell2 = pgset.clicked(cell1)
                btemp = pgset.button(n,root,sub1,sub2,1,reset)
                root, sub1,sub2 = btemp[0],btemp[1],btemp[2]
        for i in range(n):
            for j in range(n):
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
                btemp = pgset.button(n,root,sub1,sub2,2,reset)
                root, sub1,sub2,reset = btemp[0],btemp[1],btemp[2],btemp[3]
        for i in range(n):
            for j in range(n):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[20*i,20*j, 19, 19], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[20*i,20*j, 19, 19], 0)

        cell2 = c.evolve(cell1)
        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()
    if reset:
        cell1 = c.cell(n)
    if root:
        sub1 ,sub2 = True, True
pg.quit()   
