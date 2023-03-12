import tkiteasy as view
import random as r

# Debug tools
def show_matrix(m) :
    for ligne in m:
        for element in ligne:
            print("{:<8}".format(str(element)), end=' ')
        print()


# Life grid

def create_grid(n) :
    grid = []
    for i in range(n) :
        tmp = [0 for j in range(n)]
        grid.append(tmp)

    return grid

# Mechanics
def direction() :
    pass

def next_turn() :
    pass

# Bunny life

def spawn_bunny(grid, b, dvlap) :
    dim = len(grid)

    while b > 0 :
        x,y = r.randint(0,dim-1), r.randint(0,dim-1)
        if grid[x][y] == 0 :
            grid[x][y] = [1,dvlap]
            b -= 1
        
    return grid

# ----- MAIN ----- #
forest = create_grid(10)
spawn_bunny(forest,10,5)
show_matrix(forest)
