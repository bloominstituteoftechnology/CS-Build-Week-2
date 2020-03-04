import sys
​
PRINT_BEEJ     = 1
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4  # Save a value to a register
PRINT_REGISTER = 5  # Print the value in a register
ADD            = 6  # ADD 2 registers, store the result in 1st reg
​
​
memory = [
    PRINT_BEEJ,
    SAVE,  # SAVE 65 in R2
    65,
    2,
    SAVE,  # SAVE 20 in R3
    20,
    3,
    ADD,   # R2 += R3
    2,
    3,
    PRINT_REGISTER,  # PRINT R2 (85)
    2,
    HALT
]
​
register = [0] * 8
​
pc = 0  # Program counter
​
while True:
    command = memory[pc]
​
    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1
    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2
    elif command == SAVE:
        # Save a value to a register
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3
    elif command == PRINT_REGISTER:
        # Print the value in a register
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2
    elif command == ADD:
        # ADD 2 registers, store the result in 1st reg
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3
    elif command == HALT:
        sys.exit(0)
    else:
        print(f"I did not understand that command: {command}")
        sys.exit(1)