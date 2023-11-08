import random as rng
import copy

import entities.Fox as F
import entities.Rabbit as R

import View

rng.seed(0)


class Model:

    grid = []
    dim = len(grid)
    rabbit_list = []
    fox_list = []

    DIRECTION = ["right", "left", "up", "down", "cornerUR", "cornerUL", "cornerDL", "cornerDR"]
    DIRECTION_COORD = {
        "right": (1, 0),
        "left": (-1, 0),
        "up": (0, 1),
        "down": (0, -1),
        "cornerUR": (1, 1),
        "cornerUL": (-1, 1),
        "cornerDL": (-1, -1),
        "cornerDR": (1, -1)
    }

    turn = 1

    freq_reprod = 1  # must be different from 0
    actual_reprod = int

    # Vars for RABBIT ----------------------------------------------------------------------------------------------- #

    births = int
    freq_birth = int
    actual_birth = int
    lifetime_rabbit = int

    # Vars for FOX ----------------------------------------------------------------------------------------------- #

    flair = int
    lunch = int
    lifetime_fox = int
    energy = 5

    # ------------------------------------------------------------------------------------------------------------- #

    def __init__(self, reproduction, rabbits_birth_freq, rabbits_birth, lunch_value, lifetime_r, lifetime_f):
        self.freq_reprod = reproduction
        self.freq_birth = rabbits_birth_freq
        self.births = rabbits_birth
        self.lunch = lunch_value
        self.lifetime_rabbit = lifetime_r
        self.lifetime_fox = lifetime_f

    # Getters ----------------------------------------------------------------------------------------------------- #
    def get_grid(self):
        return self.grid

    def get_pos_of_everybody(self):
        self.rabbit_list = []
        self.fox_list = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if isinstance(self.grid[i][j], R.Rabbit):
                    self.rabbit_list.append([i, j, self.grid[i][j]])
                if isinstance(self.grid[i][j], F.Fox):
                    self.fox_list.append([i, j, self.grid[i][j]])

    def get_animals_totals(self):
        return sum(self.rabbit_list), sum(self.fox_list)

    def get_at(self, x, y):
        return self.grid[x][y]

    # Setters ---------------------------------------------------------------------------------------------------- #
    def end_motion(self):
        for animal in self.rabbit_list+self.fox_list:
            animal[2].in_motion = False

    # Model ------------------------------------------------------------------------------------------------------- #

    def create_grid(self, n):
        for i in range(n):
            tmp = [0 for _ in range(n)]
            self.grid.append(tmp)
        self.dim = len(self.grid)

    def spawn(self, amount, animal):  # bunny = R.Rabbit(self.lifetime_rabbit, False)
        while amount > 0:
            x, y = rng.randint(0, self.dim - 1), rng.randint(0, self.dim - 1)
            if self.grid[x][y] == 0:
                if animal == "rabbit":
                    self.grid[x][y] = R.Rabbit(self.lifetime_rabbit, False)
                elif animal == "fox":
                    self.grid[x][y] = F.Fox(self.lifetime_rabbit, self.energy, False, self.flair)
                amount -= 1

        self.get_pos_of_everybody()

    def move(self, animal):
        enum_dir = copy.deepcopy(self.DIRECTION)
        while not animal[2].in_motion:
            direction = rng.choice(enum_dir)
            dx, dy = self.DIRECTION_COORD[direction]
            new_x, new_y = animal[0] + dx, animal[1] + dy
            if self.dim-1 > new_x >= 1 and self.dim-1 > new_y >= 1 and self.get_at(new_x, new_y) == 0:
                self.grid[animal[0]][animal[1]] = 0
                animal[0], animal[1] = new_x, new_y
                animal[2].lifetime -= 1
                animal[2].in_motion = True
                self.grid[animal[0]][animal[1]] = animal[2]
            else:
                enum_dir.remove(direction)
                if not enum_dir:
                    animal[2].in_motion = True
                    print("Animal can't move")  # Debugging but needs an action

    def rabbits_move(self):
        for bunny in self.rabbit_list:
            if bunny[2].lifetime <= 0:
                # Rabbit die naturrally
                self.grid[bunny[0]][bunny[1]] = 0
                self.rabbit_list.remove(bunny)
            else:
                self.move(bunny)

    def foxes_move(self):
        for fox in self.fox_list:
            if fox[2].lifetime <= 0:
                # Fox die naturrally
                self.grid[fox[0]][fox[1]] = 0
                self.fox_list.remove(fox)
            else:
                self.move(fox)

    def next_turn(self):
        self.rabbits_move()
        self.foxes_move()
        self.end_motion()

        if self.turn % self.freq_birth == 0:
            self.spawn(self.births, "rabbit")

        self.turn += 1

    def can_breed(self, animal):
        enum_dir = copy.deepcopy(self.DIRECTION)

        while enum_dir:

            direction = rng.choice(enum_dir)
            dx, dy = self.DIRECTION_COORD[direction]
            new_x, new_y = animal[0] + dx, animal[1] + dy
            if isinstance(self.get_at(new_x, new_y), animal):
                if not self.get_at(new_x, new_y).will_repro:
                    return True

        return False

    def breed(self):
        for bunny in self.rabbit_list:
            pass
