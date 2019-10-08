import pygame as pg
def cell(x,y,k,initial_pos):
    cell=[]
    cellmode = []
    for i in range(x):
            cell.append([])
            cellmode.append([])
            for j in range(y):
                    cell[i].append(0)
                    cellmode[i].append(0)
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
                        for k in range(-1,2):
                            for l in range(-1,2):
                                cellmode[j+ix+k][i+iy+l] = 1

    return cell, cellmode

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
    if count+cell[xi][yi] == 0:
        return False
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

def evolve(cellin,cellmode,bg,csize,x,y): 
    cellout = cell(x,y,"0",[])[0]
    ncellmode = cell(x,y,"0",[])[0]
    cellin = tuple(cellin)
    for i in range(x):
        for j in range(y):
            if cellmode[i][j]:
                if alive(cellin,i,j,x,y):
                    cellout[i][j] = 1
                    pg.draw.rect(bg, (0,0,255),[csize*i,csize*j, csize-1, csize-1], 0)
                    for k in range(-1,2):
                        for l in range(-1,2):
                            ncellmode[i+k][j+l] = 1
                else:
                    cellout[i][j] = 0
                    pg.draw.rect(bg, (255,255,255),[csize*i,csize*j, csize-1, csize-1], 0)
    return cellout, ncellmode, bg
  
