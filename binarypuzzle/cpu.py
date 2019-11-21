"""CPU functionality."""

import sys

# Operations Definitions
LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
PRA = 0b


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.SP = 7  #  Stack Pointer
        self.running = False
        # Operations setup
        self.operations = {}
        self.operations[LDI] = self.ldi
        self.operations[PRN] = self.prn
        self.operations[HLT] = self.hlt
        self.operations[MUL] = self.mul
        self.operations[PUSH] = self.stack_push
        self.operations[POP] = self.stack_pop

    def load(self, program):
        """Load a program into memory."""

        address = 0

        with open(program) as instructions:
            for line in instructions:
                if line[0] is "0" or line[0] is "1":
                    self.ram[address] = int(line[:8], 2)
                    address += 1

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def stack_push(self):
        value = self.reg[self.ram_read(self.pc + 1)]
        self.reg[self.SP] -= 1
        self.ram_write(self.reg[self.SP], value)
        self.pc += 2

    def stack_pop(self):
        value = self.ram_read(self.reg[self.SP])
        self.reg[self.ram_read(self.pc + 1)] = value
        self.reg[self.SP] += 1
        self.pc += 2

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

        self.pc += 3

    def mul(self):
        self.alu("MUL", self.ram_read(self.pc + 1),
                 self.ram_read(self.pc + 2))

    def ldi(self):
        """LDI operation to store a variable in register."""
        reg_a = self.ram_read(self.pc + 1)
        reg_b = self.ram_read(self.pc + 2)
        self.reg[reg_a] = reg_b
        self.pc += 3

    def prn(self):
        """Print operation."""
        reg_a = self.ram_read(self.pc + 1)
        print(self.reg[reg_a])
        self.pc += 2

    def hlt(self):
        self.running = False

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
        ir = []
        self.running = True
        while self.running:
            ir.append(self.ram_read(self.pc))
            current_operation = ir[-1]
            try:
                self.operations[current_operation]()
            except:
                raise Exception("Unknown instruction")