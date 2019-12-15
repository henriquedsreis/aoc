"""
Day 12

"""

class Planet():
    """A planet has a position (x,y,z) and a velocity(vx, vy, vz). Additionally it has potential energy and kinetic energy."""
    position: list
    velocity: list

    def __init__(self, xyz_pos: list):
        self.position = xyz_pos.copy()
        self.velocity = [0,0,0]

    def pot(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kin(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def energy(self):
        return self.pot() * self.kin()

    def __str__(self):
        return str(self.position + self.velocity)

    def apply_velocity(self):
        for i in range(3):
            self.position[i] += self.velocity[i]


def apply_gravity(p1: Planet, p2: Planet):
    """Updates velocity"""
    for axis in range(3):
        if p1.position[axis] > p2.position[axis]:
            p1.velocity[axis] -= 1
            p2.velocity[axis] += 1
        elif p1.position[axis] < p2.position[axis]:
            p1.velocity[axis] += 1
            p2.velocity[axis] -= 1
            # else nothing happens


def print_planets(plist):
    for p in plist:
        print(p)


def calc_energy(plist):
    energy = 0
    for p in plist:
        energy += p.energy()
    return energy

############################################################
# PART 1

day11_input = [[-10, -13, 7], [1, 2, 1], [-15, -3, 13], [3, 7, -4]]
ex1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
ex2 = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

input = day11_input

# create planets
planets = []
for i in input:
    planets.append(Planet(i))


# apply gravity, and then velocity, for T ticks
for t in range(1000):
    #print('step', t)
    #print_planets(planets)

    for p1_i in range(len(planets)):
        for p2_i in range(p1_i, len(planets)):
            if p1_i == p2_i:
                continue
            apply_gravity(planets[p1_i], planets[p2_i])

    for p in planets:
        p.apply_velocity()

# print
print("total:", calc_energy(planets))



############################################################
# PART 2

print('--' * 20)
input = ex2

# create planets
planets = []
for i in input:
    planets.append(Planet(i))

# apply gravity, and then velocity, for T ticks
t = 0
while True:
    #print('step', t)
    #print_planets(planets)

    for p1_i in range(4):
        for p2_i in range(p1_i, 4):
            if p1_i != p2_i:
                apply_gravity(planets[p1_i], planets[p2_i])

    for p in planets:
        p.apply_velocity()

    t += 1
    if t % 100000 == 0:
        print(t)
    if planets[0].velocity == [0,0,0] and planets[1].velocity == [0,0,0] and planets[2].velocity == [0,0,0] and planets[3].velocity == [0,0,0] and planets[0].position == input[0]:
        break

print("step", t)
print_planets(planets)
