import time

import Model
import View
import legacy.tkiteasy as tk

# r.seed(0)
INITLAP = 20
FNLAP = 4
NLAP = 5
DVLAP = 5
FRREP = 2  # Fréquence reproduction

INITREN = 2
DVREN = 10
ENREN = 0
MIAM = 3
FLAIR = 7

TOURS = 50

g = tk.ouvrirFenetre(1200, 1200)

m = Model.Model(FRREP, FNLAP, NLAP, MIAM, DVLAP, DVREN)
m.create_grid(30)
m.spawn(INITLAP, "rabbit")
m.spawn(INITREN, "fox")
list = View.paint(g, m.get_grid(), [])

while TOURS > 0:
    m.next_turn()
    list = View.paint(g, m.get_grid(), list)
    g.actualiser()
    TOURS -= 1
    time.sleep(0.2)

g.attendreClic()
g.fermerFenetre()
