import copy

file = open('input.txt', 'r')
inp = file.read()
file.close()

inp = inp.split('\n')
inp = [[char for char in str] for str in inp]

def adjacent(layout, row, col):
    adj = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if row + i < 0 or row + i >= len(layout):
                continue
            if col + j < 0 or col + j >= len(layout[0]):
                continue

            adj.append(layout[row + i][col + j])

    return adj

def compareLayout(layout1, layout2):
    for i in range(len(layout1)):
        for j in range(len(layout1[0])):
            if layout1[i][j] != layout2[i][j]:
                return False

    return True

def countOccupied(layout):
    count = 0
    for row in layout:
        count += row.count('#')
    return count

def partOne(inp):
    prevLayout = inp
    while True:
        newLayout = copy.deepcopy(prevLayout)
        for i in range(len(prevLayout)):
            for j in range(len(prevLayout[0])):
                adj = adjacent(prevLayout, i, j)
                if prevLayout[i][j] == 'L' and '#' not in adj:
                    newLayout[i][j] = '#'
                elif prevLayout[i][j] == '#' and adj.count('#') >= 4:
                    newLayout[i][j] = 'L'

        if compareLayout(prevLayout, newLayout):
            return countOccupied(newLayout)
        
        prevLayout = newLayout

def los(layout, row, col): # line of sight (adjacent for part 2)
    adj = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            y = row
            x = col
            while True:
                y += i
                x += j
                if y < 0 or y >= len(layout):
                    break
                if x < 0 or x >= len(layout[0]):
                    break
                if layout[y][x] != '.':
                    adj.append(layout[y][x])
                    break
    return adj

def partTwo(inp):
    prevLayout = inp
    while True:
        newLayout = copy.deepcopy(prevLayout)
        for i in range(len(prevLayout)):
            for j in range(len(prevLayout[0])):
                adj = los(prevLayout, i, j)
                if prevLayout[i][j] == 'L' and '#' not in adj:
                    newLayout[i][j] = '#'
                elif prevLayout[i][j] == '#' and adj.count('#') >= 5:
                    newLayout[i][j] = 'L'

        if compareLayout(prevLayout, newLayout):
            return countOccupied(newLayout)
        
        prevLayout = newLayout

print(partTwo(inp))