with open("inputs/17.txt") as f:
    a = f.readline()
    b = f.readline()
    c = f.readline()
    a, b, c = a.strip(), b.strip(), c.strip()
    a, b, c = a.split()[2], b.split()[2], b.split()[2]
    a, b, c = int(a), int(b), int(c)
    f.readline()
    program = f.readline()
    program = program.strip()
    program = program.split()[1]
    program = program.split(",")
    program = [int(p) for p in program]

def combo_operand(operand, a, b, c):
    match operand:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return a
        case 5: return b
        case 6: return c
        case 7: raise ValueError()


def step(
    a, 
    b, 
    c, 
    instruction_pointer, 
    program,
    output,
):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer+1]
    match opcode:
        case 0: #adv
            a = int(a / 2**combo_operand(operand, a, b, c))
            instruction_pointer += 2
        case 1: #bxl
            b = b ^ operand
            instruction_pointer += 2
        case 2: #bst
            b = combo_operand(operand, a, b, c) % 8
            instruction_pointer += 2
        case 3: #jnz
            if a == 0:
                instruction_pointer += 2
            else:
                instruction_pointer = operand
        case 4: #bxc
            b = b ^ c
            instruction_pointer += 2
        case 5: #out
            output.append(combo_operand(operand, a, b, c) % 8)
            #if output != program[:len(output)]:
            #    instruction_pointer = 1000 # shortcut out of the program
            instruction_pointer += 2
        case 6: #bdv
            b = int(a / 2**combo_operand(operand, a, b, c))
            instruction_pointer += 2
        case 7: #cdv
            c = int(a / 2**combo_operand(operand, a, b, c))
            instruction_pointer += 2
    
    return a, b, c, instruction_pointer, output

def test_value(a, l):
    a, b, c = a, 0, 0
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(program):
        a, b, c, instruction_pointer, output = step(a, b, c, instruction_pointer, program, output)
    if output == program[-l:]:
        return True
    return False

a = 0
l = 1
while l <= len(program):
    if test_value(a, l):
        if l == len(program):
            print(a)
            exit()
        a = a*8
        l += 1
    else:
        a += 1
