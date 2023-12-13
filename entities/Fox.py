class Fox(object):
    
    lifetime = 0
    energy = 0
    flair = 0

    in_motion = False
    gonna_reproduce = False
    baby = False
    is_partner = False

    def __init__(self, lifetime, energy, in_motion, flair):
        self.lifetime = lifetime
        self.energy = energy
        self.en_mouvement = in_motion
        self.flair = flair

    def __str__(self):
        return "Fox"
