import random as r

r.seed(0)

class Lapin :
    
    dvlap = 0
    en_mouvement = False
    
    def __init__(self,dv,b) :
        self.dvlap = dv
        self.en_mouvement = b

    def __str__(self) :
        return "Lapin"

class Modele :

    grid = []
    lapins_coord = []
    
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

    # --- Class methods --- #

    def create_grid(self,n) :
        for i in range(n) :
            tmp = [0 for j in range(n)]
            self.grid.append(tmp)

    def can_reproduce(self,x,y) :
        
        can = False
        close = [-1,1]
        where = []

        for i in close :
            for j in close :
                if isinstance(self.grid[x+i][y+j],Lapin) and (self.grid[x+i][y+j].en_mouvement) :
                    return can
        
        return can

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

        # Lapin move

        self.get_coordoones_lapins()

        for i in range(len(self.lapins_coord)) :
            x,y = self.lapins_coord[i]
            l = self.grid[x][y]
            enum = ["right","left","up","down","dur","dul","ddl","ddr"]
            
            while not(l.en_mouvement) :
                l.dvlap -= 1
                di = r.choice(enum)
                ix, iy = self.move(di)
                nx,ny = ix+x,iy+y
                print("nx",nx,"ny",ny)
                print("ix",ix,"iy",iy)
                if (((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0)) :
                    self.grid[x][y] = 0
                    self.grid[nx][ny] = l
                    l.en_mouvement = True
                else :
                    enum.remove(di)
        
        self.end_lapins_move()
        

### MAIN ###


# Debug
def show_matrix(m) :
    for ligne in m:
        for element in ligne:
            print("{:<8}".format(str(element)), end=' ')
        print()

m = Modele()
m.create_grid(10)
m.spawn_lapins(10,5)

print("Turn 1")
grid = m.get_grid()
show_matrix(grid)
print()
m.print_pos_lapins()

print("Turn 2")
m.next_turn()
grid = m.get_grid()
show_matrix(grid)
print()
m.print_pos_lapins()

print("Turn 3")
m.next_turn()
grid = m.get_grid()
show_matrix(grid)
print()
m.print_pos_lapins()