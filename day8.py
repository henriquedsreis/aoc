"""
Day 8
"""

ex1 = '123456789012'

with open('day8_input_part1.txt') as file:
    day8_input = file.readline()

program = list(map(int, list(day8_input)))
x_axis = 25
y_axis = 6

input = program.copy()


def create_layer_dict(input: list, x: int, y: int):
    layers = dict()
    input.reverse()

    l = 0
    while input:
        layers[l] = []
        for y in range(y_axis):
            for x in range(x_axis):
                layers[l].append(input.pop())
        l += 1
    return layers


p1_layers = create_layer_dict(program, x_axis, y_axis)

layer_fewer_zeros = p1_layers[1]
for l in p1_layers:
    if p1_layers[l].count(0) < layer_fewer_zeros.count(0):
        layer_fewer_zeros = p1_layers[l]

#print(layer_fewer_zeros)
result = layer_fewer_zeros.count(1) * layer_fewer_zeros.count(2)
print(result)

############################################################
# PART 2

ex2 = '0222112222120000'

program = list(map(int, list(day8_input)))
x_axis = 25
y_axis = 6

p2_layers = create_layer_dict(program, x_axis, y_axis)

img = p2_layers[0]
#print(p2_layers)
#print(img)

#render img
for l in range(len(p2_layers.keys())):
    #print(p2_layers[l])
    #print(p2_layers[l], sep='')
    #print('img:' + str(img))
    for xy in range(x_axis * y_axis):
        #print('l=' + str(l) + '. xy = ' + str(xy))
        if img[xy] == 2: #transparent
            img[xy] = p2_layers[l][xy]

#print('-')
#print(img)

#print_img
buffer = []
for xy in range(x_axis * y_axis):
    #print(xy)
    if xy % x_axis == 0:
        print(*buffer, sep='')
        buffer = []
    buffer.append(img[xy])
print(*buffer, sep='')
