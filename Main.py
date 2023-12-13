import time

import Model
import View
import legacy.tkiteasy as tk

# r.seed(0)
INITLAP = 2
FNLAP = 4
NLAP = 5
DVLAP = 200
FRREP = 20  # Fréquence reproduction

INITREN = 2
DVREN = 10
ENREN = 0
MIAM = 3
FLAIR = 7

TOURS = 200

g = tk.ouvrirFenetre(1200, 1200)

m = Model.Model(FRREP, FNLAP, NLAP, MIAM, DVLAP, DVREN)
m.create_grid(10)
m.spawn(INITLAP, "rabbit")
# m.spawn(INITREN, "fox")
grid = View.paint(g, m.get_grid(), [])

while TOURS > 0:
    m.next_turn()
    grid = View.paint(g, m.get_grid(), grid)
    g.actualiser()
    TOURS -= 1
    time.sleep(0.1)

g.attendreClic()
g.fermerFenetre()
