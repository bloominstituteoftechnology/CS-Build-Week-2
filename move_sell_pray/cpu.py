"""CPU functionality."""

import sys


    # f'self.{i.keys}' = 
# for i in OPCODES:
#     print(vars('self').i)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.OPCODES = {
    "ADD":  {"type": 2, "code": "10100000"},
    "AND":  {"type": 2, "code": "10101000"},
    "CALL": {"type": 1, "code": "01010000"},
    "CMP":  {"type": 2, "code": "10100111"},
    "DEC":  {"type": 1, "code": "01100110"},
    "DIV":  {"type": 2, "code": "10100011"},
    "HLT":  {"type": 0, "code": "00000001"},
    "INC":  {"type": 1, "code": "01100101"},
    "INT":  {"type": 1, "code": "01010010"},
    "IRET": {"type": 0, "code": "00010011"},
    "JEQ":  {"type": 1, "code": "01010101"},
    "JGE":  {"type": 1, "code": "01011010"},
    "JGT":  {"type": 1, "code": "01010111"},
    "JLE":  {"type": 1, "code": "01011001"},
    "JLT":  {"type": 1, "code": "01011000"},
    "JMP":  {"type": 1, "code": "01010100"},
    "JNE":  {"type": 1, "code": "01010110"},
    "LD":   {"type": 2, "code": "10000011"},
    "LDI":  {"type": 8, "code": "10000010"},
    "MOD":  {"type": 2, "code": "10100100"},
    "MUL":  {"type": 2, "code": "10100010"},
    "NOP":  {"type": 0, "code": "00000000"},
    "NOT":  {"type": 1, "code": "01101001"},
    "OR":   {"type": 2, "code": "10101010"},
    "POP":  {"type": 1, "code": "01000110"},
    "PRA":  {"type": 1, "code": "01001000"},
    "PRN":  {"type": 1, "code": "01000111"},
    "PUSH": {"type": 1, "code": "01000101"},
    "RET":  {"type": 0, "code": "00010001"},
    "SHL":  {"type": 2, "code": "10101100"},
    "SHR":  {"type": 2, "code": "10101101"},
    "ST":   {"type": 2, "code": "10000100"},
    "SUB":  {"type": 2, "code": "10100001"},
    "XOR":  {"type": 2, "code": "10101011"},
                    }
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.SP = 7
        self.reg[self.SP] = 0xF4
        self.pc = 0
        self.fl = 0b00000000
        self.mine_room = []
        
        # Instructions:
        for i in self.OPCODES:
            vars(self)[i] = int(self.OPCODES[i]['code'], 2)
            # print(bin(int(self.OPCODES[i]['code'], 2)))
            # type_pc = bin(vars(self)[i]) >> 6
            # print(type_pc)
            # vars(self)[i]['_pc_type'] = int(str(self.OPCODES[i]['code'])[:2],2)
            # print(vars(self)[i])
        
        
        # self.HLT            = 1
        # self.PRINT_NUM      = 3
        # self.SAVE           = 130  # Save a value to a register
        # self.PRINT_REGISTER = 71  # Print the value in a register
        # self.ADD            = 6 
        # self.SUB            = 7
        # self.MUL            = 162
        # self.DIV            = 9

    def load(self, program):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        
        path = program
        address = 0
        with open(path) as f:
            for line in f:
                # skip empty lines and comments
                if line[0].isnumeric()==False:
                    continue
                self.ram[address] = int(line[0:8], 2)
                address += 1 

        # for instruction in program:
            
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        a_value = self.reg[reg_a]
        b_value = self.reg[reg_b]
        
        if op == self.ADD:
            self.reg[reg_a] += b_value
        elif op == self.SUB:
            self.reg[reg_a] -= b_value
        elif op == self.MUL:
            self.reg[reg_a] *= b_value
        elif op == self.DIV:
            self.reg[reg_a] /= b_value
        # CMP
        elif op == self.CMP:
            if a_value == b_value:
                self.flag = 0b00000001
            elif a_value > b_value:
                self.flag = 0b00000100
            elif a_value < b_value:
                self.flag = 0b00000010
        elif op == self.AND:
            self.reg[reg_a] = a_value & b_value
        elif op == self.OR:
            self.reg[reg_a] = a_value | b_value
        elif op == self.XOR:
            self.reg[reg_a] = a_value ^ b_value
        else:
            raise Exception("Unsupported ALU operation")
    
    def pra(self, reg_address):
        # print(self.reg[reg_address])
        # print(self.reg[reg_address][-3:])
        # return 
        self.mine_room.append(chr(self.reg[reg_address]))
        print(self.mine_room)
        # print(chr(self.reg[reg_address]))

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
        
    def ram_read(self, MAR):
        return self.ram[MAR]
    
    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR

    def run(self):
        """Run the CPU."""
        
        ir = [0] * 8
        math_op = [self.ADD, self.SUB, self.MUL,
                   self.DIV, self.CMP, self.AND, 
                   self.OR, self.XOR]
        # commands = []
        
        # with open(sys.argv[1], "r") as f:
        #     line = f.readlines()
        #     # print(line)
        # for i in line:
        #     if i[0] == "#":
        #         continue
        #     else:
        #         commands.append(int(i[:8],2))
        # f.close()
        
        # self.load(commands)
        # print(commands)
        while True:
            command = self.ram[self.pc]
            if command in math_op:
                reg_a = self.ram[self.pc + 1]
                reg_b = self.ram[self.pc + 2]
                self.alu(command, reg_a, reg_b)
                self.pc += 3
            elif command == self.NOT:
                reg_a = self.ram[self.pc + 1]
                a_value = self.reg[reg_a]
                self.reg[reg_a] = ~a_value
                self.pc += 2
            elif command == self.LDI:
                num = self.ram[self.pc + 2]
                ir = self.ram[self.pc + 1]
                self.reg[ir] = num
                self.pc += 3
            elif command == self.PRN:
                # Print the value in a register
                ir = self.ram[self.pc + 1]
                print(self.reg[ir])
                self.pc += 2
            elif command == self.PUSH:
                
                self.reg[self.SP] -= 1
                ir = self.ram[self.pc + 1]
                reg_val = self.reg[ir]
                self.ram[self.reg[self.SP]] = reg_val
                
                self.pc += 2
                
            elif command == self.POP:
                ram_value = self.ram[self.reg[self.SP]]
                ir = self.ram[self.pc + 1]
                self.reg[ir] = ram_value
                self.reg[self.SP] += 1
                
                self.pc += 2
                
            elif command == self.CALL:
                return_address = self.pc + 2
                self.reg[self.SP] -= 1
                self.ram[self.reg[self.SP]] = return_address
                
                reg_num = self.ram[self.pc + 1]
                self.pc = self.reg[reg_num]
                
            elif command == self.RET:
                self.pc = self.ram[self.reg[self.SP]]
                self.reg[self.SP] += 1
                
            elif command == self.JMP:
                reg_num = self.ram[self.pc + 1]
                reg_address = self.reg[reg_num]
                
                self.pc = reg_address
                
            elif command == self.JEQ:
                if self.flag == 0b00000001:
                    reg_num = self.ram[self.pc + 1]
                    reg_address = self.reg[reg_num]
                
                    self.pc = reg_address
                else:
                    self.pc += 2
                    
            elif command == self.JNE:
                if self.flag != 0b00000001:
                    reg_num = self.ram[self.pc + 1]
                    reg_address = self.reg[reg_num]
                
                    self.pc = reg_address
                else:
                    self.pc += 2
            
            elif command == self.ST:
                reg_b_address = self.ram[self.pc + 2]
                b_value = self.reg[reg_b_address]
                reg_a_address = self.ram[self.pc + 1]
                address_in_a = self.reg[reg_a_address]
                self.reg[address_in_a] = b_value
                
                self.pc += 3
                
            elif command == self.PRA:
                reg_a = self.ram_read(self.pc + 1)
                self.pra(reg_a)
                
                self.pc += 2
            
            elif command == self.IRET:
                self.mine_room = ''.join(self.mine_room)
                print(self.mine_room)
                return self.mine_room
            
            elif command == self.HLT:
                sys.exit(0)
            else:
                print(f"I did not understand that command: {command}")
                sys.exit(1)

