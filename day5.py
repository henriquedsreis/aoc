"""
Two new instructions opcodes:
3 to write to its only parameter, an INPUT
4 to read from its only parameter

----
Parameter modes:
From day 2
parameter mode 0 = position mode -> parameter gets interpreted as a pos

For day 5
parameter mode 1 = intermediate mode -> parameter gets interpreted as a val

instruction = [parameter 3 mode][parameter 2 mode][parameter 1 mode][opcode 1][opcode 2]
missing modes are 0 to the left are 0

"""

POINTER = 0


def get_param(intcode: list, mode: int, param: int):
    if mode == 0:
        return intcode[param]
    if mode == 1:
        return param


#adds
def execute_opcode1(intcode: list, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    p2 = get_param(intcode, param2_mode, param2_index)
    intcode[param3_index] = p1 + p2


#multiplies
def execute_opcode2(intcode: list, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    p2 = get_param(intcode, param2_mode, param2_index)
    intcode[param3_index] = p1 * p2


#writes
def execute_opcode3(intcode: list, param1_index: int):
    intcode[param1_index] = INPUT


#reads
def execute_opcode4(intcode: list, param1_mode: int, param1_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    print(p1)
    return p1


#jump if true
def execute_opcode5(intcode: list, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    p2 = get_param(intcode, param2_mode, param2_index)
    global POINTER

    if p1 != 0:
        POINTER = p2
    else:
        POINTER += 3


#jump if false
def execute_opcode6(intcode: list, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    p2 = get_param(intcode, param2_mode, param2_index)
    global POINTER

    if p1 == 0:
        POINTER = p2
    else:
        POINTER += 3


#less than
def execute_opcode7(intcode: list, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    p2 = get_param(intcode, param2_mode, param2_index)

    if p1 < p2:
        intcode[param3_index] = 1
    else:
        intcode[param3_index] = 0


#less than
def execute_opcode8(intcode: list, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
    p1 = get_param(intcode, param1_mode, param1_index)
    p2 = get_param(intcode, param2_mode, param2_index)

    if p1 == p2:
        intcode[param3_index] = 1
    else:
        intcode[param3_index] = 0


def execute_instruction(intcode: list, start_index: int):

    if start_index >= len(intcode):
        return -1

    operator = intcode[start_index]
    #print('op:' + str(operator))
    #print('p:' + str(POINTER))
    #print(intcode)


    operator_5dig = format(operator, '04d')
    opcode = operator_5dig[-2:]

    param1_mode = int(operator_5dig[1])
    param2_mode = int(operator_5dig[0])

    opcode_int = int(opcode)

    if opcode_int == 1:
        execute_opcode1(intcode, param1_mode, intcode[start_index+1], param2_mode, intcode[start_index+2], intcode[start_index+3])
        return 4
    elif opcode_int == 2:
        execute_opcode2(intcode, param1_mode, intcode[start_index+1], param2_mode, intcode[start_index+2], intcode[start_index+3])
        return 4
    elif opcode_int == 3:
        execute_opcode3(intcode, intcode[start_index+1])
        return 2
    elif opcode_int == 4:
        execute_opcode4(intcode, param1_mode, intcode[start_index+1])
        return 2
    elif opcode_int == 5:
        execute_opcode5(intcode, param1_mode, intcode[start_index+1], param2_mode, intcode[start_index+2])
        return 0
    elif opcode_int == 6:
        execute_opcode6(intcode, param1_mode, intcode[start_index+1], param2_mode, intcode[start_index+2])
        return 0
    elif opcode_int == 7:
        execute_opcode7(intcode, param1_mode, intcode[start_index+1], param2_mode, intcode[start_index+2], intcode[start_index+3])
        return 4
    elif opcode_int == 8:
        execute_opcode8(intcode, param1_mode, intcode[start_index+1], param2_mode, intcode[start_index+2], intcode[start_index+3])
        return 4
    elif opcode_int == 99:
        print('halting')
        return -1
    else:
        print('error')
        return -1


def process(intcode: list):
    return_code = 0
    global POINTER

    while return_code >= 0:
        return_code = execute_instruction(intcode, POINTER)
        POINTER += return_code

    return intcode


#PAR1
INPUT = 1

PROGRAM = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,69,55,225,1001,144,76,224,101,-139,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,60,49,225,1102,51,78,225,1101,82,33,224,1001,224,-115,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,69,5,225,2,39,13,224,1001,224,-4140,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,101,42,44,224,101,-120,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,68,49,224,101,-3332,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,50,27,225,1102,5,63,225,1002,139,75,224,1001,224,-3750,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,102,79,213,224,1001,224,-2844,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1,217,69,224,1001,224,-95,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,36,37,225,1101,26,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,449,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,539,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]
example1 = [1002,4,3,4,33]

#process(PROGRAM)

#PART2
PROGRAM = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,69,55,225,1001,144,76,224,101,-139,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,60,49,225,1102,51,78,225,1101,82,33,224,1001,224,-115,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,69,5,225,2,39,13,224,1001,224,-4140,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,101,42,44,224,101,-120,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,68,49,224,101,-3332,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,50,27,225,1102,5,63,225,1002,139,75,224,1001,224,-3750,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,102,79,213,224,1001,224,-2844,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1,217,69,224,1001,224,-95,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,36,37,225,1101,26,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,449,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,539,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]


INPUT = 5
EXAMPLE2 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
process(PROGRAM)
