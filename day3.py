"""
Day 3 - Manhattan distance

R8,U5,L5,D3
U7,R6,D4,L4 = distance 6

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
"""
import numpy as np
import scipy.spatial.distance as dist

#PART1

w1_str = 'R8,U5,L5,D3'
#w2_str = 'U7,R6,D4,L4'

w1 = w1_str.split(',')
#w2 = w2_str.split(',')

print(w1)
#print(w2)

grid = set()
origin = (0, 0)
pos = origin

print(pos)

for move in w1:

    direction = move[0]
    distance = int(move[1:])
    #new_pos = tuple()

    if direction == 'R':
        print(tuple(range(distance)))
    #if move == 'L':
    #    new_pos = map(sum, zip(pos, (-distance, 0)))
    #if move == 'U':
    #    new_pos = map(sum, zip(pos, (0, distance)))
    #if move == 'D':
    #    new_pos = map(sum, zip(pos, (0, -distance)))

    #print(new_pos)

#print(tuple(range(1,10)))