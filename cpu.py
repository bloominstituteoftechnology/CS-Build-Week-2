"""CPU functionality."""

import sys
import os
import datetime
import msvcrt, time
script_dir = os.path.dirname(__file__)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.reg[7] = 0xF4
        self.pc = 0
        self.MAR = 0
        self.MDR = 0
        self.FL = 0b00000000
        self.errorcode = 0
        self.stopmoreinterrupts = False
        self.then = datetime.datetime.today()
       

    def load(self,to_load='examples\mult.ls8'):
        """Load a program into memory."""

        address = 0
        with open(os.path.join(script_dir, to_load)) as f:
            program = f.readlines()
            program = [x for x in program if x[0]!='#']
            program = [int(x[:8],2) for x in program] 

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

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "INC":
            self.reg[reg_a] += 1
        elif op == "DEC":
            self.reg[reg_a] -= 1
        elif op == "SUB": 
            self.reg[reg_a] = self.reg[reg_a]-self.reg[reg_b]
        elif op == "MUL": 
            self.reg[reg_a] = self.reg[reg_a]*self.reg[reg_b]
        elif op == "MOD": 
            if self.reg[reg_b]!=0:
                self.reg[reg_a] = self.reg[reg_a]%self.reg[reg_b]
            else:
                raise Exception("can't divide by zero")
        # elif op == "ST": 
        #     self.reg[reg_a] = self.reg[reg_b]
        elif op == "SHL": 
            self.reg[reg_a] = self.reg[reg_a] << self.reg[reg_b]
        elif op == "CMP": 
            if self.reg[reg_a] == self.reg[reg_b]:
                self.FL = 0b00000001
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.FL = 0b00000010
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.FL = 0b00000100

        elif op == "SHR": 
            self.reg[reg_a] = self.reg[reg_a] >> self.reg[reg_b]
        elif op == "XOR": 
            self.reg[reg_a] = self.reg[reg_a] ^ self.reg[reg_a]
        elif op == "OR": 
            self.reg[reg_a] = self.reg[reg_a] | self.reg[reg_a]
        elif op == "NOT": 
            self.reg[reg_a] = ~self.reg[reg_a]
        elif op == "AND": 
            self.reg[reg_a] = self.reg[reg_a] & self.reg[reg_a]
        elif op == "DIV": 
            if self.reg[reg_b]!=0:
                self.reg[reg_a] = self.reg[reg_a]/self.reg[reg_b]
            else:
                raise Exception("can't divide by zero")
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self,address):
        return self.ram[address]
    
    def ram_write(self,address,value):
        self.ram[address] = value

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

    def run(self):
        """Run the CPU."""
        while self.pc!='HALT':
            time.sleep(0.01)
            if not self.stopmoreinterrupts:
                if msvcrt.kbhit():
                    self.ram[0xF4] = ord(msvcrt.getch())
                    #print('key trigger',chr(self.ram[0xF4]),'**********',self.ram[0xF4])
                    self.reg[6] = 0b00000010
                    self.stopmoreinterrupts = True
            #check timer
            if not self.stopmoreinterrupts:
                now = datetime.datetime.today()
                if (now - self.then).seconds > 0:
                    #print('timer interrupt trigger')
                    self.then = now
                    #print('A')
                    self.reg[6] = 0b00000001
                else:
                    self.reg[6] = 0b00000000
            #interrupt handle
            #first IM & IS register bitwise &ed and stored in masked interrupts 
            maskedInterrupts = (self.reg[5] & self.reg[6])
            #print(bin(maskedInterrupts),'mi',bin(self.reg[5]),'5',bin(self.reg[6]),'6')
            i=0
            while (maskedInterrupts >> i) % 0b10 != 0b1 and i<8:
                i=i+1
            if i<8:  #if triggered
                #print('*************************interrupt triggered')
                self.stopmoreinterrupts = True
                self.reg[6]=0b00000000
                self.reg[7] -=1
                self.ram[self.reg[7]] = self.pc
                self.reg[7] -=1
                self.ram[self.reg[7]] = self.FL
                for j in range(7):
                    self.reg[7]-=1
                    self.ram[self.reg[7]] = self.reg[j]
                # address (vector) of the appr handler looked up from the interrupt vector table.
                self.pc = self.ram[0xF8+i]
            #mainloop
            opp_dict = {0b0000:'ADD', 0b0001:'SUB', 0b0101:'INC', 0b0110:'DEC', 0b0010:'MUL', 0b0011:'DIV',
                        0b1011:'XOR', 0b0100:'ST', 0b1010:'OR',0b1100:'SHL', 0b1101:'SHR',0b1000 : 'AND',
                        0b0111 :'CMP',0b1001:'NOT'}
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)
            if self.errorcode == f'pc{self.pc}ir{ir}a{operand_a}b{operand_b}':
                self.pc='HALT'
            #print('flag',bin(self.FL),'pc',self.pc,'ir',bin(ir),'a',operand_a,'b',operand_b)#,bin(self.reg[operand_a]))
            self.errorcode = f'pc{self.pc}ir{ir}a{operand_a}b{operand_b}'
            if ((ir >>5 ) % 0b10) == 0b1 :
                #print('ALU trigger')  ## USE ALU
                self.alu(opp_dict[ir % (ir>>4)],operand_a,operand_b)
                self.pc += (ir >> 6) + 1
            elif ir == 0b00000000:
                #NOP
                pass
            elif ir == 0b01010000:
                # CALL - first push address of next instruction onto stack
                self.reg[7] -=1
                self.ram[self.reg[7]] = self.pc+2
                #then set pc equal to call address
                self.pc = self.reg[operand_a]
                pass
            elif ir == 0b00000001:
                # HLT
                self.pc = 'HALT'
            elif ir == 0b01010010:
                
                # INT
                #set nth bit of IS register to given register
                self.reg[6]= 0b1 << self.reg[operand_a] 

            elif ir == 0b000010011: 
                # IRET
                #R6 to #R0 popped off stack
                for i in range(7):
                    self.reg[6-i] = self.ram[self.reg[7]]
                    self.reg[7]+=1
                #FL register popped off stack
                self.FL = self.ram[self.reg[7]]
                self.reg[7] +=1
                self.pc = self.ram[self.reg[7]]
                self.reg[7] +=1
                self.stopmoreinterrupts = False


            elif ir ==0b01010101:
                # JEQ
                if self.FL % 0b10 == 0b1:
                    self.pc = self.reg[operand_a]
                else:
                    self.pc+=2
            elif ir ==0b01011010:
                # JGE
                if self.FL % 0b10==0b1 or (sl.FL >> 1)%0b10==0b1:
                    self.pc = self.reg[operand_a]
                else:
                    self.pc+=2
            elif ir == 0b01011001:
                #JLE
                if self.FL % 0b10==0b1 or (sl.FL >> 2)%0b10==0b1:
                    self.pc = self.reg[operand_a]
                else:
                    self.pc+=2
            elif ir == 0b01011000:
                #JLT
                if (sl.FL >> 2)%0b10==0b1:
                    self.pc = self.reg[operand_a]
                else:
                    self.pc+=2
            elif ir == 0b01010100:
                #JMP
                self.pc = self.reg[operand_a]
            elif ir == 0b01010110:
                #JNE
                if self.FL % 0b10==0b0:
                    self.pc = self.reg[operand_a]
                else:
                    self.pc+=2
            elif ir == 0b10000011:
                # LD
                #print(operand_b,self.ram[operand_b],'****LD check')
                self.reg[operand_a] = self.ram[self.reg[operand_b]]
                self.pc+=3
            elif ir == 0b10000010:
                #print('LDI trigger')
                #LDI - sets value of register qual to integer
                self.reg[operand_a] = operand_b
                self.pc+=3
            elif ir == 0b01001000:
                #PRA
                #print('PRA check',self.reg[operand_a])
                #print(chr(self.reg[operand_a]))
                print(chr(self.reg[operand_a]),end='')
                self.pc +=2
            elif ir == 0b01000111:
                #PRN
                print(self.reg[operand_a])
                self.pc +=2
            elif ir == 0b01000101:
                #PUSH
                self.reg[7] -=1
                self.ram[self.reg[7]] = self.reg[operand_a]
                self.pc +=2

            elif ir == 0b01000110:
                #POP
                self.reg[operand_a] = self.ram[self.reg[7]]
                self.reg[7] +=1
                self.pc +=2

            elif ir == 0b00010001:
                #RET
                self.pc = self.ram[self.reg[7]]
                self.reg[7] += 1

            elif ir == 0b10000100:
                #ST
                self.ram[self.reg[operand_a]] = self.reg[operand_b]
                self.pc +=3
            
            elif ir == 0b10001111:
                #ADDI - add an immediate value to a register
                self.reg[operand_a] = self.reg[operand_a] + operand_b
                self.pc +=3



        exit()

        
        


