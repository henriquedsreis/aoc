"""
Day 2 - Intcode

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""
PROGRAM_LEN = 4


def execute_opcode1(intcode: list, param1_index: int, param2_index: int, write_index: int):
    intcode[write_index] = intcode[param1_index] + intcode[param2_index]


def execute_opcode2(intcode: list, param1_index: int, param2_index: int, write_index: int):
    intcode[write_index] = intcode[param1_index] * intcode[param2_index]


def execute_instruction(intcode: list, start_index: int, index_leng: int):
    program = intcode[start_index:start_index+index_leng]

    if start_index >= len(intcode):
        return False

    opcode = program[0]
    if opcode == 1:
        execute_opcode1(intcode, intcode[start_index+1], intcode[start_index+2], intcode[start_index+3])
        return True
    elif opcode == 2:
        execute_opcode2(intcode, intcode[start_index+1], intcode[start_index+2], intcode[start_index+3])
        return True
    elif opcode == 99:
        #print('halting')
        return False
    else:
        print('error')
        return False


def process(intcode: list):
    instruction_pointer = 0
    return_code = True

    while return_code:
        return_code = execute_instruction(intcode, instruction_pointer, PROGRAM_LEN)
        instruction_pointer += PROGRAM_LEN

    return intcode

#PART1
mem = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
print(process(mem))

#PART2
for noun in range(0, 99):
    for verb in range(0, 99):
        mem_in = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
        mem_out = process(mem_in)
        if mem_out[0] == 19690720:
            print(mem_in)
            print(100*noun+verb)
            break
