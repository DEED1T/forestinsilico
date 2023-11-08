import random as r

import entities.Fox as Renard
import entities.Rabbit as Lapin


class ModelLegacy:
    grid = []
    lapins_coord = []
    renards_coord = []

    f = 1  # must be different from 0 on construction : Frequence de reproduction
    f_active = 0
    n = 1
    n_active = 0
    nb = 1
    m = 1

    def __init__(self, r, fnlap, nlap, miam, dvl, dvr):
        self.f = r
        self.n = fnlap
        self.nb = nlap
        self.m = miam
        self.dvlap = dvl
        self.dvren = dvr

    # Printers ---------------------------------------------------------------------------------------------------- #

    def print_pos_lapins(self):
        self.get_coordonnes_lapins()
        for i in range(len(self.lapins_coord)):
            y, x = self.lapins_coord[i]
            print("Lapin à x:", x, " y:", y)

    # Getters ----------------------------------------------------------------------------------------------------- #

    def get_grid(self):
        return self.grid

    def get_coordonnes_lapins(self):
        self.lapins_coord = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if isinstance(self.grid[i][j], Lapin.Rabbit):
                    self.lapins_coord.append((i, j))

    def get_lapins_total_numbers(self):
        cpt = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if isinstance(self.grid[i][j], Lapin.Rabbit):
                    cpt += 1

        print(cpt)

    def get_coordonnes_renards(self):
        self.renards_coord = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if isinstance(self.grid[i][j], Renard.Fox):
                    self.renards_coord.append((i, j))

    def get_renards_total_numbers(self):
        cpt = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if isinstance(self.grid[i][j], Renard.Fox):
                    cpt += 1

        print(cpt)

    def getatcoord(self, x, y):
        return self.grid[x][y]

    # Setters ---------------------------------------------------------------------------------------------------- #

    def end_lapins_move(self):
        self.get_coordonnes_lapins()
        for coords in self.lapins_coord:
            self.getatcoord(coords[0], coords[1]).en_mouvement = False

    def end_lapins_reproduction(self):
        self.get_coordonnes_lapins()
        for coords in self.lapins_coord:
            self.getatcoord(coords[0], coords[1]).gonna_reproduce = False

    def end_renards_move(self):
        self.get_coordonnes_renards()
        for coords in self.renards_coord:
            self.getatcoord(coords[0], coords[1]).en_mouvement = False

    # Static Methods -------------------------------------------------------------------------------------------- #

    @staticmethod
    def chasse(x, y, lapin):

        dx = lapin[1] - x
        dy = lapin[2] - y
        direction = (min(max(dx, -1), 1), min(max(dy, -1), 1))

        return direction

    @staticmethod
    def move(direction):
        if direction == "right":
            return 1, 0
        if direction == "left":
            return -1, 0
        if direction == "up":
            return 0, 1
        if direction == "down":
            return 0, -1
        if direction == "dur":
            return 1, 1
        if direction == "dul":
            return -1, 1
        if direction == "ddl":
            return -1, -1
        if direction == "ddr":
            return 1, -1

    # Model ------------------------------------------------------------------------------------------------------- #

    def create_grid(self, n):
        for i in range(n):
            tmp = [0 for _ in range(n)]
            self.grid.append(tmp)

    def can_reproduce(self, x, y):

        if self.grid[x][y].gonna_reproduce:
            return False

        dim = len(self.grid)

        for i in range(-1, 2):
            for j in range(-1, 2):
                if ((x + i < dim) and (x + i >= 0)) and ((y + j < dim) and (y + j >= 0)):
                    if isinstance(self.grid[x + i][y + j], Lapin.Rabbit) or isinstance(self.grid[x + i][y + j], Renard.Fox):
                        if (isinstance(self.grid[x + i][y + j], Lapin.Rabbit) == isinstance(self.grid[x][y], Lapin.Rabbit)) and not (
                                self.grid[x + i][y + j].gonna_reproduce):
                            self.grid[x + i][y + j].gonna_reproduce = True
                            return True
                        elif (isinstance(self.grid[x + i][y + j], Renard.Fox) == isinstance(self.grid[x][y], Renard.Fox)) and not (
                                self.grid[x + i][y + j].gonna_reproduce):
                            if (self.grid[x + i][y + j].enerren >= 5) and (self.grid[x][y].enerren >= 5):
                                self.grid[x + i][y + j].gonna_reproduce = True
                                self.grid[x + i][y + j].enerren -= 5
                                self.grid[x][y].enerren -= 5
                                return True

        return False

    def reproduce(self):

        dim = len(self.grid)
        self.get_coordonnes_lapins()

        for lapins in self.lapins_coord:
            enum = ["right", "left", "up", "down", "dur", "dul", "ddl", "ddr"]
            if self.can_reproduce(lapins[0], lapins[1]):
                repro = False
                while not repro:
                    di = r.choice(enum)
                    ix, iy = self.move(di)
                    nx, ny = ix + lapins[0], iy + lapins[1]
                    if ((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0):
                        baby_lapin = Lapin.Rabbit(5, False)
                        self.grid[nx][ny] = baby_lapin
                        repro = True
                    else:
                        enum.remove(di)
                        if not enum:
                            repro = True

        self.end_lapins_reproduction()

        self.get_coordonnes_renards()

        for renard in self.renards_coord:
            enum = ["right", "left", "up", "down", "dur", "dul", "ddl", "ddr"]
            if self.can_reproduce(renard[0], renard[1]):
                repro = False
                while not repro:
                    di = r.choice(enum)
                    ix, iy = self.move(di)
                    nx, ny = ix + renard[0], iy + renard[1]
                    if ((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0):
                        baby_renard = Renard.Fox(self.dvren, 0, False, self.grid[renard[0]][renard[1]].flair)
                        self.grid[nx][ny] = baby_renard
                        repro = True
                    else:
                        enum.remove(di)
                        if not (enum):
                            repro = True
                            # print("blue balls")

    def mange(self, x, y):

        dim = len(self.grid)

        for i in range(-1, 2):
            for j in range(-1, 2):

                if ((x + i < dim) and (x + i >= 0)) and ((y + j < dim) and (y + j >= 0)):
                    if isinstance(self.grid[x + i][y + j], Lapin.Rabbit):
                        self.grid[x][y].enerren += self.m
                        self.grid[x + i][y + j] = self.grid[x][y]
                        self.grid[x][y] = 0
                        # print("Renard à mangé lapin à x:",y+j,"y:",x+i)
                        return True

        return False

    def renifle(self, x, y, p):

        dim = len(self.grid)
        ren = self.grid[x][y]
        portee = []

        for i in range((-p + 1), p):
            for j in range((-p + 1), p):

                nx = x + i
                ny = y + j

                if (0 <= nx < dim and 0 <= ny < dim) and isinstance(self.grid[nx][ny], Lapin.Rabbit):
                    dis = abs(x - nx) + abs(y - ny)
                    portee.append((dis, nx, ny))

        # Regarde le lapin le plus près et renvoie la direction pour se rapprocher de lui
        if portee:
            close_lapin = min(portee, key=lambda p: p[0])
            # print("Lapin le plus proche à x:", close_lapin[2], "y:",close_lapin[1])
            return close_lapin

        else:
            return None

    def spawn_lapins(self, numbers, dv):
        dim = len(self.grid)

        while numbers > 0:
            x, y = r.randint(0, dim - 1), r.randint(0, dim - 1)
            if self.grid[x][y] == 0:
                bunny = Lapin.Rabbit(dv, False)
                self.grid[x][y] = bunny
                numbers -= 1

    def spawn_renards(self, numbers, dv, en):
        dim = len(self.grid)

        while numbers > 0:
            x, y = r.randint(0, dim - 1), r.randint(0, dim - 1)
            if self.grid[x][y] == 0:
                fox = Renard.Fox(dv, en, False, 10)
                self.grid[x][y] = fox
                numbers -= 1

    def next_turn(self):

        dim = len(self.grid)
        self.f_active += 1

        if self.f_active == self.f:
            self.f_active = 0
            self.reproduce()
            print("REPRODUCTION")

        # Renard Move

        self.get_coordonnes_renards()

        for i in range(len(self.renards_coord)):
            x, y = self.renards_coord[i]
            # print("renard à x:",y,"y:",x)
            ren = self.grid[x][y]
            enum_r = ["right", "left", "up", "down", "dur", "dul", "ddl", "ddr"]

            cherche_lapin = self.renifle(x, y, ren.flair)

            if ren.dvren == 0:
                self.grid[x][y] = 0
                # print("renard mort!")

            elif self.mange(x, y):
                ren.en_mouvement = True
                # print("J'ai trop manger donc je ne bouge pas")

            elif cherche_lapin is not None:
                dx, dy = self.chasse(x, y, cherche_lapin)
                nx, ny = dx + x, dy + y
                if ((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0):

                    self.grid[x][y] = 0
                    self.grid[nx][ny] = ren
                    ren.dvren -= 1
                    ren.enerren -= 1
                    ren.en_mouvement = True
                    # print("Je chasse")
                else:
                    ren.en_mouvement = True

            else:

                while not ren.en_mouvement:
                    di = r.choice(enum_r)
                    ix, iy = self.move(di)
                    nx, ny = ix + x, iy + y
                    if ((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0):
                        # print("renard bouge")
                        self.grid[x][y] = 0
                        self.grid[nx][ny] = ren
                        ren.dvren -= 1
                        ren.enerren -= 1
                        ren.en_mouvement = True
                    else:
                        enum_r.remove(di)
                        if not enum_r:
                            ren.en_mouvement = True
                            print("Can't move")

        self.end_renards_move()

        # Lapin move

        self.get_coordonnes_lapins()

        for i in range(len(self.lapins_coord)):
            x, y = self.lapins_coord[i]
            l = self.grid[x][y]
            enum_l = ["right", "left", "up", "down", "dur", "dul", "ddl", "ddr"]

            if l.dvlap == 0:
                self.grid[x][y] = 0
                # print("lapin mort!")

            else:

                while not l.en_mouvement:
                    di = r.choice(enum_l)
                    ix, iy = self.move(di)
                    nx, ny = ix + x, iy + y
                    if ((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0):
                        self.grid[x][y] = 0
                        self.grid[nx][ny] = l
                        l.dvlap -= 1
                        l.en_mouvement = True
                    else:
                        enum_l.remove(di)
                        if not enum_l:
                            l.en_mouvement = True
                            print("Can't move")

        self.end_lapins_move()

        if self.n_active == self.n:
            self.n_active = 0
            self.spawn_lapins(self.nb, self.dvlap)
            print("Spawn lapins")
