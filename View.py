import legacy.tkiteasy as tk
import entities.Fox as Fox
import entities.Rabbit as Rabbit


def show_matrix(m):
    for ligne in m:
        for element in ligne:
            print("{:<8}".format(str(element)), end=' ')
        print()


def paint(display, grid, list):

    def erase(list):
        if list:
            for c in list:
                display.supprimer(c)

    erase(list)
    p_list = []

    taille_grid = len(grid)

    case_w = 1000 // taille_grid
    case_h = 1000 // taille_grid

    for i in range(taille_grid):
        for j in range(taille_grid):

            x1 = i * case_w
            y1 = j * case_h

            if isinstance(grid[i][j], Rabbit.Rabbit):
                # infos = "i:", i , " j:" , j , " M:" , grid[i][j].in_motion, grid[i][j].lifetime
                # p = display.afficherTexte(infos, x1, y1)
                p = display.dessinerDisque(x1, y1, 10, "green")
                p_list.append(p)

            elif isinstance(grid[i][j], Fox.Fox):
                p = display.dessinerDisque(x1, y1, 10, "red")
                p_list.append(p)

    display.actualiser()
    return p_list
