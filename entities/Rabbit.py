import random as rng

rng.seed(1)


class Rabbit(object):
    
    lifetime = int

    in_motion = False
    will_repro = False
    baby = False

    def __init__(self, lifetime, in_motion):
        self.lifetime = lifetime
        self.in_motion = in_motion

    def __str__(self):
        return str(id(self))

    def set_baby(self, boolean):
        self.baby = boolean
