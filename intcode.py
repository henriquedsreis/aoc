import enum


class Status(enum.Enum):
    STANDBY = 1
    RUNNING = 2
    HALTED = 3
    ERROR = 4

class IntCodeProgram:
    """
    Runnable intcode program.
    Basically code from day 5, turned into a class
    """
    pointer: int
    program: list
    #program_len: int
    # [input, setting]
    input: list #inputs will get popped, meaning LIFO fashion
    output: int
    status: Status
    relative_base: int

    def __init__(self, incode: list, input: list):
        self.pointer = 0
        self.program = incode
        self.input = input
        self.output = None
        self.status = Status.STANDBY
        self.relative_base = 0

    def set_input(self, input: int):
        if self.status == Status.ERROR:
            return self
        self.input.insert(0, input) #just because in the first run setting is already there
        #print('in: ' + str(self.input))
        return self

    def check_create_mem(self, index: int):
        #print('index:' + str(index) + ' prog_len: ' + str(self.program_len))
        if index > len(self.program) - 1: # we need to more memory
            needed_mem = index - len(self.program) + 1
            self.program.extend([0] * needed_mem)

    def get_param(self, mode: int, param: int):
        if mode == 0: #position
            self.check_create_mem(param)
            return self.program[param]
        elif mode == 1: #immediate
            return param
        elif mode == 2: #relative
            self.check_create_mem(param + self.relative_base)
            return self.program[param + self.relative_base]

    def write_to_pos(self, pos: int, val: int):
        self.check_create_mem(pos)
        #print(pos)
        self.program[pos] = val

    #adds
    def execute_opcode1(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)
        #self.program[param3_index] = p1 + p2
        self.write_to_pos(param3_index, p1 + p2)

    #multiplies
    def execute_opcode2(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)
        #self.program[param3_index] = p1 * p2
        self.write_to_pos(param3_index, p1 * p2)

    #writes (input)
    def execute_opcode3(self, param1_mode: int, param1_index: int):
        #fix 203 error https://www.reddit.com/r/adventofcode/comments/e8aw9j/2019_day_9_part_1_how_to_fix_203_error/
        if param1_mode == 2:
            p1 = self.relative_base + param1_index
        else:
            p1 = param1_index
        #self.program[param1_index] = self.input.pop()
        self.write_to_pos(p1, self.input.pop())

    #reads (output)
    def execute_opcode4(self, param1_mode: int, param1_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        self.output = p1
        #print('output:' + str(self.output))
        self.status = Status.STANDBY

    #jump if true
    def execute_opcode5(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)

        if p1 != 0:
            self.pointer = p2
        else:
            self.pointer += 3

    #jump if false
    def execute_opcode6(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)

        if p1 == 0:
            self.pointer = p2
        else:
            self.pointer += 3

    #less than
    def execute_opcode7(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)

        if p1 < p2:
            #self.program[param3_index] = 1
            self.write_to_pos(param3_index, 1)
        else:
            #self.program[param3_index] = 0
            self.write_to_pos(param3_index, 0)

    #less than
    def execute_opcode8(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)

        if p1 == p2:
            #self.program[param3_index] = 1
            self.write_to_pos(param3_index, 1)
        else:
            #self.program[param3_index] = 0
            self.write_to_pos(param3_index, 0)

    #set relative base
    def execute_opcode9(self, param1_mode: int, param1_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        self.relative_base += p1

    def execute_instruction(self):
        #print('pointer=' + str(self.pointer))

        if self.pointer >= len(self.program):
            self.status = Status.ERROR
            return 0

        operator = self.program[self.pointer]
        #print('op:' + str(operator))
        #print('p:' + str(self.pointer))

        operator_5dig = format(operator, '04d')
        opcode = operator_5dig[-2:]

        param1_mode = int(operator_5dig[1])
        param2_mode = int(operator_5dig[0])

        opcode_int = int(opcode)
        #print('opc: ' + str(opcode_int))
        print(operator_5dig)

        if opcode_int == 1:
            self.execute_opcode1(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 2:
            self.execute_opcode2(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 3:
            self.execute_opcode3(param1_mode, self.program[self.pointer+1])
            return 2
        elif opcode_int == 4:
            self.execute_opcode4(param1_mode, self.program[self.pointer+1])
            return 2
        elif opcode_int == 5:
            self.execute_opcode5(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2])
            return 0
        elif opcode_int == 6:
            self.execute_opcode6(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2])
            return 0
        elif opcode_int == 7:
            self.execute_opcode7(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 8:
            self.execute_opcode8(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 9:
            self.execute_opcode9(param1_mode, self.program[self.pointer+1])
            return 2
        elif opcode_int == 99:
            self.status = Status.HALTED
            #print('halting')
            return 1
        else:
            self.input.pop()
            print('error')
            self.status = Status.ERROR
            return 0

    def process(self):
        if self.status in (Status.ERROR, Status.HALTED):
            return self.output

        self.status = Status.RUNNING

        while self.status not in (Status.HALTED, Status.ERROR, Status.STANDBY):
            #print(self.output)
            #print(self.program)
            return_code = self.execute_instruction()
            self.pointer += return_code
            #print(self.pointer)

        #print('stat:' + str(self.status))
        #print('prog:' + str(self.program))
        #print('pointer:' + str(self.pointer))
        return self.output
