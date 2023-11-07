import time

import Model
import View
import legacy.tkiteasy as tk

# r.seed(0)
INITLAP = 30
FNLAP = 4
NLAP = 5
DVLAP = 5
FRREP = 3  # Fréquence reproduction

INITREN = 5
DVREN = 10
ENREN = 0
MIAM = 3
FLAIR = 7

TOURS = 30

g = tk.ouvrirFenetre(1200, 1200)

m = Model.Model(FRREP, FNLAP, NLAP, MIAM, DVLAP, DVREN)
m.create_grid(30)
m.spawn_lapins(INITLAP, DVLAP)
m.spawn_renards(INITREN, DVREN, FLAIR)
list = View.paint(g, m.get_grid(), [])

while TOURS > 0:
    m.next_turn()
    list = View.paint(g, m.get_grid(), list)
    g.actualiser()
    TOURS -= 1
    time.sleep(1.5)

g.attendreClic()
g.fermerFenetre()
