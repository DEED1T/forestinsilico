import random as r
import time

r.seed(0)

class Lapin :
    
    dvlap = 0
    en_mouvement = False
    gonna_reproduce = False
    
    def __init__(self,dv,b) :
        self.dvlap = dv
        self.en_mouvement = b

    def __str__(self) :
        str = "Lapin"
        if self.dvlap == 5 :
            str +="B"
        
        return str

class Renard :
    pass

class Modele :

    grid = []
    lapins_coord = []
    f = 1  #must be different from 0 on construction : Frequence de reproduction
    f_active = 0

    def __init__(self, r) :
        self.f = r
    
    # --- Printers --- #
    
    def print_pos_lapins(self) :
        self.get_coordoones_lapins()
        for i in range(len(self.lapins_coord)) :
            y,x = self.lapins_coord[i]
            print("Lapin à x:",x," y:",y)

    # --- Getters --- #
    
    def get_grid(self) :
        return self.grid

    def get_coordoones_lapins(self) :
        self.lapins_coord = []
        for i in range(len(self.grid)) :
            for j in range(len(self.grid)) :
                if isinstance(self.grid[i][j],Lapin) :
                    self.lapins_coord.append((i,j))
    
    def get_lapins_total_numbers(self) :
        cpt = 0

        for i in range(len(self.grid)) :
            for j in range(len(self.grid)) :
                if isinstance(self.grid[i][j],Lapin) :
                    cpt+=1
        
        print(cpt)
    
    # --- Setters --- #
    
    def end_lapins_move(self) :
        self.get_coordoones_lapins()
        for coords in self.lapins_coord :
            self.grid[coords[0]][coords[1]].en_mouvement = False

    def end_lapins_reproduction(self) :
        self.get_coordoones_lapins()
        for coords in self.lapins_coord :
            self.grid[coords[0]][coords[1]].gonna_reproduce = False

    # --- Class methods --- #

    def create_grid(self,n) :
        for i in range(n) :
            tmp = [0 for j in range(n)]
            self.grid.append(tmp)

    def can_reproduce(self,x,y) :
        
        if self.grid[x][y].gonna_reproduce :
            return False

        dim = len(self.grid)

        close = [-1,1]

        for i in close :
            for j in close :
                if (((x+i < dim) and (x+i >= 0)) and ((y+j < dim) and (y+j >= 0))) :
                    if isinstance(self.grid[x+i][y+j],Lapin) and not(self.grid[x+i][y+j].gonna_reproduce):
                        self.grid[x+i][y+j].gonna_reproduce = True
                        return True
                    
        return False

    def reproduce(self) :
        
        dim = len(self.grid)
        self.get_coordoones_lapins()

        for lapins in self.lapins_coord :
            enum = ["right","left","up","down","dur","dul","ddl","ddr"]
            if self.can_reproduce(lapins[0],lapins[1]) :
                repro = False
                while not(repro) :
                    di = r.choice(enum)
                    ix, iy = self.move(di)
                    nx,ny = ix+lapins[0],iy+lapins[1]
                    if (((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0)) :
                        baby_lapin = Lapin(5,False)
                        self.grid[nx][ny] = baby_lapin
                        repro = True
                    else :
                        enum.remove(di)
                        if not(enum) :
                            repro = True
                            print("blue balls")
                

        self.end_lapins_reproduction()

    def move(self,str) :
        if str == "right":
            return 1,0
        if str == "left":
            return -1,0
        if str == "up":
            return 0,1
        if str == "down":
            return 0,-1
        if str == "dur":
            return 1,1
        if str  == "dul":
            return -1,1
        if str == "ddl":
            return -1,-1
        if str == "ddr":
            return 1,-1

    def spawn_lapins(self,numbers, dv) :
        dim = len(self.grid)

        while numbers > 0 :
            x,y = r.randint(0,dim-1), r.randint(0,dim-1)
            if self.grid[x][y] == 0 :
                bunny = Lapin(dv, False)
                self.grid[x][y] = bunny
                numbers -=1

    def next_turn(self) :
        
        dim = len(self.grid)
        self.f_active += 1

        # Lapin move

        self.get_coordoones_lapins()

        for i in range(len(self.lapins_coord)) :
            x,y = self.lapins_coord[i]
            l = self.grid[x][y]
            enum = ["right","left","up","down","dur","dul","ddl","ddr"]
            
            if l.dvlap == 0 :
                self.grid[x][y] = 0
                print("mort!")
            
            else :

                while not(l.en_mouvement) :
                    di = r.choice(enum)
                    ix, iy = self.move(di)
                    nx,ny = ix+x,iy+y
                    if (((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0)) :
                        self.grid[x][y] = 0
                        self.grid[nx][ny] = l
                        l.dvlap -= 1
                        l.en_mouvement = True
                    else :
                        enum.remove(di)
                        if not(enum) :
                            l.en_mouvement = True
                            print("Can't move")
        
        self.end_lapins_move()
        
        if self.f_active == self.f :
            self.f_active = 0
            self.reproduce()
            print("REPRODUCTION")
        
        

### MAIN ###


# Debug
def show_matrix(m) :
    for ligne in m:
        for element in ligne:
            print("{:<8}".format(str(element)), end=' ')
        print()

m = Modele(2)
m.create_grid(10)
m.spawn_lapins(30,5)
print("Turn 0")
grid = m.get_grid()
show_matrix(grid)
print()

for i in range(1,11) :

    print("Turn", i)
    m.next_turn()
    grid = m.get_grid()
    show_matrix(grid)
    print()
    #m.print_pos_lapins()
    time.sleep(2.5)

