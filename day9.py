file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')
inp = [int(x) for x in inp]

def adds(numSet, mySum):
    looked = set()
    for num in numSet:
        if mySum - num in looked: # We want A + B = 2020. Therefore we can see if 2020 - A to get B, and see if B is in the list
            return True
        looked.add(num)
    return False

def partOne(inp):
    preamble = 25
    numSet = set()
    for num in inp[:preamble]:
        numSet.add(num)
    for i in range(preamble, len(inp)):
        curr = inp[i]
        isValid = adds(numSet, curr)
        if not isValid:
            return curr
        
        last = inp[i - preamble]
        numSet.remove(last)
        numSet.add(curr)

def partTwo(inp):
    goal = 1721308972 # from part one
    count = 0
    contiguous = []
    for num in inp:
        contiguous.append(num)
        count += num
        while count > goal:
            back = contiguous.pop(0)
            count -= back

        if count == goal:
            print(contiguous)
            return min(contiguous) + max(contiguous)


print(partTwo(inp))