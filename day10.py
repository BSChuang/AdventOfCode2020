file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')
inp = [int(x) for x in inp]

def partOne(inp):
    adapters = set(inp)
    joltage = 0
    oneDiff = 0
    threeDiff = 0
    while len(adapters) > 0:
        for i in range(1, 4):
            if joltage + i in adapters:
                if i == 1:
                    oneDiff += 1
                elif i == 3:
                    threeDiff += 1

                joltage += i
                adapters.remove(joltage)
                break
    return oneDiff * (threeDiff + 1)

def partTwo(inp):
    inp = sorted(inp) + [max(inp) + 3]
    reachable = {0: 1}
    for num in inp:
        count = 0
        for i in range(1, 4):
            if num - i in reachable:
                count += reachable[num - i]
            reachable[num] = count
    
    return reachable[max(inp)]

print(partTwo(inp))