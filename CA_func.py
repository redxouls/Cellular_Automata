def cell(x,y):
    cell =[]
    for i in range(x):
        cell.append([])
        for j in range(y):
                cell[i].append(0)
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
    cellout = cell(x,y)
    cellin = tuple(cellin)
    for i in range(x):
        for j in range(y):
            if alive(cellin,i,j,x,y):
                cellout[i][j] = 1
            else:
                cellout[i][j] = 0
    return cellout
  
