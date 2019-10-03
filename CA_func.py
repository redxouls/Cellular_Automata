def Rule():
    return True
def cell(n):
    cell =[]
    for i in range(n):
        cell.append([])
        for j in range(n):
                cell[i].append(0)
    return cell

def cell_out(cell):  
    n = len(cell)
    cell_out = []
    for k in range(n):
        prin_out = ""
        for i in range(n):
            if cell[k][i]:
                prin_out += "* "
            else:
                prin_out += " "
        cell_out.append(prin_out)
    return cell_out

def alive(cell,x,y):
    count = 0
    n = len(cell)
    for i in range(-1,2):
        for j in range(-1,2):
            x1 = x+i
            y1 = y+j
            if x1<0 or y1<0 or x1>n-1 or y1>n-1 or (i==j and i==0):
                abc=1
            else:
                count += cell[x1][y1]
    if cell[x][y]==1:
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

def evolve(inc): 
    n = len(inc)
    out = cell(n)
    inc = tuple(inc)
    for i in range(n):
        for j in range(n):
            if alive(inc,i,j):
                out[i][j] = 1
            else:
                out[i][j]= 0
    return out
  
