import pygame as pg
import time,os
import CA_func as c 
import pgset


n = int(input("size"))
temp = pgset.Init(n)
bg,screen = temp[0],temp[1]



clock = pg.time.Clock()
run = True
while(run):
    run = False
    running = True
    cell1 = c.cell(n)
    while running:
        clock.tick(30)
        cell2 = cell1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                   running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                cell2 = pgset.clicked(cell1)
        for i in range(n):
            for j in range(n):
                if (cell1[i][j]):
                    pg.draw.rect(bg, (0,0,255),[20*i,20*j, 19, 19], 0)
                else:
                    pg.draw.rect(bg, (255,255,255),[20*i,20*j, 19, 19], 0)

        cell1 = cell2
        screen.blit(bg, (0,0))
        pg.display.update()

    running = True

    while running:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                   running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                   running = False
                elif event.key ==pg.K_SPACE:
                    run = True
                    running = False
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
pg.quit()   
