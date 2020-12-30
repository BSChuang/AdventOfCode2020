file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')

dirDict = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

def partOne(inp):
    x = 0
    y = 0
    direction = 1 # 0: north, 1: east, 2: south, 3: west
    for str in inp:
        action = str[0]
        num = int(str[1:])

        if action == 'N' or (action == 'F' and dirDict[direction] == 'N'):
            y += num
        elif action == 'S' or (action == 'F' and dirDict[direction] == 'S'):
            y -= num
        elif action == 'E' or (action == 'F' and dirDict[direction] == 'E'):
            x += num
        elif action == 'W' or (action == 'F' and dirDict[direction] == 'W'):
            x -= num
        elif action == 'L':
            direction = (direction - num / 90) % 4
        elif action == 'R':
            direction = (direction + num / 90) % 4

    return abs(x) + abs(y)

print(partOne(inp))