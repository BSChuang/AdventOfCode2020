file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')

def partOne(inp, slopeX, slopeY):
    pos = (0, 0)
    hit = 0
    while pos[0] < len(inp):
        if inp[pos[0]][pos[1] % len(inp[0])] == '#':
            hit += 1
        pos = (pos[0] + slopeY, pos[1] + slopeX)

    return hit

def partTwo(inp):
    return partOne(inp, 1, 1) * partOne(inp, 3, 1) * partOne(inp, 5, 1) * partOne(inp, 7, 1) * partOne(inp, 1, 2)

print(partTwo(inp))