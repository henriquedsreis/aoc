"""
Day 11

0 is black panel
1 is white panel

"""
from intcode import IntCodeProgram, Status
import enum


class Color(enum.Enum):
    BLACK = 0
    WHITE = 1

############################################################
# PART 1

day11_input = [3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,28,2,1008,7,10,2,4,17,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,59,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,81,1006,0,24,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,105,2,6,13,10,1006,0,5,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,134,2,1007,0,10,2,1102,20,10,2,1106,4,10,1,3,1,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,172,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,194,1,103,7,10,1006,0,3,1,4,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,228,2,109,0,10,1,101,17,10,1006,0,79,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,260,2,1008,16,10,1,1105,20,10,1,3,17,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,295,1,1002,16,10,101,1,9,9,1007,9,1081,10,1005,10,15,99,109,641,104,0,104,1,21101,387365733012,0,1,21102,1,336,0,1105,1,440,21102,937263735552,1,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,3451034715,1,1,21101,0,394,0,1105,1,440,21102,3224595675,1,1,21101,0,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337454440,1,21102,428,1,0,1105,1,440,21101,0,825460798308,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21102,1,40,2,21101,0,471,3,21101,461,0,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,1,0,466,109,-2,2105,1,0,0,109,4,2101,0,-1,503,1207,-3,0,10,1006,10,521,21101,0,0,-3,21202,-3,1,1,22102,1,-2,2,21101,1,0,3,21102,540,1,0,1105,1,545,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22102,1,-4,-4,1106,0,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,587,1,0,1105,1,545,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,606,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,22102,1,-1,1,21102,1,628,0,105,1,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

program = day11_input

panel_map = dict()
robot_position = (0,0)
robot_angle = 90

paint_robot = IntCodeProgram(program, [])
new_pos_counter = 0


while paint_robot.status != Status.HALTED:
    #scan current pos
    if robot_position not in panel_map.keys():  # first time at position
        panel_map[robot_position] = Color.BLACK.value
        new_pos_counter += 1

    paint_robot.set_input(panel_map[robot_position])
    paint_color = paint_robot.process()
    rotate_inst = paint_robot.process()

    #paint
    panel_map[robot_position] = paint_color

    #rotate robot
    if rotate_inst == 0:  # turn left
        robot_angle = (robot_angle + 90) % 360
    elif rotate_inst == 1:  # turn right
        robot_angle = (robot_angle - 90) % 360

    #move 1 position
    if robot_angle == 0:
        robot_position = (robot_position[0] + 1, robot_position[1])
    elif robot_angle == 90:
        robot_position = (robot_position[0], robot_position[1] + 1)
    elif robot_angle == 180:
        robot_position = (robot_position[0] - 1, robot_position[1])
    elif robot_angle == 270:
        robot_position = (robot_position[0], robot_position[1] - 1)

#print(panel_map)
print(new_pos_counter)


############################################################
# PART 2


program = day11_input

panel_map = dict()
robot_position = (0,0)
robot_angle = 90

paint_robot = IntCodeProgram(program, [])
new_pos_counter = 0


while paint_robot.status != Status.HALTED:
    #scan current pos
    if robot_position not in panel_map.keys():  # first time at position
        panel_map[robot_position] = Color.WHITE.value
        new_pos_counter += 1

    paint_robot.set_input(panel_map[robot_position])
    paint_color = paint_robot.process()
    rotate_inst = paint_robot.process()

    #paint
    panel_map[robot_position] = paint_color

    #rotate robot
    if rotate_inst == 0:  # turn left
        robot_angle = (robot_angle + 90) % 360
    elif rotate_inst == 1:  # turn right
        robot_angle = (robot_angle - 90) % 360

    #move 1 position
    if robot_angle == 0:
        robot_position = (robot_position[0] + 1, robot_position[1])
    elif robot_angle == 90:
        robot_position = (robot_position[0], robot_position[1] + 1)
    elif robot_angle == 180:
        robot_position = (robot_position[0] - 1, robot_position[1])
    elif robot_angle == 270:
        robot_position = (robot_position[0], robot_position[1] - 1)

#print(new_pos_counter)
print(panel_map.keys())

# img axis
x_axis = abs(max([k[0] for k in panel_map.keys()]))
y_axis = abs(min([k[1] for k in panel_map.keys()]))

img = []
# render img to list
for xy in range(x_axis * y_axis):
    #print(xy)
    if (xy % x_axis, - xy // x_axis) not in panel_map.keys(): #the robot didnt pass there
        img.append(Color.BLACK.value)
    else:
        img.append(panel_map[(xy % x_axis, - xy // x_axis)])

print(img)

#print_img (from day 8)
buffer = []
for xy in range(x_axis * y_axis):
    #print(xy)
    if xy % x_axis == 0:
        print(*buffer, sep='')
        buffer = []
    buffer.append(img[xy])

print(*buffer, sep='')
