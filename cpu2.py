import sys
from datetime import datetime  # for timer interrupt
# Opcodes:
ADD  = 0b10100000
AND  = 0b10101000
CALL = 0b01010000
CMP  = 0b10100111
DEC  = 0b01100110
DIV  = 0b10100011
HLT  = 0b00000001
INC  = 0b01100101
IRET = 0b00010011
JEQ  = 0b01010101
JLE  = 0b01011001
JLT  = 0b01011000
JMP  = 0b01010100
JNE  = 0b01010110
LD   = 0b10000011
LDI  = 0b10000010
MUL  = 0b10100010
OR   = 0b10101010
POP  = 0b01000110
PRA  = 0b01001000
PRN  = 0b01000111
PUSH = 0b01000101
RET  = 0b00010001
SHL  = 0b10101100
ST   = 0b10000100
SUB  = 0b10100001
XOR  = 0b10101011
# Reserved general-purpose register numbers:
IM = 5
IS = 6
SP = 7
# CMP flags:
FL_LT = 0b100
FL_GT = 0b010
FL_EQ = 0b001
# IS flags
IS_TIMER    = 0b00000001
IS_KEYBOARD = 0b00000010
class CPU:
    def __init__(self):
        self.pc = 0  # program counter
        self.fl = 0  # flags
        self.ie = 1
        self.halted = False
        self.last_timer_int = None
        self.inst_set_pc = False  # True if this instruction set the PC
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.reg[SP] = 0xf4
        self.bt = {  # branch table
            ADD: self.op_add,
            AND: self.op_and,
            CALL: self.op_call,
            CMP: self.op_cmp,
            DEC: self.op_dec,
            DIV: self.op_div,
            HLT: self.op_hlt,
            INC: self.op_inc,
            IRET: self.op_iret,
            JEQ: self.op_jeq,
            JLE: self.op_jle,
            JLT: self.op_jlt,
            JMP: self.op_jmp,
            JNE: self.op_jne,
            LD: self.op_ld,
            LDI: self.op_ldi,
            MUL: self.op_mul,
            OR: self.op_or,
            POP: self.op_pop,
            PRA: self.op_pra,
            PRN: self.op_prn,
            PUSH: self.op_push,
            RET: self.op_ret,
            SHL: self.op_shl,
            ST: self.op_st,
            SUB: self.op_sub,
            XOR: self.op_xor,
        }
    def load(self, filename):
        address = 0
        with open(filename) as fp:
            for line in fp:
                comment_split = line.split("#")
                num = comment_split[0].strip()
                if num == '':  # ignore blanks
                    continue
                val = int(num, 2)
                self.ram[address] = val
                address += 1
    def ram_write(self, mdr, mar):
        self.ram[mar] = mdr
    def ram_read(self, mar):
        return self.ram[mar]
    def push_val(self, val):
        self.reg[SP] -= 1
        self.ram_write(val, self.reg[7])
    def pop_val(self):
        val = self.ram_read(self.reg[7])
        self.reg[SP] += 1
        return val
    def alu(self, op, reg_a, reg_b):
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "AND":
            self.reg[reg_a] &= self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]
        elif op == "DEC":
            self.reg[reg_a] -= 1
        elif op == "INC":
            self.reg[reg_a] += 1
        elif op == "CMP":
            self.fl &= 0x11111000  # clear all CMP flags
            if self.reg[reg_a] < self.reg[reg_b]:
                self.fl |= FL_LT
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.fl |= FL_GT
            else:
                self.fl |= FL_EQ
        elif op == "OR":
            self.reg[reg_a] |= self.reg[reg_b]
        elif op == "SHL":
            self.reg[reg_a] <<= self.reg[reg_b]
        elif op == "XOR":
            self.reg[reg_a] ^= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
    def check_for_timer_int(self):
        """Check the time to see if a timer interrupt should fire."""
        if self.last_timer_int == None:
            self.last_timer_int = datetime.now()
        now = datetime.now()
        diff = now - self.last_timer_int
        if diff.seconds >= 1:  # OK, fire!
            self.last_timer_int = now
            self.reg[IS] |= IS_TIMER
    def handle_ints(self):
        if not self.ie:  # see if interrupts enabled
            return
        # Mask out interrupts
        masked_ints = self.reg[IM] & self.reg[IS]
        for i in range(8):
            # See if the interrupt triggered
            if masked_ints & (1 << i):
                self.ie = 0   # disable interrupts
                self.reg[IS] &= ~(1 << i)  # clear bit for this interrupt
                # Save all the work on the stack
                self.push_val(self.pc)
                self.push_val(self.fl)
                for r in range(7):
                    self.push_val(self.reg[r])
                # Look up the address vector and jump to it
                self.pc = self.ram_read(0xf8 + i)
                break # no more processing
    def trace(self):
        print(f"TRACE: %02X | %02X | %d | %02X %02X %02X |" % (
            self.pc,
            self.fl,
            self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')
        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()
    def run(self):
        while not self.halted:
        # Interrupt cod
            self.check_for_timer_int()     # timer interrupt check
            #self.check_for_keyboard_int()  # keyboard interrupt check
            self.handle_ints()             # see if any interrupts occurre
            # Normal instruction processing
            #self.trace()
            ir = self.ram[self.pc]
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            inst_size = ((ir >> 6) & 0b11) + 1
            self.inst_set_pc = ((ir >> 4) & 0b1) == 1
            if ir in self.bt:
                self.bt[ir](operand_a, operand_b)
            else:
                raise Exception(f"Invalid instruction {hex(ir)} at address {hex(self.pc)}")
            # If the instruction didn't set the PC, just move to the next instruction
            if not self.inst_set_pc:
                self.pc += inst_size
    def op_ldi(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
    def op_prn(self, operand_a, operand_b):
        print(self.reg[operand_a])
    def op_pra(self, operand_a, operand_b):
        print(chr(self.reg[operand_a]), end='')
        sys.stdout.flush()
    def op_add(self, operand_a, operand_b):
        self.alu("ADD", operand_a, operand_b)
    def op_and(self, operand_a, operand_b):
        self.alu("AND", operand_a, operand_b)
    def op_sub(self, operand_a, operand_b):
        self.alu("SUB", operand_a, operand_b)
    def op_mul(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)
    def op_div(self, operand_a, operand_b):
        self.alu("DIV", operand_a, operand_b)
    def op_dec(self, operand_a, operand_b):
        self.alu("DEC", operand_a, None)
    def op_inc(self, operand_a, operand_b):
        self.alu("INC", operand_a, None)
    def op_or(self, operand_a, operand_b):
        self.alu("OR", operand_a, operand_b)
    def op_xor(self, operand_a, operand_b):
        self.alu("XOR", operand_a, operand_b)
    def op_pop(self, operand_a, operand_b):
        self.reg[operand_a] = self.pop_val()
    def op_push(self, operand_a, operand_b):
        self.push_val(self.reg[operand_a])
    def op_call(self, operand_a, operand_b):
        self.push_val(self.pc + 2)
        self.pc = self.reg[operand_a]
    def op_ret(self, operand_a, operand_b):
        self.pc = self.pop_val()
    def op_ld(self, operand_a, operand_b):
        self.reg[operand_a] = self.ram_read(self.reg[operand_b])
    def op_shl(self, operand_a, operand_b):
        self.alu("SHL", operand_a, operand_b)
    def op_st(self, operand_a, operand_b):
        self.ram_write(self.reg[operand_b], self.reg[operand_a])
    def op_jmp(self, operand_a, operand_b):
        self.pc = self.reg[operand_a]
    def op_jeq(self, operand_a, operand_b):
        if self.fl & FL_EQ:
            self.pc = self.reg[operand_a]
        else:
            self.inst_set_pc = False
    def op_jle(self, operand_a, operand_b):
        if self.fl & FL_LT or self.fl & FL_EQ:
            self.pc = self.reg[operand_a]
        else:
            self.inst_set_pc = False
    def op_jlt(self, operand_a, operand_b):
        if self.fl & FL_LT:
            self.pc = self.reg[operand_a]
        else:
            self.inst_set_pc = False
    def op_jne(self, operand_a, operand_b):
        if not self.fl & FL_EQ:
            self.pc = self.reg[operand_a]
        else:
            self.inst_set_pc = False
    def op_cmp(self, operand_a, operand_b):
        self.alu("CMP", operand_a, operand_b)
    def op_iret(self, operand_a, operand_b):
        # restore work from stack
        for i in range(6, -1, -1):
            self.reg[i] = self.pop_val()
        self.fl = self.pop_val()
        self.pc = self.pop_val()
        # enable interrupts
        self.ie = 1
    def op_hlt(self, operand_a, operand_b):
        self.halted = True