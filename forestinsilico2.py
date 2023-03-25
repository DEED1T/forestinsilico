import random as r
import time

from tkiteasy import *

#r.seed(0)

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
        elif self.dvlap == 5 :
            str+="J"
        
        return str

class Renard :
    
    dvren = 0
    enerren = 0
    en_mouvement = False
    gonna_reproduce = False
    flair = 0

    def __init__(self, dv, en, b, f) :
        self.dvren = dv
        self.enerren = en
        self.en_mouvement = b
        self.flair = f

    def __str__(self) :
        return "Fox"

class Modele :

    grid = []
    lapins_coord = []
    renards_coord = []
    
    f = 1  #must be different from 0 on construction : Frequence de reproduction
    f_active = 0
    n = 1 
    n_active = 0
    nb = 1
    m = 1

    dvlap = 0
    dvren = 0

    # m = Modele(FRREP,FNLAP,NLAP,MIAM)


    def __init__(self, r,fnlap,nlap,miam,dvl,dvr) :
        self.f = r
        self.n = fnlap
        self.nb = nlap
        self.m = miam
        self.dvlap = dvl
        self.dvren = dvr
    
    # --- Printers --- #
    
    def print_pos_lapins(self) :
        self.get_coordonnes_lapins()
        for i in range(len(self.lapins_coord)) :
            y,x = self.lapins_coord[i]
            print("Lapin à x:",x," y:",y)

    # --- Getters --- #
    
    def get_grid(self) :
        return self.grid

    def get_coordonnes_lapins(self) :
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

    def get_renards_total_numbers(self) :
        cpt = 0

        for i in range(len(self.grid)) :
            for j in range(len(self.grid)) :
                if isinstance(self.grid[i][j],Renard) :
                    cpt+=1
        
        print(cpt)

    def get_coordonnes_renards(self) :
        self.renards_coord = []
        for i in range(len(self.grid)) :
            for j in range(len(self.grid)) :
                if isinstance(self.grid[i][j],Renard) :
                    self.renards_coord.append((i,j))
    
    # --- Setters --- #
    
    def end_lapins_move(self) :
        self.get_coordonnes_lapins()
        for coords in self.lapins_coord :
            self.grid[coords[0]][coords[1]].en_mouvement = False

    def end_lapins_reproduction(self) :
        self.get_coordonnes_lapins()
        for coords in self.lapins_coord :
            self.grid[coords[0]][coords[1]].gonna_reproduce = False

    def end_renards_move(self) :
        self.get_coordonnes_renards()
        for coords in self.renards_coord :
            self.grid[coords[0]][coords[1]].en_mouvement = False
    # --- Class methods --- #

    def create_grid(self,n) :
        for i in range(n) :
            tmp = [0 for j in range(n)]
            self.grid.append(tmp)

    def can_reproduce(self,x,y) :
        
        if self.grid[x][y].gonna_reproduce :
            return False

        dim = len(self.grid)

        for i in range(-1,2) :
            for j in range(-1,2) :
                if (((x+i < dim) and (x+i >= 0)) and ((y+j < dim) and (y+j >= 0))) :
                    if isinstance(self.grid[x+i][y+j],Lapin) or isinstance(self.grid[x+i][y+j],Renard) :
                        if (isinstance(self.grid[x+i][y+j],Lapin) == isinstance(self.grid[x][y],Lapin)) and not(self.grid[x+i][y+j].gonna_reproduce):
                            self.grid[x+i][y+j].gonna_reproduce = True
                            return True
                        elif (isinstance(self.grid[x+i][y+j],Renard) == isinstance(self.grid[x][y],Renard)) and not(self.grid[x+i][y+j].gonna_reproduce) :
                            if (self.grid[x+i][y+j].enerren >= 5) and (self.grid[x][y].enerren >= 5) :
                                self.grid[x+i][y+j].gonna_reproduce = True
                                self.grid[x+i][y+j].enerren -= 5 
                                self.grid[x][y].enerren -= 5
                                return True 
                    
        return False

    def reproduce(self) :
        
        dim = len(self.grid)
        self.get_coordonnes_lapins()

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
                            #print("blue balls")
                
        self.end_lapins_reproduction()
        
        self.get_coordonnes_renards()

        for renard in self.renards_coord :
            enum = ["right","left","up","down","dur","dul","ddl","ddr"]
            if self.can_reproduce(renard[0],renard[1]) :
                repro = False
                while not(repro) :
                    di = r.choice(enum)
                    ix, iy = self.move(di)
                    nx,ny = ix+renard[0],iy+renard[1]
                    if (((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0)) :
                        baby_renard= Renard(self.dvren,0,False,self.grid[renard[0]][renard[1]].flair)
                        self.grid[nx][ny] = baby_renard
                        repro = True
                    else :
                        enum.remove(di)
                        if not(enum) :
                            repro = True
                            #print("blue balls")

        

    def mange(self,x,y) :
        
        dim = len(self.grid)

        for i in range(-1,2) :
            for j in range(-1,2) :

                if (((x+i < dim) and (x+i >= 0)) and ((y+j < dim) and (y+j >= 0))) :
                    if isinstance(self.grid[x+i][y+j],Lapin) :
                        self.grid[x][y].enerren += self.m
                        self.grid[x+i][y+j] = self.grid[x][y]
                        self.grid[x][y] = 0
                        #print("Renard à mangé lapin à x:",y+j,"y:",x+i)
                        return True
        
        return False

    def renifle(self,x,y,p) :
        
        dim = len(self.grid)
        ren = self.grid[x][y]
        portee = []

        for i in range((-p+1),p) :
            for j in range((-p+1),p) :

                nx = x + i
                ny = y + j

                if (0 <= nx < dim and 0 <= ny < dim) and isinstance(self.grid[nx][ny],Lapin):
                    
                    dis = abs(x - nx) + abs(y - ny)
                    portee.append((dis,nx,ny))

        # Regarde le lapin le plus près et renvoie la direction pour se rapprocher de lui
        if portee :
            close_lapin = min(portee, key=lambda p:p[0])
            #print("Lapin le plus proche à x:", close_lapin[2], "y:",close_lapin[1])
            return close_lapin

        else : 
            return None
        
    def chasse(self,x,y,lapin) :

        dx = lapin[1] - x
        dy = lapin[2] - y
        direction = (min(max(dx, -1), 1), min(max(dy, -1), 1))
        
        return direction

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

    def spawn_renards(self, numbers, dv, en) :
        dim = len(self.grid)

        while numbers > 0 :
            x,y = r.randint(0,dim-1), r.randint(0,dim-1)
            if self.grid[x][y] == 0 :
                fox = Renard(dv, en, False, 10)
                self.grid[x][y] = fox
                numbers -=1

    def next_turn(self) :
        
        dim = len(self.grid)
        self.f_active += 1
        
        if self.f_active == self.f :
            self.f_active = 0
            self.reproduce()
            print("REPRODUCTION")

        

        # Renard Move

        self.get_coordonnes_renards()

        for i in range(len(self.renards_coord)) :
            x,y = self.renards_coord[i]
            #print("renard à x:",y,"y:",x)
            ren = self.grid[x][y]
            enum_r = ["right","left","up","down","dur","dul","ddl","ddr"]

            cherche_lapin = self.renifle(x,y,ren.flair)

            if ren.dvren == 0 :
                self.grid[x][y] = 0
                #print("renard mort!")

            elif self.mange(x,y) :
                ren.en_mouvement = True
                #print("J'ai trop manger donc je ne bouge pas")

            elif cherche_lapin != None :
                dx,dy = self.chasse(x,y,cherche_lapin)
                nx,ny = dx+x,dy+y
                self.grid[x][y] = 0
                self.grid[nx][ny] = ren
                ren.dvren -= 1
                ren.enerren -= 1
                ren.en_mouvement = True
                #print("Je chasse")

            else :

                while not(ren.en_mouvement) :
                    di = r.choice(enum_r)
                    ix, iy = self.move(di)
                    nx,ny = ix+x,iy+y
                    if (((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0)) :
                        #print("renard bouge")
                        self.grid[x][y] = 0
                        self.grid[nx][ny] = ren
                        ren.dvren -= 1
                        ren.enerren -= 1
                        ren.en_mouvement = True
                    else :
                        enum_r.remove(di)
                        if not(enum_r) :
                            ren.en_mouvement = True
                            print("Can't move")
        
        self.end_renards_move()
        
        # Lapin move

        self.get_coordonnes_lapins()

        for i in range(len(self.lapins_coord)) :
            x,y = self.lapins_coord[i]
            l = self.grid[x][y]
            enum_l = ["right","left","up","down","dur","dul","ddl","ddr"]
            
            if l.dvlap == 0 :
                self.grid[x][y] = 0
                #print("lapin mort!") 
            
            else :

                while not(l.en_mouvement) :
                    di = r.choice(enum_l)
                    ix, iy = self.move(di)
                    nx,ny = ix+x,iy+y
                    if (((nx < dim) and (nx >= 0)) and ((ny < dim) and (ny >= 0)) and (self.grid[nx][ny] == 0)) :
                        self.grid[x][y] = 0
                        self.grid[nx][ny] = l
                        l.dvlap -= 1
                        l.en_mouvement = True
                    else :
                        enum_l.remove(di)
                        if not(enum_l) :
                            l.en_mouvement = True
                            print("Can't move")
        
        self.end_lapins_move()
        
        if self.n_active == self.n :
            self.n_active = 0
            self.spawn_lapins(self.nb,self.dvlap)
            print("Spawn lapins")
        

### MAIN ###

def show_matrix(m) :
    for ligne in m:
        for element in ligne:
            print("{:<8}".format(str(element)), end=' ')
        print()

# --- Vue --- #



def paint(grid,list) : 

    erase(list)
    p_list = []

    taille_grid = len(grid)

    case_w = 1000 // taille_grid
    case_h = 1000 // taille_grid

    for i in range(taille_grid) :
        for j in range(taille_grid) :
            
            x1 = i * case_w 
            y1 = j * case_h 
            x2 = ((i + 1) * case_w) 
            y2 = ((j + 1) * case_h) 

            

            if isinstance(grid[i][j],Lapin) :
                p = g.dessinerDisque(x1,y1,10,"green")
                p_list.append(p)

            elif isinstance(grid[i][j],Renard) :
                p = g.dessinerDisque(x1,y1,10,"red")
                p_list.append(p)

    g.actualiser()
    return p_list

def erase(list) :
    if list :
        for c in list :
            g.supprimer(c)


## MAIN ##

INITLAP = 0
FNLAP = 0
NLAP = 0
DVLAP = 0
FRREP = 0 #Fréquence reproduction

INITREN = 0
DVREN = 0
ENREN = 0
MIAM = 0
FLAIR = 0

TOURS = 30


g = ouvrirFenetre(1200,1200)

m = Modele(FRREP,FNLAP,NLAP,MIAM,DVLAP,DVREN)
m.create_grid(30)
m.spawn_lapins(INITLAP,DVLAP)
m.spawn_renards(INITREN,DVREN,FLAIR)
list = paint(m.get_grid(),[])

while(TOURS > 0) :
    m.next_turn()
    list = paint(m.get_grid(),list)
    g.actualiser()
    TOURS -=1
    time.sleep(3)
    
g.attendreClic()
g.fermerFenetre()

