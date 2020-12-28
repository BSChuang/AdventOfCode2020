file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')

def parseInstr(instr):
    op, arg = instr.split()
    return op, int(arg)

def partOne(inp):
    acc = 0
    pc = 0
    inp = [parseInstr(instr) for instr in inp]

    checked = []

    while pc not in checked:
        checked.append(pc)
        op, arg = inp[pc]
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
    
    return acc

def partTwo(inp):
    inp = [parseInstr(instr) for instr in inp]
    return recursion(inp, [], 0, 0, False)

def recursion(inp, checked, acc, pc, swapped):
    while pc not in checked:
        if pc == len(inp):
            return acc
        checked.append(pc)
        op, arg = inp[pc]
        if op == 'nop':
            if not swapped:
                result = recursion(inp, checked.copy(), acc, pc + arg, True) # As if we executed jmp instead
                if result != None: # If it has looped, ignore this reality
                    return result
            pc += 1
        elif op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            if not swapped:
                result = recursion(inp, checked.copy(), acc, pc + 1, True) # As if we executed nop instead
                if result != None: # If it has looped, ignore this reality
                    return result
            pc += arg
    
    return None



print(partTwo(inp))