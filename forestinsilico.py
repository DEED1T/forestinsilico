import tkiteasy as view
import random as r

# Debug tools
def show_matrix(m) :
    for ligne in m:
        for element in ligne:
            print("{:<8}".format(str(element)), end=' ')
        print()

def bunny_numbers(grid) :
    
    cpt = 0

    for i in range(len(grid)) :
        for j in range(len(grid)) :
            if grid[j][i][0] == 1 :
                cpt+=1

    print("Il y'a ",cpt," lapins")

# Life grid

def create_grid(n) :
    grid = []
    for i in range(n) :
        tmp = [[0,0,False] for j in range(n)]
        grid.append(tmp)

    return grid

# Mechanics
def direction(str) :
    if str == "right":
        return 1,0
    if str == "left":
        return -1,0
    if str == "up":
        return 0,1
    if str == "down":
        return 0,-1
    if str == "dUR":
        return 1,1
    if str  == "dUL":
        return -1,1
    if str == "dDL":
        return -1,-1
    if str == "dDR":
        return 1,-1
    
def reset_move(grid) :
    for i in range(len(grid)) :
        for j in range(len(grid)) :
            grid[i][j][2] = False


def next_turn(grid) :
    
    n,m = len(grid[0]),  len(grid)

    for i in range(n) :
        for j in range(m) :
            if grid[j][i][0] == 1 :

                enum = ["right","left","up","down","dUR","dUL","dDL","dDR"]
                

                #print("Lapin ",i," ", j)
                while not(grid[j][i][2]) and (grid[j][i][0] == 1) :

                    di = r.choice(enum)
                    enum.remove(di)
                    
                    nx,ny = direction(di)
                    
                    #---
                    
                    print(enum)
                    if not(j+ny>9 or j+ny<0 or i+nx>9 or i+nx<0) :
                        if grid[j+ny][i+nx][0] == 1 : 
                            grid[j][i][2] = True
                            grid[j][i][1] -= 1 
                            grid[j+ny][i+nx] = grid[j][i]
                            grid[j][i] = [0,0,False]
                        
                    
                #print("Lapin ",i," ", j, " a bouger")
    
    reset_move(grid)
    bunny_numbers(grid)

# Bunny life

def spawn_bunny(grid, b, dvlap) :
    dim = len(grid)

    while b > 0 :
        x,y = r.randint(0,dim-1), r.randint(0,dim-1)
        if grid[x][y] == [0,0,False] :
            grid[x][y] = [1,dvlap,False]
            b -= 1
        
    return grid

# ----- MAIN ----- # 
forest = create_grid(10)
spawn_bunny(forest,10,5)
show_matrix(forest)
next_turn(forest)
print("Next Turn")
print(" ")
show_matrix(forest)
next_turn(forest)
print("Next Turn")
print(" ")
show_matrix(forest)