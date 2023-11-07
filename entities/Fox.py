class Fox :
    
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