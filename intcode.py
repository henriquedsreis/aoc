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
    # [input, setting]
    input: list #inputs will get popped, meaning LIFO fashion
    output: int
    status: Status

    def __init__(self, incode: list, input: list):
        self.pointer = 0
        self.program = incode
        self.input = input
        self.status = Status.STANDBY

    def set_input(self, input: int):
        if self.status == Status.ERROR:
            return self
        self.input.insert(0, input) #just because in the first run setting is already there
        #print('in: ' + str(self.input))
        return self

    def get_param(self, mode: int, param: int):
        if mode == 0:
            return self.program[param]
        if mode == 1:
            return param

    #adds
    def execute_opcode1(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)
        self.program[param3_index] = p1 + p2

    #multiplies
    def execute_opcode2(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)
        self.program[param3_index] = p1 * p2

    #writes (input)
    def execute_opcode3(self, param1_index: int):
        self.program[param1_index] = self.input.pop()

    #reads (output)
    def execute_opcode4(self, param1_mode: int, param1_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        self.output = p1
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
            self.program[param3_index] = 1
        else:
            self.program[param3_index] = 0

    #less than
    def execute_opcode8(self, param1_mode: int, param1_index: int, param2_mode: int, param2_index: int, param3_index: int):
        p1 = self.get_param(param1_mode, param1_index)
        p2 = self.get_param(param2_mode, param2_index)

        if p1 == p2:
            self.program[param3_index] = 1
        else:
            self.program[param3_index] = 0

    def execute_instruction(self):

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
        #print(opcode_int)

        if opcode_int == 1:
            self.execute_opcode1(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 2:
            self.execute_opcode2(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 3:
            self.execute_opcode3(self.program[self.pointer+1])
            return 2
        elif opcode_int == 4:
            self.execute_opcode4(param1_mode, self.program[self.pointer+1])
            return 2
        elif opcode_int == 5:
            self.execute_opcode5(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2])
            return 0
        elif opcode_int == 6:
            self.execute_opcode6( param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2])
            return 0
        elif opcode_int == 7:
            self.execute_opcode7(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 8:
            self.execute_opcode8(param1_mode, self.program[self.pointer+1], param2_mode, self.program[self.pointer+2], self.program[self.pointer+3])
            return 4
        elif opcode_int == 99:
            self.status = Status.HALTED
            return 0
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
            return_code = self.execute_instruction()
            self.pointer += return_code

        #print('stat:' + str(self.status))
        return self.output

