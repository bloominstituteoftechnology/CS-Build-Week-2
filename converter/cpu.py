"""CPU functionality."""

import sys
HLT = 0x01   # Halt CPU and exit emulator
LDI = 0x82   # Set value of register to integer
PRN = 0x47   # Print numeric value stored in register
MUL = 0xA2   # Multiply values in two registers and store the result in first register
ADD = 0xA0   # Add values in two registers and store the result in first register
POP = 0x46   # Pop the value at the top of the stack into the given register
PUSH = 0x45  # Push value in given register on stack
CALL = 0x50  # Call subroutine at address stored in register
RET = 0x11   # Return from a subroutine
CMP = 0xA7   # Compare the values in two registers
JMP = 0x54   # Jump to the address stored in the given register.
JEQ = 0x55   # If equal flag is true, jump to address stored in the given register
JNE = 0x56   # If E flag is false, jump to address stored in the given register
AND = 0xA8   # AND registerA and registerB, store  result in registerA
OR = 0x69    # OR registerA and registerB, store  result in registerA
XOR = 0xAB   # XOR registerA and registerB, store  result in registerA
NOT = 0x69   # NOT in given register
SHL = 0xAC   # Shift registerA left by bits in registerB, filling the low bits with 0
SHR = 0xAD   # Shift registerA right by bits in registerB, filling the high bits with 0
MOD = 0xA4   # Divide first register by second, store >>remainder<< of the result in registerA
PRA = 0x48


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 0x100
        self.reg = [0] * 0x08
        self.pc = 0
        self.mar = 0
        self.mdr = 0
        self.fl = 0x00
        self.sp = 0xF4
        self.branchtable = {
            HLT: self.hlt,
            LDI: self.ldi,
            PRN: self.prn,
            POP: self.pop,
            PUSH: self.push,
            CALL: self.call,
            RET: self.ret,
            CMP: self.cmp,
            JMP: self.jmp,
            JEQ: self.jeq,
            JNE: self.jne,
            PRA: self.pra,
            'ALU': {
                ADD: self.alu,
                MUL: self.alu,
                AND: self.alu,
                OR: self.alu,
                XOR: self.alu,
                NOT: self.alu,
                SHL: self.alu,
                SHR: self.alu,
                MOD: self.alu,
            }
        }
        self.room_lines = []

    def load(self, path):
        """Load a program into memory."""

        address = 0

        f = open(path)
        program = f.read().splitlines()
        f.close()

        for index, line in enumerate(program):
            comment = line.find('#')
            if comment != -1:
                line = line[:comment]
            if line != '':
                line = int(line.strip(), 2)
            program[index] = line

        while '' in program:
            program.remove('')

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def hlt(self, *args):
        with open('room.ls8', 'w') as outfile:
            outfile.truncate()
            outfile.write(''.join(self.room_lines[-3:]))
        exit()

    def ldi(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b

    def prn(self, operand_a, *args):
        print(self.reg[operand_a])

    def pra(self, *args):
        op_a = self.ram_read(self.pc + 1)
        print_ascii = chr(self.reg[op_a])
        # print(print_ascii)
        self.room_lines.append(print_ascii)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == ADD:
            self.reg[reg_a] += self.reg[reg_b]
        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == AND:
            self.reg[reg_a] = (self.reg[reg_a] & self.reg[reg_b])
        elif op == OR:
            self.reg[reg_a] = (self.reg[reg_a] | self.reg[reg_b])
        elif op == XOR:
            self.reg[reg_a] = (self.reg[reg_a] ^ self.reg[reg_b])
        elif op == NOT:
            self.reg[reg_a] = (~ self.reg[reg_a])
        elif op == SHL:
            self.reg[reg_a] = (self.reg[reg_a] << self.reg[reg_b])
        elif op == SHR:
            self.reg[reg_a] = (self.reg[reg_a] >> self.reg[reg_b])
        elif op == MOD:
            self.reg[reg_a] = (self.reg[reg_a] % self.reg[reg_b])
        else:
            raise Exception("Unsupported ALU operation")

    def pop(self, operand_a, *args):
        """
        Copy val from sp to given register
        Increments sp
        """
        val = self.ram_read(self.sp)
        self.reg[operand_a] = val
        self.sp += 1

    def push(self, operand_a, *args):
        """
        Decrements sp
        Copy value in given register to sp
        """
        self.sp -= 1
        self.ram_write(self.sp, self.reg[operand_a])

    def call(self, operand_a, *args):
        """
        The address of the instruction directly after CALL is
        pushed onto the stack. This allows us to return to where
        we left off when the subroutine finishes executing.

        The PC is set to the address stored in the given register.
        We jump to that location in RAM and execute the first
        instruction in the subroutine. The PC can move forward or
        backwards from its current location.
        """
        self.sp -= 1
        self.ram_write(self.sp, self.pc)
        self.push(operand_a)
        self.pc = self.mdr - 2

    def ret(self, *args):
        """
        Pop the value from the top of the stack and store it in the PC
        """
        self.pop(self.mdr)
        self.pc = self.ram[self.sp] + 1

    def cmp(self, a, b):
        if self.reg[a] == self.reg[b]:
            self.fl = 0x01
        elif self.reg[a] > self.reg[b]:
            self.fl = 0x02
        else:
            self.fl = 0x03

    def jmp(self, a, *args):
        self.pc = self.reg[a] - 2

    def jeq(self, a, *args):
        if f'{self.fl:x}' == f'{0x01}':
            self.pc = self.reg[a] - 2

    def jne(self, a, *args):
        if f'{self.fl:x}' != f'{0x01}':
            self.pc = self.reg[a] - 2

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while True:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if ir in self.branchtable:
                self.branchtable[ir](operand_a, operand_b)
                self.pc += (ir >> 6) + 1

            elif ir in self.branchtable['ALU']:
                self.branchtable['ALU'][ir](ir, operand_a, operand_b)
                self.pc += (ir >> 6) + 1

            else:
                print(f'{ir:b} not supported')
                self.pc += 1

    def ram_read(self, address):
        self.mar = address
        self.mdr = self.ram[address]
        return self.mdr

    def ram_write(self, address, value):
        self.mar = address
        self.mdr = value
        self.ram[self.mar] = self.mdr
