"""
Day 6 - Orbit count

Representation:
COM)A
A)B

Direct orbits (always 1, except for COM):
B = 1
A = 1
COM = 0

Indirect orbits (1 + orbits of its star):
B = 2
A = 1
COM = 0

"""

#PART1
STAR_MAP = {}

def get_orbits(obj: str, orb_map: dict):
    if obj == 'COM':
        return 0
    else:
        return 1 + get_orbits(orb_map[obj], orb_map)

#reading input
#with open('day6_input_sample.txt') as file:
with open('day6_input_part2.txt') as file:
    input_d6 = file.read().split('\n')
    input_d6.pop()
    #print(input_d6)

#creating the orbital map
for direct_orb in input_d6:
    star = direct_orb.split(')')[0]
    orb_obj = direct_orb.split(')')[1]
    STAR_MAP[orb_obj] = star

#checking how many orbits
orbit_count = 0
for obj in STAR_MAP.keys():
    orbit_count += get_orbits(obj, STAR_MAP)

#print(orbit_count)

#PART2

print(STAR_MAP)


# comprehensions are SOOOOOO UNINTUITIVE!!
HOP_MAP = {k: set() for k in STAR_MAP.keys()}


for obj in STAR_MAP.keys():
    #can hop to its star
    HOP_MAP[obj].add(STAR_MAP[obj])

    #can hop to its orbiting objects
    for planet, star in STAR_MAP.items():
        if star == obj:
            HOP_MAP[obj].add(planet)

HOP_MAP['COM'] = set()
for planet, star in STAR_MAP.items():
    if star == 'COM':
        HOP_MAP['COM'].add(planet)

print(HOP_MAP)


DEAD_END = set()


def hop_to_san():
    hops = 0
    pos = 'YOU'
    traversed = {'YOU'}
    while pos != 'SAN':
    #for i in range(50):

        #print('--')
        #print('pos: ' + str(pos))
        #print('traversed: ' + str(traversed))
        #print('deadend: ' + str(DEAD_END))

        #if 'SAN' in HOP_MAP[pos]:
        #    break

        for h in HOP_MAP[pos]:
            #print('h:' + str(h) + '. hops=' + str(hops))

            if 'SAN' == h: #found him
                return hops - 2
            elif h in DEAD_END or h in traversed:
                continue
            elif len(HOP_MAP[h] - traversed - DEAD_END) == 0: #dead end
                DEAD_END.add(h)
                hops = 0
                pos = 'YOU'
                traversed = {'YOU'}
                break #reset

            traversed.add(h)
            pos = h
        hops += 1


print(hop_to_san())
