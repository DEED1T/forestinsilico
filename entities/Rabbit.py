import random as rng

rng.seed(1)


class Rabbit(object):
    
    lifetime = int

    in_motion = False
    will_reproduce = False
    baby = False
    is_partner = False
    sterile = False

    def __init__(self, lifetime, in_motion, baby=False):
        self.lifetime = lifetime
        self.in_motion = in_motion
        self.baby = baby

    def __str__(self):
        return "Partner : " + str(self.is_partner) + " WRepro : " + str(self.will_reproduce)

    def set_baby(self, boolean):
        self.baby = boolean
