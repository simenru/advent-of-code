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

INSTRUCTION_POINTER = 0
OUTPUT = []

def combo_operand(operand):
    match operand:
        case 0: return 0
        case 1: return 1
        case 2: return 2
        case 3: return 3
        case 4: return a
        case 5: return b
        case 6: return c
        case 7: raise ValueError()


def apply_instruction(opcode, operand):
    global INSTRUCTION_POINTER
    global OUTPUT
    global a, b, c, program

    match opcode:
        case 0: #adv
            a = int(a / 2**combo_operand(operand))
            INSTRUCTION_POINTER += 2
        case 1: #bxl
            b = b ^ operand
            INSTRUCTION_POINTER += 2
        case 2: #bst
            b = combo_operand(operand) % 8
            INSTRUCTION_POINTER += 2
        case 3: #jnz
            if a == 0:
                INSTRUCTION_POINTER += 2
            else:
                INSTRUCTION_POINTER = operand
        case 4: #bxc
            b = b ^ c
            INSTRUCTION_POINTER += 2
        case 5: #out
            OUTPUT.append(combo_operand(operand) % 8)
            INSTRUCTION_POINTER += 2
        case 6: #bdv
            b = int(a / 2**combo_operand(operand))
            INSTRUCTION_POINTER += 2
        case 7: #cdv
            c = int(a / 2**combo_operand(operand))
            INSTRUCTION_POINTER += 2

while INSTRUCTION_POINTER < len(program):
    opcode = program[INSTRUCTION_POINTER]
    operand = program[INSTRUCTION_POINTER + 1]
    apply_instruction(opcode, operand)

print(",".join([str(o) for o in OUTPUT]))