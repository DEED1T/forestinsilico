class Rabbit:
    
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
