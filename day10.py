"""
Day 10
"""
import math
############################################################
# PART 1

with open('day10_part1_input.txt') as file:
    day10_input = file.read()
with open('day10_part1_input1.txt') as file:
    ex1 = file.read()
with open('day10_part1_input2.txt') as file:
    ex2 = file.read()
with open('day10_part1_input3.txt') as file:
    ex3 = file.read()
with open('day10_part1_input4.txt') as file:
    ex4 = file.read()
with open('day10_part1_input5.txt') as file:
    ex5 = file.read()


def calc_dist(p1: tuple, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


def calc_degrees_between(p1: tuple, p2:tuple):
    if round((math.degrees(math.atan2(p2[0]-p1[0], p2[1] - p1[1]))), 3) < 0:
        correction = 360
    else:
        correction = 0
    return round((math.degrees(math.atan2(p2[0]-p1[0], p2[1] - p1[1]))), 3) + correction


str_map = day10_input

# The map and its axis
#print(str_map)

#1 based
x_axis = str_map.index('\n')
y_axis = str_map.count('\n') + 1 #there''s no newline at the end
#print(str(x_axis) + ' by ' + str(y_axis))

#Parsing the map to list
lst_map = list(filter(lambda c: c != '\n', [char for char in str_map]))
#print(lst_map)

#Creating the asteroids maps
asteroid_set = set()

for xy in range(x_axis * y_axis):
    if lst_map[xy] == '#':
        asteroid_set.add((xy % x_axis, xy // y_axis))
        #print('x:' + str(xy % x_axis))
        #print('y:' + str(xy % x_axis))


def update_asteroid_map():
    asteroid_angle_map = dict()
    for asteroid in asteroid_set:

        for target_ast in asteroid_set:

            if asteroid != target_ast:

                angle = calc_degrees_between(asteroid, target_ast)
                if asteroid not in asteroid_angle_map.keys(): # first aligned target for this asteroid, we need to create angle map
                    asteroid_angle_map[asteroid] = dict()

                if angle not in asteroid_angle_map[asteroid]: # first aligned target on this angle
                    asteroid_angle_map[asteroid][angle] = target_ast
                elif calc_dist(asteroid, target_ast) < calc_dist(asteroid, asteroid_angle_map[asteroid][angle]): # we found a closer asteroid on this angle
                    asteroid_angle_map[asteroid][angle] = target_ast
    return asteroid_angle_map


asteroid_angle_map = update_asteroid_map()
asteroid_count = 0
for asteroid, angle_map in asteroid_angle_map.items():
    if len(angle_map.keys()) > asteroid_count:
        asteroid_count = len(angle_map.keys())
        big_d_asteroid = asteroid

print(asteroid_count)
print(big_d_asteroid)


#print(asteroid_set)
#print(asteroid_angle_map)

############################################################
# PART 2

station = big_d_asteroid

print(asteroid_angle_map[station])

laser_angle = 181
i = 0

while len(asteroid_set) != 1 and i < 200: # let''s not destroy ourselves
    station_angle_map = update_asteroid_map()[station]

    next_angles = sorted((angle for angle in list(station_angle_map.keys()) if angle < laser_angle), reverse=True)
    if not next_angles: #full round
        laser_angle = 360
        next_angles = sorted((angle for angle in list(station_angle_map.keys()) if angle < laser_angle), reverse=True)

    laser_angle = next_angles[0]
    print('it: ' + str(i+1) + '. destroying: ' + str(station_angle_map[laser_angle]) + ' at angle ' + str(laser_angle))
    asteroid_set.remove(station_angle_map[laser_angle])

    i += 1


#2518 too high

